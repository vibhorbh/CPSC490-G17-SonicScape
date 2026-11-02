Epic: #1 Stories: #22
Goal 2 Design

Swipe Sequence Diagram

sequenceDiagram
    actor User
    participant App
    participant FeedbackSystem
    participant RecommendationEngine

    User->>App: Swipe Right
    App->>FeedbackSystem: Record Like
    FeedbackSystem->>RecommendationEngine: Update Ranking
    RecommendationEngine-->>App: Updated Recommendations
    App-->>User: Visual Confirmation
