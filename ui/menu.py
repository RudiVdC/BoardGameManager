# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:27:35 2026

@author: expor
"""

def show_menu():
    options = ["1", "2", "3", "4", "5", "6"]
    while True:
        print("=================================")
        print("       BOARD GAME MANAGER")
        print("=================================")
        print()
        print("1. View board game collection")
        print("2. Add a board game")
        print("3. Search for a board game")
        print("4. Remove a board game from your collection")
        print("5. Export data to Excel file")
        print()
        print("6. Exit")
        print()
        choice = input("Choose an option: ")
        if choice in options:
            return int(choice)
        else:
            print("Not a valid choice!")