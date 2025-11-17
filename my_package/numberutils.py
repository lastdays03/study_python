# my_package/numberutils.py
"""
Number utils module for my package
"""

def to_money(value: int) -> str:
    return f"{value:,.0f}원"

def to_percent(value: float) -> str:
    return f"{value:.2%}"

def to_comma(value: int) -> str:
    return f"{value:,.0f}"