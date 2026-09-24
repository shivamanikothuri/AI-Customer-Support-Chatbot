import sqlite3
from datetime import datetime

DATABASE_NAME = "chatbot.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_chat(user_message, bot_response):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO chat_logs
        (user_message, bot_response, timestamp)
        VALUES (?, ?, ?)
    """, (
        user_message,
        bot_response,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_chat_logs():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_message, bot_response, timestamp
        FROM chat_logs
        ORDER BY id DESC
    """)

    logs = cursor.fetchall()

    connection.close()

    return logs