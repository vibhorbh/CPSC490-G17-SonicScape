import os
import sqlite3

# Database file lives next to this module in src/sonicscape/database/.
# Path is relative to prototype/, matching how ScreenViews.py loads its images.
DB_PATH = "src/sonicscape/database/sonicscape.db"

# schema.sql sits in the same folder as this file and defines every table.
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def _connect(db_path=DB_PATH):
    # Opens a connection to the database, creating its folder if needed
    folder = os.path.dirname(db_path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    return sqlite3.connect(db_path)


def init_db(db_path=DB_PATH):
    # Creates the tables defined in schema.sql. Safe to call every time the app starts,
    # as long as schema.sql uses CREATE TABLE IF NOT EXISTS.
    with open(SCHEMA_PATH) as f:
        schema = f.read()

    conn = _connect(db_path)
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()


def create_user(username, password, db_path=DB_PATH):
    # Adds a new user. Returns True if created, False if the username is blank or already taken.
    # NOTE: password is stored as plain text for now; replace with a salted hash before release.
    username = username.strip()
    if not username or not password:
        return False

    conn = _connect(db_path)
    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # UNIQUE constraint failed: username already exists
        return False
    finally:
        conn.close()


def verify_user(username, password, db_path=DB_PATH):
    # Returns True if the username exists and the password matches, otherwise False.
    conn = _connect(db_path)
    try:
        row = conn.execute(
            "SELECT password FROM users WHERE username = ?",
            (username.strip(),),
        ).fetchone()
    finally:
        conn.close()

    return row is not None and row[0] == password


def username_exists(username, db_path=DB_PATH):
    # Returns True if the username is already taken.
    conn = _connect(db_path)
    try:
        row = conn.execute(
            "SELECT 1 FROM users WHERE username = ?",
            (username.strip(),),
        ).fetchone()
    finally:
        conn.close()

    return row is not None
