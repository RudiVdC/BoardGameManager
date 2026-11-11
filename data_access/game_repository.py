# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:36:25 2026

@author: expor
"""

from data_access.database import get_connection
from domain.publisher import Publisher
from domain.board_game import BoardGame

class GameRepository:
    
    @staticmethod
    def add_publisher(publisher):
        """Adds a new publisher to the database if it doesn't exist yet."""
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if publisher already exists
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (publisher.name,))
        row = cursor.fetchone()
        
        if row:
            publisher.id = row[0]
        else:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (publisher.name,))
            conn.commit()
            publisher.id = cursor.lastrowid
            
        conn.close()
        return publisher.id

    @staticmethod
    def add_board_game(game):
        """Saves a board game object to the database."""
        # First, ensure the publisher exists in the database and get its ID
        publisher_id = GameRepository.add_publisher(Publisher(game.publisher))
        
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO board_games (name, publisher_id, min_players, max_players, playing_time, year, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            game.name,
            publisher_id,
            game.min_players,
            game.max_players,
            game.playing_time,
            game.year,
            game.status
        ))
        
        conn.commit()
        game.id = cursor.lastrowid
        conn.close()
        print(f"Board game '{game.name}' successfully added to the database!")

    @staticmethod
    def get_all_games():
        """Retrieves all board games from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT bg.id, bg.name, p.name, bg.min_players, bg.max_players, bg.playing_time, bg.year, bg.status
            from board_games bg
            JOIN publishers p ON bg.publisher_id = p.id
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        games = []
        for row in rows:
            game = BoardGame(
                game_id=row[0],
                name=row[1],
                publisher=row[2],
                min_players=row[3],
                max_players=row[4],
                playing_time=row[5],
                year=row[6],
                status=row[7]
            )
            games.append(game)
            
        return games
    
    @staticmethod
    def search_games(query):
        """Searches for board games by name (case-insensitive)."""
        conn = get_connection()
        cursor = conn.cursor()
        
        # Use LIKE with wildcards (%) to find partial matches on game name
        cursor.execute("""
            SELECT bg.id, bg.name, p.name, bg.min_players, bg.max_players, bg.playing_time, bg.year, bg.status
            FROM board_games bg
            JOIN publishers p ON bg.publisher_id = p.id
            WHERE bg.name LIKE ?
        """, (f"%{query}%",))
        
        rows = cursor.fetchall()
        conn.close()
        
        games = []
        for row in rows:
            game = BoardGame(
                game_id=row[0],
                name=row[1],
                publisher=row[2],
                min_players=row[3],
                max_players=row[4],
                playing_time=row[5],
                year=row[6],
                status=row[7]
            )
            games.append(game)
            
        return games
    
    @staticmethod
    def delete_game(game_id):
        """Verwijdert een bordspel uit de database op basis van ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM board_games WHERE id = ?", (game_id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def update_game(game):
        """Updates an existing board game in the database."""
        publisher_id = GameRepository.add_publisher(Publisher(game.publisher))
        
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE board_games 
            SET name = ?, publisher_id = ?, min_players = ?, max_players = ?, playing_time = ?, year = ?, status = ?
            WHERE id = ?
        """, (
            game.name,
            publisher_id,
            game.min_players,
            game.max_players,
            game.playing_time,
            game.year,
            game.status,
            game.id
        ))
        if cursor.rowcount > 0:
            print(f"Board game '{game.name}' successfully updated in the database!")
        else:
            print("No board game was updated.")
        conn.commit()
        conn.close()