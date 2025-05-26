from dataclasses import dataclass

@dataclass
class Plant:
    """Represents a plant with its watering information."""
    name: str
    watering_frequency: int  # in days
    last_watered_date: str  # ISO format date string (YYYY-MM-DD)
