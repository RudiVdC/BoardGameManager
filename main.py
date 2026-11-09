# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:43:33 2026

@author: expor
"""

from data_access.database import init_database
from data_access.game_repository import GameRepository
from domain.board_game import BoardGame
from ui.menu import show_menu
from service.export_data import export_games_to_csv
from ui.game_selection import select_games
from ui.menu_edit_game import show_edit_menu
from service.edit_data import edit_data

def get_valid_integer(prompt):
    """Continuously prompts the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
            
def main():
    # Initialize the database and tables at startup
    init_database()
    print("Welcome to the Board Game Manager!")

    while True:
        choice = show_menu()
        
        if choice == 1:
            print("\n--- Board Game Collection ---")
            games = GameRepository.get_all_games()
            if games:
                for game in games:
                    print(f"- {game}")
            else:
                print("No board games found in the collection yet.")
                
        elif choice == 2:
            print("\n--- Add a New Board Game ---")
            
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
            
            status = input("Enter status (e.g., Owned, Wishlist): ").strip()
            if not status:
                status = "Owned"
            
            # Create domain object and save via repository
            new_game = BoardGame(
                name=name,
                publisher=publisher,
                min_players=min_players,
                max_players=max_players,
                playing_time=playing_time,
                year=year,
                status=status
            )
            GameRepository.add_board_game(new_game)
            
        elif choice == 3:
            print("\n--- Search Board Game ---")
            search_term = input("Enter (part of) the game name to search: ").strip()
            
            if not search_term:
                print("Search term cannot be empty. Please try again.")
            else:
                games = GameRepository.search_games(search_term)
                
                if games:
                    print(f"\nFound {len(games)} matching game(s):")
                    for game in games:
                        print(f"- {game}")
                else:
                    print("No board games found matching your search.")
        
        elif choice == 4:
            print("\n--- Update board game details ---")
            selected_game = select_games()
            
            if selected_game:
                while True:
                    edit_choice = show_edit_menu(selected_game)
                    
                    if edit_choice == 8:
                        GameRepository.update_game(selected_game)
                        print("Changes saved successfully to the database!")
                        break
                    
                    elif edit_choice is not None:
                        selected_game = edit_data(edit_choice, selected_game)

        elif choice == 5:
            print("\n--- Remove a Board Game ---")
            selected_game = select_games()
            
            if selected_game:
                while True:
                    confirmation = input(
                        f"Are you sure you want to delete "
                        f"'{selected_game.name}'? (y/n): "
                    ).strip().lower()

                    if confirmation == "y":
                        GameRepository.delete_game(selected_game.id)
                        print(f"'{selected_game.name}' was successfully deleted!")
                        break
                    elif confirmation == "n":
                        print("Deletion cancelled.")
                        break
                    else:
                        print("Invalid choice. Please enter 'y' or 'n'.")

        elif choice == 6:
            print("\n--- Creating CSV Report ---")
            games = GameRepository.get_all_games()
        
            if games:
                report_name = input(
                    "Give file name (default: BoardGameManager_Data.csv): "
                ).strip()
        
                try:
                    if report_name == "":
                        filename = export_games_to_csv(games)
                    else:
                        extension = report_name.split(".")

                        if extension[-1].lower() != "csv":
                            report_name += ".csv"
                
                        filename = export_games_to_csv(games, report_name)
                
                    print(f"CSV report successfully created: {filename}")
        
                except PermissionError:
                    print(
                        "Unable to create the CSV file. "
                        "Please close the file in Excel and try again."
                    )
        
                except OSError as error:
                    print(f"An error occurred while creating the CSV file: {error}")
        
            else:
                print("No board games found in the collection yet.")
        else:
            print("\nThank you for using Board Game Manager. Goodbye!")
            break

if __name__ == "__main__":
    main()