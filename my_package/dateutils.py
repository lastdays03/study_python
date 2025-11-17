# my_package/dateutils.py
"""
Date utils module for my package
"""
from datetime import datetime

def to_date(value: str) -> str:
    return datetime.strptime(value, "%Y-%m-%d").date()