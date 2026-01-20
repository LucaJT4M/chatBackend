import sqlite3
from datetime import datetime
from Classes.class_importer import *

DB_NAME = "chatData.db"

def __get_connection():
    """Erstellt und gibt eine Datenbankverbindung zurück"""
    return sqlite3.connect(DB_NAME)

def __get_datetime() -> str:
    return datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

# User Operations
def create_user(username: str, password: str) -> User:
    created_at = __get_datetime()

    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, created_at)
        )
        user_id = cursor.lastrowid

    new_user = User(user_id, username, password, created_at)

    return new_user

def get_users() -> list[User]:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM users"
        )
        rows = cursor.fetchall()

    return [User(*row) for row in rows]

def get_user_by_name(username: str) -> User:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT users.id, users.username, users.password, users.created_at FROM users WHERE users.username = ?",
            (username,)
        )
        row = cursor.fetchone()

    return User(*row) if row else None

def delete_user(user_id: int) -> bool:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

        print("Deleted User")
        return cursor.rowcount > 0  # True, wenn mindestens 1 Zeile gelöscht wurde

# Chat Operations
def create_chat(user1_id: int, user2_id: int) -> Chat:
    created_at = __get_datetime()

    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chats (user1, user2, created_at) VALUES (?, ?, ?)",
            (user1_id, user2_id, created_at)
        )
        chat_id = cursor.lastrowid

    new_chat = Chat(chat_id, user1_id, user2_id, created_at)

    print("Chat created")
    return new_chat

def get_chats() -> list[Chat]:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM chats"
        )
        rows = cursor.fetchall()

    return [Chat(*row) for row in rows]

def delete_chat(chat_id: int) -> bool:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM chats WHERE id = ?",
            (chat_id,)
        )
        print("Deleted chat")

        return cursor.rowcount > 0  # True, wenn mindestens 1 Zeile gelöscht wurde

def find_chat(user1_id: int, user2_id: int) -> Chat:
    with __get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT chats.id, chats.user1, chats.user2, chats.created_at FROM chats WHERE chats.user1 = ? AND chats.user2 = ? OR chats.user1 = ? AND chats.user2 = ?",
                (user1_id, user2_id, user2_id, user1_id,)
            )
            row = cursor.fetchone()

    return Chat(*row) if row else None

# Message Operations
def create_message(chat_id: int, sender_id: int, content: int) -> Message:
    created_at = __get_datetime()

    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (chat_id, sender_id, content, created_at) VALUES (?, ?, ?, ?)",
            (chat_id, sender_id, content, created_at)
        )
        message_id = cursor.lastrowid

    new_message = Message(message_id, chat_id, sender_id, content, created_at)

    print("Message created")
    return new_message
    
def get_messages() -> list[Message]:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM messages"
        )
        rows = cursor.fetchall()

    return [Message(*row) for row in rows]

def delete_message(message_id: int):
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM messages WHERE id = ?",
            (message_id,)
        )
    
        print("Deleted Message")
        return cursor.rowcount > 0  # True, wenn mindestens 1 Zeile gelöscht wurde

def get_messages_from_chat(chat_id: int) -> list[Message]:
    with __get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM messages WHERE messages.chat_id = ?",
            (chat_id,)
        )
        rows = cursor.fetchall()

    return [Message(*row) for row in rows]


def __wipe_db():
    users = get_users()
    chats = get_chats()
    messages = get_messages()

    for u in users:
        delete_user(u.id)

    for c in chats:
        delete_chat(c.id)

    for m in messages:
        delete_message(m.id)

def __init_test():
    user_len = len(get_users())

    if user_len < 2:
        for i in range(user_len, 2):
            test_username = f"TestUser{i}"
            test_password = f"testPassword{i}"
            create_user(username=test_username, password=test_password)

    users = get_users()
    chat = Chat(0, 0, 0, "")

    if len(get_chats()) < 1:
        chat = create_chat(users[0].id, users[1].id)

    if (len(get_messages())) < 2:
        for i in range(0, 4):
            create_message(chat.id, users[0].id, f"Test Msg {i}")