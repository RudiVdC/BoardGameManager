# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:34:57 2026

@author: expor
"""

import csv
from data_access.game_repository import GameRepository
from ui.export_menu import get_export_filename

def export_games_to_csv(games_data, filename="BoardGameManager_Data.csv"):
    """
    Exporteert een alfabetisch gesorteerde lijst met spellen naar een CSV-bestand.
    """
    headers = ["ID", "Name", "Publisher", "Min Players", "Max Players", "Playing Time", "Year", "Status"]
    
    sorted_games = sorted(games_data, key=lambda game: game.name.lower())

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)

        for game in sorted_games:
            writer.writerow([
                game.id, game.name, game.publisher,
                game.min_players, game.max_players,
                game.playing_time, game.year, game.status
            ])

    return filename

def create_csv_report():
    games = GameRepository.get_all_games()

    if not games:
        print("No board games found in the collection yet.")
        return

    filename = get_export_filename()

    try:
        filename = export_games_to_csv(games, filename)
        print(f"CSV report successfully created: {filename}")

    except PermissionError:
        print(
            "Unable to create the CSV file. "
            "Please close the file in Excel and try again."
        )

    except OSError as error:
        print(f"An error occurred while creating the CSV file: {error}")