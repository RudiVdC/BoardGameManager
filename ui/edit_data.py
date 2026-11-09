# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:28:04 2026

@author: expor
"""

from ui.helpers import get_valid_integer
from domain.board_game import VALID_STATUSES

def edit_data(choice, game):
    if choice == 1:
        new_name = input(f"Enter new name (current: {game.name}): ").strip()
        if new_name:
            game.name = new_name
            
    elif choice == 2:
        new_pub = input(f"Enter new publisher (current: {game.publisher}): ").strip()
        if new_pub:
            game.publisher = new_pub
            
    elif choice == 3:
        game.min_players = get_valid_integer(f"Enter new min players (current: {game.min_players}): ")
        
    elif choice == 4:
        game.max_players = get_valid_integer(f"Enter new max players (current: {game.max_players}): ")
        
    elif choice == 5:
        game.playing_time = get_valid_integer(f"Enter new playing time in minutes (current: {game.playing_time}): ")
        
    elif choice == 6:
        game.year = get_valid_integer(f"Enter new publication year (current: {game.year}): ")
        
    elif choice == 7:
        print(f"\nCurrent status: {game.status}")
        print("Available statuses:")
        for index, s in enumerate(VALID_STATUSES, start=1):
            print(f"[{index}] {s}")
        
        status_choice = input("Choose a new status number (or press Enter to keep current): ").strip()
        
        if status_choice.isdigit() and 1 <= int(status_choice) <= len(VALID_STATUSES):
            game.status = VALID_STATUSES[int(status_choice) - 1]
            print(f"Status updated to: {game.status}")
        elif status_choice != "":
            print("Invalid choice. Status was not changed.")

    return game