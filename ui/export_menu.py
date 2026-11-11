# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:12:04 2026

@author: expor
"""

def get_export_filename():
    report_name = input(
        "Give file name (default: BoardGameManager_Data.csv): "
    ).strip()

    if not report_name:
        return "BoardGameManager_Data.csv"

    extension = report_name.split(".")

    if extension[-1].lower() != "csv":
        report_name += ".csv"

    return report_name