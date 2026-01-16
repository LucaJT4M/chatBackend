import sqlite3
from Classes.user import User
import datetime

DB_NAME = "chatData.db"

def get_connection():
    """Erstellt und gibt eine Datenbankverbindung zurück"""
    return sqlite3.connect(DB_NAME)

def create_user(username: str, password: str) -> User:
    created_at = datetime.utcnow().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, created_at)
        )
        user_id = cursor.lastrowid

    return User(user_id, username, password, created_at)

def get_users():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users"
        )