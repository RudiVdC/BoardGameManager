# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:28:04 2026

@author: expor
"""

from ui.helpers import get_valid_integer
from domain.board_game import VALID_STATUSES
from service.game_validation import is_positive_number, is_valid_player_range

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
        while True:
            min_players = get_valid_integer(f"Enter new minimum players (current: {game.min_players}): ")
    
            if is_positive_number(min_players):
                game.min_players = min_players
                break
    
            print("Minimum players must be greater than zero.")

    if game.max_players < game.min_players:
        print("The current maximum number of players is too low.")

        while True:
            max_players = get_valid_integer(f"Enter new maximum players (minimum: {game.min_players}): ")

            if is_valid_player_range(game.min_players, max_players):
                game.max_players = max_players
                break

            print("Maximum players must be at least equal to minimum players.")
        
    elif choice == 4:
        while True:
            max_players = get_valid_integer(f"Enter new maximum players (current: {game.max_players}): ")
        
            if is_valid_player_range(game.min_players, max_players):
                game.max_players = max_players
                break
        
            print("Invalid player range! Maximum players must be positive "
                  "and cannot be lower than minimum players.")
        
    elif choice == 5:
        while True:
            playing_time = get_valid_integer(
                f"Enter new playing time in minutes (current: {game.playing_time}): "
            )
    
            if is_positive_number(playing_time):
                game.playing_time = playing_time
                break
    
            print("Playing time must be greater than zero.")
        
    elif choice == 6:
        while True:
            year = get_valid_integer(
                f"Enter new publication year (current: {game.year}): "
            )
    
            if is_positive_number(year):
                game.year = year
                break
    
            print("Publication year must be greater than zero.")
        
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