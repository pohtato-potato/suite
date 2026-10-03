# The app family: map and shared rules

**Date:** 3 October 2026
**Status:** agreed in conversation; written up for review.
**Scope:** how the personal web apps fit together, who owns which data, what passes between them, the groundwork they share, and the order to build them in. Each app still gets its own design round and its own spec.

## 1. Purpose

A family of small personal web apps, each with its own character, that share data without stepping on each other. This map exists so that:

- each new app slots in without reworking the ones already built;
- every kind of data has exactly one owning app;
- the next build is chosen deliberately, not by whichever idea is loudest.

## 2. Ground rules shared by every app

These come from Health and Logbook and hold for every app in the family:

- **Data lives on the phone** (IndexedDB in Chrome on the Samsung S23), with the laptop as a full second home where the app supports it. No server, no accounts, no analytics.
- **Code is public and holds no personal data.** Personal details arrive through a private starter file that is never committed, or are typed in.
- **Each app lives at `pohtato-potato.github.io/<app>/`** and its address never changes.
- **Each app has its own character:** its own look, voice and personality. There is no shared visual style.
- **Each kind of data has exactly one owning app.** Other apps only see it through postcards (section 5).
- **Nothing is published or pushed without asking.**

## 3. The family

| App | Status | One line |
|---|---|---|
| **Health** | Built | Food, steps, sleep, training and body. |
| **Logbook** | Built | The daily hub: a low-effort archive of life, organised by day. |
| **Media** | Next to build | An in-depth collection of films, shows, books and other works, with ratings, reviews and what you took from them. |
| **Inventory** | Planned, second | Everything owned and wanted, with the wardrobe at its centre. |
| **Places** | Planned, third | Places, visits and the map, including the Google Maps Timeline import. |
| **Commonplace** | Maybe, parked | A commonplace book: passages and ideas collected by topic, from any source. |

Dropped: **People.** People stay in Logbook.

## 4. Who owns what

