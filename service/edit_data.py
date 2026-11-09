# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:59:39 2026

@author: expor
"""

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
        game.min_players = int(input(f"Enter new min players (current: {game.min_players}): "))
    elif choice == 4:
        game.max_players = int(input(f"Enter new max players (current: {game.max_players}): "))
    elif choice == 5:
        game.playing_time = int(input(f"Enter new playing time (current: {game.playing_time}): "))
    elif choice == 6:
        game.year = int(input(f"Enter new publication year (current: {game.year})): "))
    elif choice == 7:
        new_status = input(f"Enter new status (current: {game.status}): ").strip()
        if new_status:
            game.status = new_status
    return game