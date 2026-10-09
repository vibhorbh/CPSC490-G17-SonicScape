# Project Proposal — Echo Sphere

**Department of Computer Science**
**CPSC 490 Undergraduate Seminar in Computer Science — Proposal for Capstone Project**

**Group 17 — SonicScape ** · Sponsor: independent
Authors: 〈Bhargava, Vibhor, vibhorbh〉,〈…Deboer Bradley, braddeboer> 〉,〈…Kaur Jaspreet, jaspreek9k〉〈…Alrubai Hassan, 〉
Date: 〈YYYY-MM-DD〉

## 0. Abstract
Our goal as a team was to make a music app but after doing a little bit of market research, we found that most music apps have the same features i.e., liking songs, adding songs to playlists, searching up features and paying a premium to get no ads, the UI is plain and old and even regular app updates don't bring much changes so we felt the need to make the user experience more interesting by using planets and subsystems as our base idea. In our project, we want to build a new style of music app where the users will be able to listen to music in a new way that hasn't been explored much, as planets and star systems, you will be able to click into planets and star systems to switch genres and play around with playlists and songs instead of using those same old boring flat interfaces every other music app gives you. We want to give users the feeling that using the "premium" music apps shouldn't be industry standard that everyone has to use, we want music apps to become more experimental and playful even. 

For SonicScape, we want the app to feel more like exploring than just scrolling through another music platform. Instead of only giving users playlists or random recommendations, the app will let them move through different planets and star systems that represent genres, artists, and songs. As users like, dislike, or skip music, the app can slowly learn what they enjoy and use that to improve future recommendations. The main goal is to make discovering music feel more fun, personal, and interactive, while still keeping the basic features people expect from a music app.

## 1. Introduction
Our Team has decided to build Project SonicScape, we intend for this program to pull and parse information from Nasa's official website utilizing the free API keys that Nasa has to offer as well as potentially utilizing databases of music to organize a users preference on our own backend rather than relying fully on an llm. Once we are able to build the API parser and pull information we plan to utilize mapping of solar systems to create a music app that allows the user to traverse galaxies/star systems which will be interpreted as different music genres and artists. As the user begins traversing they will be able to swipe right or left on the given artist/genre to confirm or deny their fondness of the music. The current plan is to have Galaxies represent music Genres, Star Systems represent Artists, and individual planets representing songs from the Artists. We plan to incorporate some level of AI to begin creating a custom profile of the individual users music taste to help them find new music similar to what they already like. Our Project hopes to solve the problem of large corporations inbuilt AI models such as "DJ X" from Spotify. As a user of both Spotify and its DJ X for years now our team can personally attest to the lack luster nature of this AI DJ, often when you select the DJ they play music that you already are listening to, claim to get ready to play music that will quote "pump you up" just to play soft indie music, and just generally suggest poor music related to what you actually listen to.


| Existing approach | What it does | Pros | Cons | Why ours differs |
|---|---|---|---|---|
| 〈Spotify〉 | 〈recommends music based on what users listen to〉 | 〈easy to use, good playlist, personalized suggestions〉 | 〈Music discovery is mostly through playlist and search〉 | 〈Ecosphere makes discovering music more interactive by letting users explore the space theme world rather then boring screens〉 |
| 〈Apple Music〉 | 〈Suggests songs, artists, playlists based on your preferences〉 | 〈Good recommendation and large music library〉 | 〈Using a traditional browsing experience〉 | 〈It focuses on exploration and visual interaction instead of standard menus〉 |
| 〈YouTube Music〉 | 〈Recommends music using listening and viewing history〉 | 〈Large variety of music and personalized suggestions〉 | 〈Recommendations can become repetitiv〉 | 〈It encourages users to actively discover new music through exploration〉 |

〈Discuss the table in prose — the table is evidence, the paragraph is the
argument. "Nothing like this exists" is almost never true and reads as a
missing survey; if a close competitor exists, say so and explain why you are
still building this.〉

### 1.2 Problem Statements

