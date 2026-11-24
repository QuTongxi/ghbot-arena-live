"""Minimal availability helper used as review fixture."""

def open_seats(capacity: int, booked: int) -> int:
    """Return remaining seats; never negative."""
    return max(0, capacity - booked)
