# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:22:48 2026

@author: expor
"""

def show_edit_menu(game):
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        print("=======================")
        print("=   Current Details   =")
        print("=======================")
        print()
        print(f"Name: {game.name}")
        print(f"Publisher: {game.publisher}")
        print(f"Minimum players: {game.min_players}")
        print(f"Maximum players: {game.max_players}")
        print(f"Playing time: {game.playing_time} min")
        print(f"Publication year: {game.year}")
        print(f"Status: {game.status}")
        print()
        print("What would you like to change?")
        print("[1] Name")
        print("[2] Publisher")
        print("[3] Minimum players")
        print("[4] Maximum players")
        print("[5] Playing time")
        print("[6] Publication year")
        print("[7] Status")
        print()
        print("[8] Save changes and return")
        print("[9] Cancel without saving")
        print()
        choice = input("Choose an option: ").strip()
        if choice in options:
            return int(choice)
        else:
            print("Not a valid choice!")