# Media — movies and TV watch history

| File | Use |
| --- | --- |
| [watch-history.json](watch-history.json) | Source of truth: every movie / show watched |
| [tools/import_imdb_history.py](tools/import_imdb_history.py) | Merges a new IMDb watch-history paste into the JSON |
| [sources/](sources/) | Raw IMDb exports, named `YYYY-MM-DD-imdb-watch-history.txt` |

## Updating from IMDb

1. Copy the IMDb **watch history** page into a `.txt` and drop it in `Personal Inbox/`.
2. Run `python -I media/tools/import_imdb_history.py "<file>" --as-of YYYY-MM-DD`.
   New titles are added. Existing titles only get their IMDb fields refreshed (rating, votes,
   certificate, runtime, end year). Fields you entered by hand are never overwritten.
3. Move the file to `sources/`.

## Top-level structure

```json
{
  "schema_version": 1,
  "imdb_data_as_of": "2026-10-24",   // date of the export the ratings/votes came from
  "lists": { "<list-id>": { "name", "url", "changes", "entry_fields", "tagging_status" } },
  "titles": [ ... ]
}
```

## Title record

| Field | Type | Notes |
| --- | --- | --- |
| `imdb_id` | string \| null | `tt0120815`. Not in the watch-history paste; to be filled in |
| `imdb_url` | string \| null | `https://www.imdb.com/title/<imdb_id>/` |
| `title` | string | As IMDb shows it |
| `kind` | string | `movie`, `tv-series`, `tv-mini-series`, `tv-movie`, `tv-special`, … (video-game rows in an export are skipped) |
| `year` | int | Release year, or first-air year for shows |
| `end_year` | int \| null | Shows only: last-air year |
| `ongoing` | bool | Shows only: IMDb lists it as `2022–` (still airing) |
| `runtime_minutes` | int \| null | Movies only (null for shows) |
| `certificate` | string \| null | `R`, `PG-13`, `TV-MA`, `Not Rated`, … |
| `imdb_rating` | number \| null | 1–10, as of `imdb_data_as_of` |
| `imdb_votes` | string \| null | As IMDb shows it (`1.7M`, `13K`) |
| `directors` | string[] | |
| `genres` | string[] | IMDb genres |
| `cast` | string[] | Actors / actresses |
| `status` | `finished` \| `dnf` \| null | Overall. null = not recorded yet |
| `viewings` | object[] | One per watch: `{ "date": "2026-10-24" \| "2026-10" \| "2026" \| null, "status": "finished" \| "dnf", "notes": "" }` |
| `lists` | object[] | Notable-list tags, see below |
| `notes` | string | Free text |

**Shows only:**

| Field | Type | Notes |
| --- | --- | --- |
| `season_count` | int \| null | Number of seasons the show has |
| `seasons` | object[] | `{ "season": 1, "status": "finished" \| "dnf" \| "not-started" \| null, "episodes_watched": [1, 2, 3] }` |

## Notable lists

Each tag in a title's `lists` names a list defined at the top of the file, plus that list's own fields:

```json
"lists": [
  { "list": "oscar-best-picture", "ceremony_year": 1999 },
  { "list": "imdb-top-250-movies", "rank": 52, "as_of": "2026-10-24" }
]
```

- `oscar-best-picture` (Best Picture winners). Membership is permanent.
- `imdb-top-250-movies` / `imdb-top-250-tv` (IMDb Top 250). These charts move all the time, so
  each tag carries the rank and the date checked. A refresh rewrites these tags from a new snapshot.

To add a new list, define it under `lists` with an id, name, URL and `entry_fields`, then tag titles.
