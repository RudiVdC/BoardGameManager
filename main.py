# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:43:33 2026

@author: expor
"""

from ui.menu import show_menu

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