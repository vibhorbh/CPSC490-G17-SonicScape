# Specification — Personalized Map with a Persistent User Profile

> Epic: #23 · Stories: #29, #30 · Task: #42
> Owner: hassanalrubai02 · Sprint: 2 · Status: draft

## Scope

**In scope.** Creating a user account, signing in, selecting starting genres and artists, saving user preferences and swipe history in a local database, and restoring saved information when the user signs in again.

**Out of scope.** Third-party sign-in, cloud synchronization, password recovery, email verification, editing or deleting an account, social features, and sharing profiles between users. These are not required for the initial version of SonicScape.

## Functional requirements

The requirements use EARS-style statements: "when [trigger], the system shall [response]", so each one becomes a test almost verbatim.

| **ID** | **Requirement** | **Story** |
|---|---|---|
| FR-1 | When a new user submits valid registration information, the system shall create a user account. | #29 |
| FR-2 | When a registered user submits valid sign-in credentials, the system shall authenticate the user and load their profile. | #29 |
| FR-3 | When a user submits invalid sign-in credentials, the system shall reject the sign-in attempt without loading a profile, and shall not reveal whether the username or the password was wrong. | #29 |
| FR-4 | When a user signs in for the first time, the system shall allow them to select starting genres and artists. | #29 |
| FR-5 | When a user selects starting genres and artists, the system shall save those selections to that user's account. | #29 |
| FR-6 | When a user has saved starting selections, the system shall use them to initialize that user's personalized music map. | #29 |
| FR-7 | When a signed-in user swipes left or right on a genre, artist, or song, the system shall save the item, the direction, and the time to that user's swipe history. | #30 |
| FR-8 | When a returning user signs in, the system shall restore their saved profile, starting selections, and swipe history. | #30 |
| FR-9 | When a returning user's personalized map is loaded, the system shall build it from their restored selections and swipe history instead of resetting their music selections. | #30 |
| FR-10 | When a new user submits a username that is already registered, the system shall reject the registration. | #29 |

## Non-functional requirements

| **ID** | **Requirement** | **Why it matters here** |
|---|---|---|
| NFR-1 | Account passwords shall be stored as salted password hashes rather than plaintext. | Protects account credentials if the database file is copied or leaked. |
| NFR-2 | User selections and swipe history shall remain available after the application closes and restarts. | Supports persistent personalization. |
| NFR-3 | Data belonging to one user shall not be displayed in, or saved to, another user's account. | Keeps profiles separate. |
| NFR-4 | A user with no saved selections or swipe history shall be able to sign in and open a map without an error. | New accounts may not have any feedback yet. |

## Acceptance criteria (epic level)

- [ ] A new user can create an account and sign in through the application interface, not by calling functions in a console.
- [ ] A first-time user can choose starting genres and artists, and the map they see afterward reflects those choices.
- [ ] After a swipe, the swipe is saved: closing and restarting the application, then signing in again, shows it in that user's history.
- [ ] A returning user signs in and sees the same starting selections and swipe history they had before.
- [ ] With two accounts that have different selections, each account sees only its own selections and swipes.
- [ ] An unknown username and a wrong password produce the same rejection message, and neither signs the user in.
- [ ] Registering a second account with an already registered username is rejected.
- [ ] Inspecting the stored account shows a salted hash and no plaintext password.
- [ ] A brand-new account with no selections and no swipes signs in and opens a map without an error.
- [ ] FR-1 … FR-10 each have a test that fails if the behaviour is removed.
- [ ] `python .github/scripts/check_repo.py` is green and the prototype's tests pass.

## Open questions

| **Question** | **Owner** | **Needed by** |
|---|---|---|
| Which local database technology will the team use? | Team | Before implementation |
| Will users sign in with usernames or email addresses? | Team | Before implementing account creation |
| What are the rules for a valid username and password (length, characters)? | Team | Before implementing account creation |
| How many starting genres and artists must a user pick, and may they skip the step? | Team | Before implementing FR-4 |
| Can users change their initial music preferences after onboarding? | Team | Before implementing preferences |
| Should repeated swipes overwrite earlier feedback or be saved as separate records, and can a swipe be undone (see `specs_goal2.md`)? | Team | Before implementing swipe history |
| How does a user sign out, and does the application remember them between launches? | Team | Before implementing FR-2 |
| Are derived preferences (proposal §3) stored, or recomputed from swipe history at sign-in? | Team | Before implementing FR-9 |
| What does the map show for a user who skipped starting selections and has no swipes? | Team | Before implementing FR-9 |

## Related design documents

- Goal 3 database ER diagram: `docs/design/goal3-database.md` (task #43).
