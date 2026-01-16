import sqlite3

DB_NAME = "chatData.db"


def get_connection():
    """Erstellt und gibt eine Datenbankverbindung zurück"""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Erstellt die Benutzertabelle"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS benutzer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            alter INTEGER NOT NULL
        )
        """)


def add_user(name: str, alter: int):
    """Fügt einen Benutzer hinzu"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO benutzer (name, alter) VALUES (?, ?)",
            (name, alter)
        )


def get_all_users():
    """Gibt alle Benutzer zurück"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM benutzer")
        return cursor.fetchall()


def get_user_by_name(name: str):
    """Sucht einen Benutzer nach Namen"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM benutzer WHERE name = ?",
            (name,)
        )
        return cursor.fetchone()


def update_user_age(name: str, new_age: int):
    """Aktualisiert das Alter eines Benutzers"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE benutzer SET alter = ? WHERE name = ?",
            (new_age, name)
        )


def delete_user(name: str):
    """Löscht einen Benutzer"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM benutzer WHERE name = ?",
            (name,)
        )


if __name__ == "__main__":
    create_table()

    add_user("Max", 30)
    add_user("Anna", 25)

    print("Alle Benutzer:")
    print(get_all_users())

    print("Benutzer Anna:")
    print(get_user_by_name("Anna"))

    update_user_age("Anna", 26)

    delete_user("Max")

    print("Nach Änderungen:")
    print(get_all_users())