| Problem | Addressed by |
|---|---|
| P1 〈Music discovery can feel repetitive and non-engaging in traditional music apps〉 | 〈Goal 1 (#n)〉 |
| P2 〈Users may have difficulty finding new artists, songs, genres that match their interests〉 | 〈Goal 2 (#n)〉 |
| P3 〈Existing music apps provide limited interactive exploration features〉 | 〈Goal 3 (#n)〉 |

## 2. Goals and Objectives

> Describe goals and objectives. Goals are general statements of what you are
> trying to accomplish with the project or problems to solve. Objectives are
> specific, measurable statements of what you want to complete to reach the
> project goals. Most projects have 2-3 goals.
>
> List the objectives for each goal. To write objectives, look at the goal
> statement and list what you need to complete using action words like use
> case names in order to meet the goal.
>
> Note that the goals and objectives in a proposal will be an important
> metric to evaluate whether or not you successfully finished your project
> when you turn in your final project report.

Each **goal** is tracked as an **Epic** issue and each **objective** as a
**User Story** issue in the team repository (see the setup guide's *Epics and user stories* section).
**Every epic and user story in the repository is linked from this section** —
CI gate G8 fails if one exists that this section does not link. That is what
keeps the goals in this document and the work on the board from drifting
apart.

Write each objective the way the guidance above asks — **an action word plus
the measure that says it is done**, not a role-play sentence:

- **Goal 1: 〈e.g. Secure account management〉** (Epic #〈n〉)
  - Objective 1.1: 〈Implement member registration and login with hashed
    credentials, session expiry, and rejection of malformed input.〉 (#〈n〉)
  - Objective 1.2: 〈Demonstrate the login round-trip in a runnable prototype
    at the Week-8 in-class check.〉 (#〈n〉)
- **Goal 2: 〈your second goal〉** (Epic #〈n〉)
  - Objective 2.1: 〈Action word + what you will complete + how it will be
    measured〉 (#〈n〉)

〈Replace the brackets with your own 2–3 goals and their objectives, and put
the **real issue numbers** in as you file them — gate G8 checks that every
epic and story in your repository is linked from this section. A fully worked
version of this, with live issues and a populated board, is in the course
example repository.〉

## 3. Proposed Approaches

> Describe your proposed approach to solve the problem, specifying how you
> will achieve the stated goals. List some possible strategies.

〈Your approach — **clear and concise**. State the strategy you chose, the
alternatives you considered, and the reasoning that decided between them.
Think of this as the argument, not the manual: a reader should finish this
section understanding *what* you will do and *why that* rather than the
alternatives.〉

**Keep the details out of this section.** Tooling, platforms, frameworks,
DBMS choices, environment setup, diagrams, and the work breakdown all belong
in §4 (Required Environment, Resources, and Planned Activities). If a
sentence here names a version number, a library, or a configuration, it
probably belongs in §4 — leave a pointer instead ("the implementation stack
is detailed in §4").

〈A few paragraphs, or a short list of candidate strategies with one line of
trade-off each. If it runs past a page, you are writing §4.〉

## 4. Required Environment, Resources, and Planned Activities

> Review the required and available resources and environment to complete
> your project. For example, server, platform, software tools, operating
> systems, DBMS, or any required skills.
>
> Describe the expected activities to achieve the stated goals, e.g.,
> software development process.

〈Your environment, resources, and planned activities.〉

**Diagrams belong in this section.** Include at minimum a high-level
architecture diagram and a system (context) diagram; add the ER/EER model and
a data-flow diagram where they help the reader understand what you are
building and what it depends on. Draw them with any graphical tool
(Lucidchart, draw.io, Miro, Mermaid, ERDPlus, Figma), keep the authoritative
copies in `docs/design/` with both editable source and exported image, and
reference them here.

〈Number every figure, caption it, and point at it from the prose — "Figure 1
shows the three deployment tiers and the trust boundary between them." A
figure the text never mentions is decoration. See `docs/design/DIAGRAMS.md`
for tools, conventions, and the rule that every box and arrow must be
verified against reality.〉

### Specification and design documents

**Every specification and design document the team writes is listed here**
with the objective it serves. This section is the index of the project's
technical detail: §3 holds the argument, §4 holds the documents that make it
buildable. CI gate G9 fails if a document exists in `docs/specs/` or
`docs/design/` that this section does not link.

| Document | Kind | Covers | Issues |
|---|---|---|---|
| 〈docs/specs/account-management.md〉 | specification | 〈account management requirements〉 | 〈#n, #n〉 |
| 〈docs/design/architecture.md〉 | design | 〈system architecture + data model〉 | 〈#n〉 |

〈The scaffold ships `docs/specs/example-spec.md` and
`docs/design/example-design.md` as worked examples — read them, then delete
them once you have your own, and list yours here.〉

〈Replace these rows with your own. Each document names its epic and stories
in its own first lines too (gate G2), so the trail runs both ways.〉

### Planned activities — the work items

The goals and objectives live in §2 as epics and user stories. **This section
links every *other* work item: features, enhancements, bugs, tasks, and
sub-tasks** — the concrete activities that deliver those objectives. CI gate
G8 fails if such an issue exists that this section does not link.

| Issue | Type | Activity | Parent | Owner | Sprint |
|---|---|---|---|---|---|
| 〈#n〉 | 〈task〉 | 〈stand up the prototype login endpoint〉 | 〈#story〉 | 〈owner〉 | 〈Sprint 1〉 |
| 〈#n〉 | 〈feature/enhancement/bug/task/sub-task〉 | 〈…〉 | 〈#story〉 | 〈…〉 | 〈…〉 |

〈Replace these rows with your own, and keep the table current as you file new
issues — with §2 it gives a reader every planned activity in one place, each
traceable to the objective it serves.〉

## 5. Project Outcomes

> Describe the outcomes or deliverables, e.g., final project report, user
> manuals, source code, data or database files, etc.
>
> Note: the deliverables always include the team GitHub repository, which
> must already contain prototype v0 (a thin end-to-end proof-of-concept,
> however small, running when this proposal is submitted). Briefly describe
> what your v0 demonstrates and how to run it.

〈**One or two paragraphs** explaining the project outcome overall — what will
exist when the project is finished, and what it will let someone do. Keep it
prose, not a checklist; name the deliverables inside the paragraphs, and say
briefly what prototype v0 demonstrates today and how to run it.〉

## 6. Project Timeline

> Identifies tasks (project objectives) to be performed, milestones to be
> met, and the estimated number of hours for each task.

〈**This is the plan for CPSC 491 next semester — the implementation timeline,
not this semester's proposal work.** Identify the tasks (your objectives from
§2), the milestones, and the estimated hours for each, in the order they will
be built. State the assumptions it rests on (sponsor availability, data
access, hardware).〉

| Task (objective) | Milestone | Owner | Est. hours | Spring phase |
|---|---|---|---|---|
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |
| 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 | 〈…〉 |

〈Do **not** put this fall's four proposal sprints here — those live on the
project board and in `docs/sprint-reviews/`. This section answers "how does
the system actually get built next semester?"〉

## 7. AI Usage

> Per the course AI policy (see the syllabus, Use of AI Tools), disclose the
> AI tools used in preparing this proposal and the prototype: which tools,
> for what tasks (e.g., code generation, test writing, debugging,
> diagramming), and approximately what fraction of each artifact was
> AI-assisted.
>
> Reminder: the prose of this proposal must be your own writing. You remain
> fully responsible for the correctness of all AI-assisted work, including
> the prototype code.

〈Your disclosure. Naming the tool is not disclosure — name what it drafted,
what fraction of each artifact was AI-assisted, and how you verified it.〉

## 8. References

> [1] Burges, C. J. C. Tutorial on Support Vector Machines for Pattern
> Recognition. Kluwer Academic Publishers, 1998.
> [2] Chen, P., Fan, R., and Lin, C. A study on SMO-type decomposition
> methods for support vector machines. IEEE Transactions on Neural Networks,
> 2006.
> [3] For Wikipedia, specify the URL here
> [4] For a web source, specify the URL here plus date accessed

〈Number references in the order first cited and cite them in the text as
[1], [2]. Every entry must be a source a team member has actually read and
can produce on request.〉
