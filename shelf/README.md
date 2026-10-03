# The shelf, version 2

The family's apps (Media, Logbook, Health) live on one website and leave each other cards in a small IndexedDB called `shelf`.

- `shelf.ts` is the contract: the store, the card shape, and a check for every format and version. It has no imports.
- `fixtures/` holds one valid card per format. They're examples with no personal data.
- **Each app keeps byte-identical copies** of `shelf.ts` and the fixtures it reads or writes, and a test checks them against this folder whenever the suite repository sits beside it.
- **To change a format,** add a new version (a new `format@version` check and fixture), let readers accept both, and retire the old one later. Never change a published version in place.

| Format | From → to | About |
|---|---|---|
| `media.day` v1 | Media → Logbook | a day: what was noted, started, finished or rated, with ratings as they stood that day |
| `media.catalogue` v1 | Media → Logbook | the works, so `/` in Logbook can suggest them |
| `logbook.mention` v1 | Logbook → Media | a Logbook line that links a work |
| `logbook.handover` v1 | Logbook → Media | one media entry moving to Media |
| `media.receipt` v1 | Media → Logbook | Media has that entry, safely |
| `logbook.share` v1 | Logbook → Media | a link shared into Logbook as "watched" |
| `health.day` v2 | Health → Logbook | Health's day |
