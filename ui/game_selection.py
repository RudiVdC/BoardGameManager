# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:49:32 2026

@author: expor
"""
from data_access.game_repository import GameRepository

def select_games(): 
    """
    Interactive search and selection of a board game.
    Returns the selected BoardGame object, or None if cancelled/not found.
    """
    all_games = GameRepository.get_all_games()
    
    if not all_games:
        print("No board games found in the database.")
        return None
    
    filtered_games = all_games
    search_term = ""

    while True:
        print(f"\nCurrent search: '{search_term}'")
        print(f"Number of matching games: {len(filtered_games)}")

        print("-" * 40)

        for index, game in enumerate(filtered_games, start=1):
            print(f"[{index}] {game.name} ({game.year})")

        print("-" * 40)

        action = input(
            "Enter letters to filter, a number to select a game, "
            "'clear' to reset the search or 'cancel' to cancel: "
        ).strip()

        if action.lower() == "cancel":
            return None

        elif action.lower() == "clear":
            search_term = ""
            filtered_games = all_games

        elif action == "":
            print("Please enter something.")

        elif action.isdigit():
            choice_index = int(action)

            if 1 <= choice_index <= len(filtered_games):
                selected_game = filtered_games[choice_index - 1]
                return selected_game
            else:
                print("Invalid number. Please try again.")

        else:
            search_term += action

            filtered_games = [
                game for game in all_games
                if search_term.lower() in game.name.lower()
            ]

            if not filtered_games:
                print(
                    f"No games found matching '{search_term}'. "
                    "The search has been reset."
                )
                filtered_games = all_games
                search_term = ""