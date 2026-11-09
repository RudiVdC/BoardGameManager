# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:31:03 2026

@author: expor
"""

VALID_STATUSES = ["Owned", "Wishlist", "Played", "For Sale"]

class BoardGame:
    def __init__(self, name, publisher, min_players, max_players, playing_time, year, status, game_id=None):
        self.id = game_id
        self.name = name
        self.publisher = publisher
        self.min_players = min_players
        self.max_players = max_players
        self.playing_time = playing_time
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.name} ({self.year}) - Publisher: {self.publisher}"