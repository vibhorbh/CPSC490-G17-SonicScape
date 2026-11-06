> Epic: #22
> Stories: #27 , #28

# Goal 2 Design

## Swipe Sequence Diagram

Figure 1 shows what happens when a user swipes on a genre, artist, or song.
The app sends the swipe to the feedback system, which records it. The app shows
the user a confirmation right away, and the recommendation engine then updates
the ranking and the map's highlights.

```mermaid
sequenceDiagram
    actor User
    participant App
    participant FeedbackSystem
    participant RecommendationEngine

    User->>App: Swipe on a genre, artist, or song
    App->>FeedbackSystem: Send swipe (right or left)
    alt Swipe right (like)
        FeedbackSystem->>RecommendationEngine: Like recorded, move similar items up
    else Swipe left (dislike)
        FeedbackSystem->>RecommendationEngine: Dislike recorded, move item and close neighbors down
    end
    FeedbackSystem-->>App: Swipe recorded
    App-->>User: Visual confirmation
    RecommendationEngine-->>App: Updated ranking
    App-->>User: Updated map highlights
```

*Figure 1: Swipe sequence for Goal 2. It answers one question: what happens,
in order, between a user's swipe and the map updating?*
