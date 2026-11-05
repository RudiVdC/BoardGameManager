# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:04:12 2026

@author: expor
"""

import sqlite3
import json
import os

def get_config():
    """Leest de database locatie uit config.json vanuit de hoofdmap van het project."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "..", "config.json")
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.json not found at path: {config_path}! Please copy config.example.json to config.json.")
    
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_connection():
    """Maakt een verbinding met de SQLite database op basis van de config."""
    config = get_config()
    db_path = config.get("database_path", "data/boardgames.db")
    
    # Zorg ervoor dat de 'data' map bestaat als deze in het pad staat
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)
        
    conn = sqlite3.connect(db_path)
    return conn

def init_database():
    """Maakt de tabellen 'publishers' en 'board_games' aan als ze nog niet bestaan."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabel 1: Publishers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)
    
    # Tabel 2: Board Games
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