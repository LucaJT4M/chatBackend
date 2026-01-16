import sqlite3
from Classes.user import User
import datetime

DB_NAME = "chatData.db"

def get_connection():
    """Erstellt und gibt eine Datenbankverbindung zurück"""
    return sqlite3.connect(DB_NAME)

def create_user(username: str, password: str) -> User:
    created_at = datetime.datetime.utcnow().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, created_at)
        )
        user_id = cursor.lastrowid

    newUser = User()
    newUser.id = user_id
    newUser.username = username
    newUser.password = password
    newUser.created_at = created_at

    return newUser

def get_users() -> list[User]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users"
        )
        rows = cursor.fetchall()

    return [User(*row) for row in rows]

def delete_user(user_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        return cursor.rowcount > 0  # True, wenn mindestens 1 Zeile gelöscht wurde
    
newUser = User()
newUser.username = "testUser"
newUser.password = "testPassword"

create_user(newUser.username, newUser.password)