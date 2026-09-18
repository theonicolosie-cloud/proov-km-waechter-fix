# fleet_utils.py
# Utility helpers for Vossberg Mobility fleet reporting.
# Written in 2013. Modernised 2025: dead code removed, inverted miles constant corrected.

MILES_PER_KM = 0.621371  # was 1.609 (km-per-mile) — wrong direction, corrected


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a whole-number percentage string."""
    return f"{int(value)}%"


def mean(values: list) -> float:
    """Return the arithmetic mean of a list of numbers, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)
