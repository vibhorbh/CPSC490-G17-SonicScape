# Specification: Swipe Feedback

> Epic: #22 · Stories: 2.1, 2.2
> Owner: Jaspreet Kaur · Sprint: 2 · Status: draft

## Scope

**In scope.** Users swipe right or left to like or dislike any genre, artist,
or song on the map. Each swipe updates the similarity ranking: items similar
to liked ones move up, and disliked items and their close neighbors move down.
The map's highlights change in the same session.

**Out of scope** (candidates for later work, not for this project):

- Inferring taste from skips.
- Star ratings.
- Collaborative filtering.
- LLM-driven recommendations.

## Functional requirements

Written in EARS form: "when [trigger], the system shall [response]", so each
one becomes a test almost verbatim.

| ID | Requirement | Story |
|---|---|---|
| FR-1 | When a user swipes right on a genre, artist, or song, the system shall record a like for that item. | 2.1 |
| FR-2 | When a user swipes left on a genre, artist, or song, the system shall record a dislike for that item. | 2.1 |
| FR-3 | When a swipe is recorded, the system shall show the user a visual confirmation. | 2.1 |
| FR-4 | When a like is recorded, the system shall move items similar to the liked item up the similarity ranking. | 2.2 |
| FR-5 | When a dislike is recorded, the system shall move the disliked item and its close neighbors down the similarity ranking. | 2.2 |
| FR-6 | When the ranking changes, the system shall update the map's highlights in the same session, without the user signing out and back in. | 2.2 |

## Non-functional requirements

| ID | Requirement | Why it matters here |
|---|---|---|
| NFR-1 | The map's highlights update within 1 second of a swipe on the demo dataset. | §3 promises that what the user sees next responds directly to their feedback. |
| NFR-2 | Every ranking change can be traced to the swipe that caused it. | Keeps the similarity approach inspectable, the reason §3 chose it over an LLM. |

## Acceptance criteria (epic level)

- [ ] A user can like and dislike a genre, an artist, and a song through the
      interface, by swiping, not by calling functions in a console.
- [ ] A swipe visibly changes the map's highlights in the same session.
- [ ] FR-1 … FR-6 each have a test that fails if the behaviour is removed.
- [ ] `python .github/scripts/check_repo.py` is green and the prototype's
      tests pass.

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| Does a dislike only lower an item, or hide it entirely? | Team | before FR-5 is implemented |
| How far does a dislike spread: what counts as a "close neighbor"? | Team | before FR-5 is implemented |
| Does a like or dislike on a genre affect the artists and songs inside it? | Team | before FR-4 is implemented |
| Can a user undo a swipe? | Team | before FR-1 is implemented |
