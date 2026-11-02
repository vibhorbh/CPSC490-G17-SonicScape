
# Specification — Personalized Map with a Persistent User Profile

> Epic: #23 · Stories: #29, #30 · Owner: hassanalrubai02 · Sprint: 2 · Status: draft

## Scope

**In scope.** Creating a user account, signing in, selecting starting genres and artists, saving user preferences and swipe history in a local database, and restoring saved information when the user signs in again.

**Out of scope.** Third-party sign-in, cloud synchronization, password recovery, social features, and sharing profiles between users. These are not required for the initial version of SonicScape.

## Functional requirements

The requirements use EARS-style statements so that each one describes a trigger and an expected system response.

| **ID** | **Requirement** | **Story** |
|---|---|---|
| FR-1 | When a new user submits valid registration information, the system shall create a user account. | #29 |
| FR-2 | When a registered user submits valid sign-in credentials, the system shall authenticate the user and load their profile. | #29 |
| FR-3 | When a user submits invalid sign-in credentials, the system shall reject the sign-in attempt without loading a profile. | #29 |
| FR-4 | When a user signs in for the first time, the system shall allow them to select starting genres and artists. | #29 |
| FR-5 | When a user selects starting genres and artists, the system shall save those selections and use them to initialize the personalized music map. | #29 |
| FR-6 | When a signed-in user swipes left or right on a genre, artist, or song, the system shall save the feedback to that user's swipe history. | #30 |
| FR-7 | When a user's profile or preferences change, the system shall save the updated information to the local database. | #30 |
| FR-8 | When a returning user signs in, the system shall restore their saved profile, preferences, and swipe history. | #30 |
| FR-9 | When the user's personalized map is loaded, the system shall use their restored preferences and feedback instead of resetting their music selections. | #30 |

## Non-functional requirements

| **ID** | **Requirement** | **Why it matters here** |
|---|---|---|
| NFR-1 | Account passwords shall be stored as salted password hashes rather than plaintext. | Protects account credentials. |
| NFR-2 | User preferences and swipe history shall remain available after the application closes and restarts. | Supports persistent personalization. |
| NFR-3 | Data belonging to one user shall not be displayed in another user's account. | Keeps profiles separate. |
| NFR-4 | The system shall handle an account with no saved preferences or swipe history without crashing. | New accounts may not have any feedback yet. |

## Acceptance criteria (epic level)

- [ ] A new user can create an account and sign in through the application interface.
- [ ] A first-time user can choose starting genres and artists that seed their music map.
- [ ] The application saves preferences and swipe history to the local database.
- [ ] A returning user can sign in and see their previously saved preferences.
- [ ] Saved information remains available after the application restarts.
- [ ] Two different accounts maintain separate preferences and swipe histories.
- [ ] Invalid sign-in credentials do not grant access to another user's profile.
- [ ] Each functional requirement can be checked through a test or demonstration.

## Open questions

| **Question** | **Owner** | **Needed by** |
|---|---|---|
| Which local database technology will the team use? | Team | Before implementation |
| Will users sign in with usernames or email addresses? | Team | Before implementing account creation |
| Can users change their initial music preferences after onboarding? | Team | Before implementing preferences |
| Should repeated swipes overwrite earlier feedback or be saved as separate records? | Team | Before implementing swipe history |

## Related design documents

- Goal 3 database ER diagram — planned for Sprint 2; file will be added at `docs/design/goal3-database.md`.
- Epic: #23
- Stories: #29 and #30
