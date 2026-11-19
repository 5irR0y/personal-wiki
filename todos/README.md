# Personal to-do conventions

Life / non-work action tracking. Open list: [open.md](open.md). Completed: [archive.md](archive.md).

## Chat: show my personal to-do list

Recurring items are materialized when the list is shown, using calendar-day math from the last archive **Done** date. Cadences: `daily`, `weekly <Weekday>`, `monthly day-N`, `every-N-days`.

Display sections (number continuously):

1. **Overdue**
2. **Today**
3. **Recurring** — prepend `D:` / `W:` / `M:` / `X{N}:`
4. **Lower Priority**

Do not show Created dates or internal ids unless needed to disambiguate.

## Adding / completing

- Add → `open.md` with **Created** = today; next id `Pers-###`.
- Complete → move/log in `archive.md` with **Done** date.
- Recurring: definition stays; archive each occurrence; rematerialize when the personal list is shown and due.
