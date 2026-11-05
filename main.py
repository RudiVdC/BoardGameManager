# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:43:33 2026

@author: expor
"""

def show_menu():
    options = ["1", "2", "3", "4"]
    while True:
        print("=================================")
        print("       BOARD GAME MANAGER")
        print("=================================")
        print()
        print("1. View board game collection")
        print("2. Add a board game")
        print("3. Search for a board game")
        print("4. Exit")
        print()
        choice = input("Choose an option: ")
        if choice in options:
            return int(choice)
        else:
            print("Geen geldige keuze!")

def main():
    while True:
        choice = show_menu()
        if choice == 1:
            print("Toon de bordspelcollectie")
        elif choice == 2:
            print("Voeg een bordspel toe")
        elif choice == 3:
            print("Zoek een bordspel")
        else:
            print("Goodbye!")
            break
    
if __name__ == "__main__":
    main()