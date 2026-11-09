# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:33:52 2026

@author: expor
"""
from ui.helpers import get_valid_integer
from domain.board_game import BoardGame, VALID_STATUSES

def get_game_data():
    while True:
        name = input("Enter game name: ").strip()
        if name:
            break
        print("Game name cannot be empty.")
    
    while True:
        publisher = input("Enter publisher name: ").strip()
        if publisher:
            break
        print("Publisher name cannot be empty.")
    
    min_players = get_valid_integer("Enter minimum players: ")
    max_players = get_valid_integer("Enter maximum players: ")
    playing_time = get_valid_integer("Enter playing time (minutes): ")
    year = get_valid_integer("Enter publication year: ")
    
    while True:
        print("\nAvailable statuses:")
        for index, s in enumerate(VALID_STATUSES, start=1):
            print(f"[{index}] {s}")
        
        choice = input("Choose a status number (default 1 - Owned): ").strip()
        
        if not choice:
            status = VALID_STATUSES[0]  # "Owned"
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(VALID_STATUSES):
            status = VALID_STATUSES[int(choice) - 1]
            break
        else:
            print("Invalid choice. Please pick a number from the list.")

    return BoardGame(
        name=name,
        publisher=publisher,
        min_players=min_players,
        max_players=max_players,
        playing_time=playing_time,
        year=year,
        status=status
    )