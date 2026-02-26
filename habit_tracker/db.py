import sqlite3

def connect(db_path: str = "database.db") -> sqlite3.Connection:
    return sqlite3.connect(db_path)

def initialize_schema(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    con.commit()

def add_habit(con: sqlite3.Connection, habit_name: str) -> None:
    cur = con.cursor()
    cur.execute("INSERT INTO habits (habit) VALUES (?)", (habit_name,)) #Question mark - 
    con.commit()

