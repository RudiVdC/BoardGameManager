# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 10:36:14 2026

@author: expor
"""

def is_positive_number(value):
    """Checks whether a number is greater than zero."""
    return value > 0


def is_valid_player_range(min_players, max_players):
    """Checks whether the player range is valid."""
    return min_players > 0 and max_players >= min_players