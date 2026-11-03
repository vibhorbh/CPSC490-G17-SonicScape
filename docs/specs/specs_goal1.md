# Specification — Navigation and Discovery

> Epic: #21 · Stories: #25 (1.1), #26 (1.2)
> Owner: 〈name〉 · Sprint: 2 · Status: draft

## Scope

**In scope.** A three-level music map in which galaxies are genres, star
systems are artists, and planets are songs. Each user's map is generated from
a stored dataset and that user's own data. Selecting a planet opens the song
on an external listening service. The map highlights unvisited artists similar
to ones the user has liked.

**Out of scope** (candidates for later work, not for this project):

- In-app audio playback. This is a stretch goal, pursued only if a suitable
  preview source is available.
- LLM-driven recommendations.
- A free-form map layout without the genre → artist → song hierarchy.
- Playlists, sharing, and other social features.

## Functional requirements

Written in EARS form — "when 〈trigger〉, the system shall 〈response〉" — so each
one becomes a test almost verbatim.

| ID | Requirement | Story |
|---|---|---|
| FR-1 | When a signed-in user opens the map, the system shall generate it from the stored dataset and that user's data rather than from a hardcoded base map. | #25 1.1 |
| FR-2 | When the map opens, the system shall display galaxies, each labeled with a genre. | #25 1.1 |
| FR-3 | When a user selects a galaxy, the system shall display that genre's star systems, each labeled with an artist. | #25 1.1 |
| FR-4 | When a user selects a star system, the system shall display that artist's planets, each labeled with a song. | #25 1.1 |
| FR-5 | When a user selects a planet, the system shall open that song on the external listening service. | #25 1.1 |
| FR-6 | When a user selects "back", the system shall return to the previous level of the map. | #25 1.1 |
| FR-7 | When the map is displayed, the system shall highlight star systems that are similar to artists the user has liked and that the user has not yet liked or visited. | #26 1.2 |

## Non-functional requirements

| ID | Requirement | Why it matters here |
|---|---|---|
| NFR-1 | Moving between map levels takes under 1 second on the demo dataset. | Navigation that lags breaks the sense of exploring. |
| NFR-2 | A user can go from a genre to opening a song in 3 selections or fewer. | Keeps the hierarchy a clear path rather than a maze (§3). |
| NFR-3 | For every highlighted star system, the system can show which liked artist it is similar to. | §3 chose a similarity approach because it can be inspected; this makes that checkable. |
| NFR-4 | Map navigation reads only from the stored local dataset and makes no live calls to external music services. | Keeps the demo reliable and avoids depending on third-party uptime and rate limits. |

## Acceptance criteria (epic level)

- [ ] A signed-in user can navigate from a galaxy to a star system to a planet
      and open the song through the interface — by clicking, not by calling
      functions in a console.
- [ ] Highlighted star systems appear on the map, and each one can be traced
      to a liked artist.
- [ ] FR-1 … FR-7 each have a test that fails if the behaviour is removed.
- [ ] In usability testing, at least 4 of 5 testers find and open a requested
      song without help.
- [ ] In testing, users swipe right on highlighted artists more often than on
      randomly chosen ones.
- [ ] `python .github/scripts/check_repo.py` is green and the prototype's
      tests pass.

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| Which external listening service does selecting a planet open, and does every track in the dataset have a link to it? | 〈name〉 | before FR-5 is implemented |
| Where does the stored music dataset come from, how large is it (genres, artists, songs), and what source supplies artist similarity? | 〈name〉 | Sprint 〈n〉 planning |
| What counts as "visited": opening a star system, or opening one of its songs? | 〈name〉 | before FR-7 is implemented |
| How many star systems are highlighted at once? | 〈name〉 | before FR-7 is implemented |
| Which astronomical data source supplies star and planet names, and is it fetched once or at runtime? | 〈name〉 | before FR-1 is implemented |
| If the in-app playback stretch goal is pursued, which preview source is used, and are its terms acceptable? | 〈name〉 | only if the stretch goal starts |