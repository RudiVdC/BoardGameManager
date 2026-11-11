# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:04:12 2026

@author: expor
"""

import sqlite3
import json
import os


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_config():
    """Leest de database locatie uit config.json."""

    config_path = os.path.join(PROJECT_DIR, "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"config.json not found at path: {config_path}! "
            "Please copy config.example.json to config.json."
        )

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    if not config.get("database_path"):
        raise ValueError("The database_path setting is missing in config.json.")

    return config


def get_connection():
    """Maakt een verbinding met de SQLite database op basis van de config."""

    config = get_config()
    db_path = config["database_path"]

    if not os.path.isabs(db_path):
        db_path = os.path.join(PROJECT_DIR, db_path)

    db_dir = os.path.dirname(db_path)

    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

    conn = sqlite3.connect(db_path)

    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def init_database():
    """Maakt de tabellen publishers en board_games aan als ze nog niet bestaan."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS board_games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            publisher_id INTEGER,
            min_players INTEGER,
            max_players INTEGER,
            playing_time INTEGER,
            year INTEGER,
            status TEXT,
            FOREIGN KEY (publisher_id) REFERENCES publishers (id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database successfully initialized with 2 tables!")


if __name__ == "__main__":
    init_database()
