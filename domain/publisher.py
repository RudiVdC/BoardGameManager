# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:18:38 2026

@author: expor
"""

class Publisher:
    def __init__(self, name, publisher_id=None):
        self.id = publisher_id
        self.name = name

    def __str__(self):
        return self.name