| App | Owns |
|---|---|
| Health | body measures, food, water, steps, sleep, training, check-ins, the India walk |
| Logbook | days, lines, feelings (moments and the day overall), photos of the day, keepsakes, voice notes, spans, tags, people, marks |
| Media | works (films, shows, books, and whichever other kinds Media's own design adds), ratings, reviews and thoughts, watchlist, progress, rewatches and rereads, quotes from works |
| Inventory | belongings, wardrobe items, outfits, wear history, packing lists, wish-list |
| Places | places, visits, the Timeline import, places to go |
| Commonplace (if built) | passages and ideas filed by topic |

### Moves this causes in Logbook

Logbook was designed before the family took shape, so two things move out of it:

1. **Films, books and shows move to Media.** Logbook stops capturing them (the + sheet entry, the 1–7 rating, the "Currently" pin, the shelf page) and shows Media's postcards instead. Entries already kept in Logbook move to Media once Media can import them. Nothing is deleted before it has arrived safely in Media.
2. **Places and the Timeline import move to Places** when Places is built. Until then Logbook keeps them as they are.

Each move is planned and done inside the receiving app's build, and Logbook's export keeps working throughout.

### Quotes

There are three possible homes for a quote. The rule:

- A quote from a work (a book, film or show) belongs to **Media**.
- A line overheard or said on a day belongs to **Logbook**.
- If Commonplace is ever built, it takes over passages filed by topic, and section 4 is revised then.

## 5. What passes between apps (postcards)

Agreed flows so far. More will be added as each app is designed.

| From | To | What |
|---|---|---|
| Health | Logbook | The day's steps, sleep, workout, check-in, walk progress and a line in Health's voice. **Built, contract v1.** |
| Media | Logbook | What was watched, read, started or finished that day, with the rating. |
| Logbook | Media | How a work made you feel, in Logbook's feeling words. |
| Places | Logbook | Where you went that day. |
| Health | Places | Walks and steps on the days a place was visited. |
| Inventory | Logbook | The outfit of the day, on days you choose to log it; new things bought. |
| Logbook ↔ Inventory | both ways | A gift marked in Logbook shows on the item as "gift from…", and the reverse. |

## 6. Shared groundwork

### 6.1 Shelf version 2

The shelf today is the `shelf` IndexedDB database on the shared website, with one store of postcards. Health writes and Logbook reads, one card per day. Version 2 must allow:

- **any app to leave a card for any other app**, with the sender and the intended reader named on the card;
- **cards about one item, not only one day** (feelings about one film; a gift linked to one belonging);
- **every card format versioned** and pinned by a fixture, as v1 is.

Health's v1 postcard keeps working unchanged until both Health and Logbook have moved to v2. The detailed design of v2 belongs to Media's spec, because Media is the first app that needs it.

### 6.2 A home for this map and the contracts

A new small public repository, `pohtato-potato/suite`, holding no personal data:

- this map;
- every postcard format's fixture file (starting with `postcard-v1.json` from Health and Logbook);
- a short list of which app writes and reads each format.

Each app keeps a copy of the fixtures it uses. Its tests check that copy against the suite's version, so a format can't drift in one app unnoticed. Creating the repository on GitHub needs the owner's go-ahead; until then the folder exists only on the PC.

### 6.3 One backup place

One Google Drive folder and one sign-in pattern for the whole family. Each app writes its own backup file into that folder; no app reads another app's database to back it up.

### 6.4 Storage

All the apps share one web address, so the phone gives them one shared storage allowance. So:

- every app asks the phone to keep its storage permanently (`navigator.storage.persist()`);
- photo-heavy apps (Inventory, Logbook) store photos compressed, with small thumbnails, and say plainly when the phone is nearly full.

## 7. Build order

1. **Media** (next). Thoughts on recently watched things fade the longer they wait; Media is smaller and close to what is already built; and moving films, books and shows out of Logbook is easiest while Logbook is fresh. Media's build also designs shelf v2.
2. **A throwaway test alongside Media:** can background removal for clothing cut-outs run on the S23 in the browser, offline, with nothing uploaded? The answer shapes Inventory's design. The test's code is not kept.
3. **Inventory.** It's a bigger build, and needs an afternoon of photographing belongings.
4. **Places.**
5. **Commonplace**, only if still wanted after a few months of using Media.

## 8. Inventory: a head start for its design round

Everything here is a starting list for Inventory's own design round, not a decision.

- **Scope:** all belongings and a wish-list in one app, with the wardrobe as the most developed part.
- **Every item:** category, brand, model, size; where it's kept (shelf, drawer, box); price, shop and date bought; receipt photo; warranty and return windows; serial number; condition; lent to whom; gift from; sentimental flag; "thinking of letting go"; sold or donated, with the date.
- **Clothes add:** colours (read from the cut-out), fabric, fit notes, care instructions, season, occasion and formality, times worn, last worn, cost per wear, saved outfits, packing lists.
- **Wish-list:** a link, a rough price and a priority, for any kind of thing.
- **Mixing and matching:** cut-out photos of each item, which you tap or scroll through to build an outfit, with the owner's face photo above to judge colour against skin tone. No body simulation.
- **Use:** occasional, not daily. Planning outfits, packing, and finding a piece without emptying the closet.
- **Not included:** washing or laundry status.

## 9. Open questions

- **Commonplace:** confirm it stays parked until Media has been in use for a while (proposed, not yet confirmed).
- **Section 4's table** was proposed and not separately confirmed. Check it before Media's spec relies on it.
- **More flows** (section 5) will be added as each app is designed. Each new flow is added here as well as in the two apps' specs.

## 10. Out of scope

- The design of any single app: each one gets its own brainstorm and spec, starting with Media.
- The code for shelf v2 and the suite repository: these are planned inside Media's build.
