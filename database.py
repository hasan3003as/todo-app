import sqlite3
from datetime import datetime


def get_connection():
    """Connect to the SQLite database (creates the file if it doesn't exist)."""
    conn = sqlite3.connect("todos.db")
    conn.row_factory = sqlite3.Row  # So we can access columns by name
    return conn


def create_table():
    """Create the tasks table if it doesn't already exist."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def get_all_tasks():
    """Retrieve every task from the database."""
    conn = get_connection()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(task) for task in tasks]


def add_task(title):
    """Insert a new task."""
    conn = get_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()


def toggle_task(task_id):
    """Flip a task between complete and incomplete."""
    conn = get_connection()
    conn.execute(
        "UPDATE tasks SET completed = NOT completed WHERE id = ?", (task_id,)
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    """Remove a task permanently."""
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()