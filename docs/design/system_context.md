> Epic: #22
> Stories: #27 , #28

# System Context Diagram

```mermaid
graph LR
    User[User]
    SonicScape[SonicScape System]
    Last.fm[Last.fm API]
    Database[(Database)]

    User --> SonicScape
    SonicScape --> Spotify
    SonicScape --> Database
```
