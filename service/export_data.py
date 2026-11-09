# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:34:57 2026

@author: expor
"""

import csv

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