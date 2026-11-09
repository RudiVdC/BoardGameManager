# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:34:25 2026

@author: expor
"""

def get_valid_integer(prompt):
    """Continuously prompts the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")