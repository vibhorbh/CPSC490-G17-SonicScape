-- SonicScape database schema
-- Run by init_db() in database.py every time the app starts.
-- Every table uses IF NOT EXISTS so running it again is harmless.

-- User accounts (Goal 3, Story #29)
-- NOTE: password is stored as plain text for now.
CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    username   TEXT    NOT NULL UNIQUE,
    password   TEXT    NOT NULL,
    created_at TEXT    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

