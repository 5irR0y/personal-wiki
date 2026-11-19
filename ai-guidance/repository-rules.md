# Personal wiki — repository rules

This repo is Leroy’s **life / non-work** knowledge base. It is standalone and separate from the work wiki (`personal-work-wiki`).

## Scope

- Everything in this repo is personal by default; no need to ask.
- **Work-adjacent content is allowed here:** resume, work history, career-search material, and notes about co-workers that matter personally. Stored under `projects/phoenix/` or a `people/` / `reference/` folder if one is added.
- **Day-to-day work records do not belong here:** meetings, team to-dos, 1:1 topics, project status, and the company contact directory live in the work wiki. If asked to file those here, point that out and ask.
- Company benefits and employment logistics (PTO, 401(k), HSA, equity) stay in the work wiki unless Leroy explicitly asks for a specific item here.
- Never depend on paths outside this repo. Do not link to the work wiki; refer to it by name in prose only.

## Folder map

| Folder | Purpose |
| --- | --- |
| `Personal Inbox/` | Temporary drop zone for personal files. Process promptly; nothing durable stays here |
| `todos/` | Open and archived life to-dos |
| `projects/` | Active life projects (trips, plans) |
| `projects/archive/` | Closed life projects |
| `media/` | Movie / TV watch history (`watch-history.json`). Schema and IMDb import steps are in `media/README.md` |
| `ai-guidance/` | Operating rules for this personal wiki |
| `.cursor/rules/` | Cursor rules (copy with the folder if spun into its own repo) |

Suggest new subfolders (`people/`, `meetings/`, `reference/`, …) when content repeatedly needs a home.

## Personal Inbox

Anything dropped in
`Personal Inbox/` is personal by definition, so there's no need to ask whether it's work.

- Reading files there counts as processing them. In the same turn, file the content and **move** the
  source to a permanent folder (e.g. IMDb exports → `media/sources/YYYY-MM-DD-imdb-watch-history.txt`).
  Moving doesn't need permission.
- Never leave processed files or scratch folders in `Personal Inbox/`.
- Ask before **deleting** an original.

## Archiving projects

When a life project is finished (trip taken, plan executed):

1. Put a **Status: Closed YYYY-MM-DD** line under the H1 saying what happened, and check off any
   remaining boxes rather than deleting them. If the boxes were checked in one pass at close-out
   rather than verified individually, say so in that line.
2. `git mv` the file (and any `.html` print copy) into `projects/archive/`.
3. Move the matching to-dos to `todos/archive.md`, keeping the parent/sub-item structure intact,
   and repoint links to `../projects/archive/…`.

## To-dos

- Open list: `todos/open.md`. Archive: `todos/archive.md`.
- “Add this to my **personal** to-do list” → `todos/open.md`. Set **Created** to today. Assign next id (`Pers-###`).
- Showing / completing / recurring behavior uses the order Overdue → Today → Recurring → Lower Priority, and **all items here are personal** — no separate `Personal: yes` marker needed for new items.
- Recurring: definitions under **Recurring definitions**; materialize active instances only when he asks to see the **personal** to-do list. Cadences: `daily`, `weekly <Weekday>`, `monthly day-N`, `every-N-days`. Calendar-day math from last archive **Done**.
- Completing: “#N is done” against the most recent numbered **personal** list shown. One-time → archive; recurring → log occurrence, leave definition.

## Trip checklists (e.g. `projects/archive/poland-trip-2026-09-12-*`)

**Poland trip: closed 2026-09-21** — trip ran 2026-09-12 → 2026-09-17 and was successful. All four
files are now under `projects/archive/`; the to-dos are in `todos/archive.md`. The rules below apply to
the *next* trip checklist.

- **Never delete a completed item while the trip is live.** When Leroy says something is done, leave the
  line where it is and check the box: `☐` → `☑` in the trip plans, `- [ ]` → `- [x]` in `todos/open.md`.
  Add a short `Done <date>` / `Done: YYYY-MM-DD` note. This overrides the archive-on-completion rule
  above until the trip is over — he wants to see the whole list and what is already crossed off. Once the
  trip is done, archive it as described above.
- When a trip has both a `-leroy` and a `-family` plan plus `.html` print copies, all of them carry the
  same content. Update them together so the fridge copy never falls behind.
