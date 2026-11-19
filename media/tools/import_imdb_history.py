"""Merge an IMDb "watch history" page copy-paste into ../watch-history.json.

Usage:  python -I import_imdb_history.py <export.txt> [--as-of YYYY-MM-DD]

- New titles are appended with empty placeholders for the fields IMDb's page doesn't show.
- Existing titles (matched on imdb_id, else title + year + kind) only get their IMDb-sourced
  fields refreshed (rating, votes, certificate, runtime, end_year). Hand-entered fields
  (viewings, status, seasons, lists, directors, genres, cast, notes) are never touched.
"""
import json
import re
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "watch-history.json"

SCORE_RE = re.compile(r"^(\d+(?:\.\d)?) \(([\d.]+[KM]?)\)$")
KINDS = {
    "TV Mini Series": "tv-mini-series",
    "TV Series": "tv-series",
    "TV Movie": "tv-movie",
    "TV Special": "tv-special",
    "TV Short": "tv-short",
    "TV Episode": "tv-episode",
    "Video Game": "video-game",
    "Video": "video",
    "Short": "short",
}
META_RE = re.compile(
    r"^(?P<year>\d{4})(?P<range>–(?P<end>\d{4})?\s?)?"
    r"(?P<rt>\d+h(?: \d+m)?|\d+m)?"
    r"(?P<rest>.*)$"
)


def runtime_minutes(rt):
    if not rt:
        return None
    h = re.search(r"(\d+)h", rt)
    m = re.search(r"(\d+)m", rt)
    return (int(h.group(1)) * 60 if h else 0) + (int(m.group(1)) if m else 0)


def parse_blocks(text):
    """Yield (caption, [indented lines], score_line) per entry."""
    lines = [l.rstrip() for l in text.replace("\r", "").split("\n")]
    caption, body = None, []
    for line in lines:
        if not line.strip():
            continue
        if line.startswith("    "):
            body.append(line.strip())
        elif SCORE_RE.match(line.strip()):
            yield caption, body, line.strip()
            caption, body = None, []
        else:
            if caption is not None and body:  # entry with no score line
                yield caption, body, None
                body = []
            caption = line.strip()
    if caption is not None and body:
        yield caption, body, None


def parse_entry(caption, body, score):
    e = {"title": body[0], "imdb_rating": None, "imdb_votes": None}
    if score:
        m = SCORE_RE.match(score)
        e["imdb_rating"], e["imdb_votes"] = float(m.group(1)), m.group(2)
    if len(body) > 2 and re.match(r"^S\d+\.E\d+$", body[1]):  # episode layout
        s, ep = re.findall(r"\d+", body[1])
        e.update(kind="tv-episode", series=body[2], season=int(s), episode=int(ep))
        for v in body[3:]:
            if re.fullmatch(r"\d{4}", v):
                e["year"] = int(v)
            elif re.fullmatch(r"\d+h(?: \d+m)?|\d+m", v):
                e["runtime_minutes"] = runtime_minutes(v)
            elif v != "TV Episode":
                e["certificate"] = v
        return e
    meta = body[1] if len(body) > 1 else ""
    m = META_RE.match(meta)
    if not m:
        raise ValueError(f"Unparsed metadata for {body[0]!r}: {meta!r}")
    rest, kind = m.group("rest").strip(), "movie"
    for label, k in KINDS.items():
        if rest.endswith(label):
            rest, kind = rest[: -len(label)].strip(), k
            break
    e.update(
        kind=kind,
        year=int(m.group("year")),
        end_year=int(m.group("end")) if m.group("end") else None,
        ongoing=bool(m.group("range")) and not m.group("end"),
        runtime_minutes=runtime_minutes(m.group("rt")),
        certificate=rest or None,
    )
    return e


def new_record(e):
    is_show = e["kind"] in ("tv-series", "tv-mini-series")
    rec = {
        "imdb_id": None,
        "imdb_url": None,
        "title": e["title"],
        "kind": e["kind"],
        "year": e["year"],
        "end_year": e.get("end_year"),
        "ongoing": e.get("ongoing", False),
        "runtime_minutes": None if is_show else e.get("runtime_minutes"),
        "certificate": e.get("certificate"),
        "imdb_rating": e["imdb_rating"],
        "imdb_votes": e["imdb_votes"],
        "directors": [],
        "genres": [],
        "cast": [],
        "status": None,
        "viewings": [],
        "lists": [],
        "notes": "",
    }
    if is_show:
        rec["season_count"] = None
        rec["seasons"] = []
    return rec


def key(r):
    return (r["title"].casefold(), r["year"], r["kind"])


def main():
    args = sys.argv[1:]
    as_of = args[args.index("--as-of") + 1] if "--as-of" in args else None
    src = Path(args[0])
    db = json.loads(DATA.read_text(encoding="utf-8"))
    by_key = {key(r): r for r in db["titles"]}
    entries = [parse_entry(*b) for b in parse_blocks(src.read_text(encoding="utf-8"))]

    added = updated = dupes = 0
    seen = set()
    episodes = [e for e in entries if e["kind"] == "tv-episode"]
    for e in entries:
        if e["kind"] in ("tv-episode", "video-game"):  # games aren't watch history
            continue
        k = key(e)
        if k in seen:
            dupes += 1
            print(f"duplicate row skipped: {e['title']} ({e['year']})")
            continue
        seen.add(k)
        if k in by_key:
            r = by_key[k]
            for f in ("imdb_rating", "imdb_votes", "certificate", "end_year", "ongoing"):
                if e.get(f) is not None:
                    r[f] = e[f]
            if r["kind"] not in ("tv-series", "tv-mini-series") and e.get("runtime_minutes"):
                r["runtime_minutes"] = e["runtime_minutes"]
            updated += 1
        else:
            r = new_record(e)
            db["titles"].append(r)
            by_key[k] = r
            added += 1

    # Fold watched episodes into their show's season entry.
    for ep in episodes:
        show = next((r for r in db["titles"] if "seasons" in r
                     and r["title"].casefold() == ep["series"].casefold()), None)
        if show is None:  # only episodes were in the export; create the show
            show = new_record({"title": ep["series"], "kind": "tv-series", "year": ep["year"],
                               "imdb_rating": None, "imdb_votes": None})
            show["notes"] = "Created from episode rows; series vs. mini-series not confirmed."
            db["titles"].append(show)
            added += 1
        season = next((s for s in show["seasons"] if s["season"] == ep["season"]), None)
        if season is None:
            season = {"season": ep["season"], "status": None, "episodes_watched": []}
            show["seasons"].append(season)
            show["seasons"].sort(key=lambda s: s["season"])
        if ep["episode"] not in season["episodes_watched"]:
            season["episodes_watched"].append(ep["episode"])
            season["episodes_watched"].sort()

    if as_of:
        db["imdb_data_as_of"] = as_of
    DATA.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"parsed {len(entries)} entries ({len(episodes)} episodes): "
          f"{added} added, {updated} refreshed, {dupes} duplicate rows skipped")


if __name__ == "__main__":
    main()
