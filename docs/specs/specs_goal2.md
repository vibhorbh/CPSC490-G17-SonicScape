## Functional requirements

Written in EARS form — "when 〈trigger〉, the system shall 〈response〉" — so each
one becomes a test almost verbatim.

| ID | Requirement | Story |
|---|---|---|
| FR-1 | When a user swipes right on a genre, artist, or song, the system shall record a like for that item. | 〈#n〉 2.1 |
| FR-2 | When a user swipes left on a genre, artist, or song, the system shall record a dislike for that item. | 〈#n〉 2.1 |
| FR-3 | When a swipe is recorded, the system shall show the user a visual confirmation. | 〈#n〉 2.1 |
| FR-4 | When a like is recorded, the system shall move items similar to the liked item up the similarity ranking. | 〈#n〉 2.2 |
| FR-5 | When a dislike is recorded, the system shall move the disliked item and its close neighbors down the similarity ranking. | 〈#n〉 2.2 |
| FR-6 | When the ranking changes, the system shall update the map's highlights in the same session, without the user signing out and back in. | 〈#n〉 2.2 |

## Non-functional requirements

| ID | Requirement | Why it matters here |
|---|---|---|
| NFR-1 | The map's highlights update within 1 second of a swipe on the demo dataset. | §3 promises that what the user sees next responds directly to their feedback. |
| NFR-2 | Every ranking change can be traced to the swipe that caused it. | Keeps the similarity approach inspectable, the reason §3 chose it over an LLM. |

## Acceptance criteria (epic level)

- [ ] A user can like and dislike a genre, an artist, and a song through the
      interface — by swiping, not by calling functions in a console.
- [ ] A swipe visibly changes the map's highlights in the same session.
- [ ] FR-1 … FR-6 each have a test that fails if the behaviour is removed.
- [ ] `python .github/scripts/check_repo.py` is green and the prototype's
      tests pass.
