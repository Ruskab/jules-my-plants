from datetime import date, timedelta
from .models import Plant
from plant_app.data.data_manager import save_plants_to_json, load_plants_from_json

# Load plants from JSON when the module is initialized
plants_list: list[Plant] = load_plants_from_json()

def add_plant(name: str, watering_frequency: int, last_watered_date: str) -> Plant:
    """
    Creates a new Plant object and adds it to the plants_list.

    Args:
        name: The name of the plant.
        watering_frequency: How often the plant needs to be watered (in days).
        last_watered_date: The date the plant was last watered (YYYY-MM-DD).

    Returns:
        The created Plant object.
    """
    new_plant = Plant(
        name=name,
        watering_frequency=watering_frequency,
        last_watered_date=last_watered_date,
    )
    plants_list.append(new_plant)
    save_plants_to_json(plants_list)  # Save after adding
    return new_plant

def view_plants() -> list[str] | str:
    """
    Generates a list of strings representing plants and their watering status.

    Returns:
        A list of strings with plant information, or a message if no plants exist.
    """
    if not plants_list:
        return "No plants added yet."

    plant_statuses = []
    today = date.today()

    for plant in plants_list:
        try:
            last_watered_date_obj = date.fromisoformat(plant.last_watered_date)
        except ValueError:
            # Handle invalid date format gracefully
            status_str = (
                f"Plant: {plant.name}\n"
                f"  Last Watered: {plant.last_watered_date} (Invalid date format)\n"
                f"  Watering Frequency: {plant.watering_frequency} days\n"
                f"  Status: [UNKNOWN - Invalid Date]"
            )
            plant_statuses.append(status_str)
            continue

        next_watering_date = last_watered_date_obj + timedelta(days=plant.watering_frequency)
        needs_watering = next_watering_date <= today

        status_indicator = "[NEEDS WATERING!]" if needs_watering else "[OK]"

        status_str = (
            f"Plant: {plant.name}\n"
            f"  Last Watered: {plant.last_watered_date}\n"
            f"  Watering Frequency: {plant.watering_frequency} days\n"
            f"  Next Watering Date: {next_watering_date.isoformat()}\n"
            f"  Status: {status_indicator}"
        )
        plant_statuses.append(status_str)

    return plant_statuses

def mark_plant_as_watered(plant_name: str) -> str:
    """
    Marks a specific plant as watered today.

    Args:
        plant_name: The name of the plant to mark as watered.

    Returns:
        A message indicating success or failure.
    """
    today_str = date.today().isoformat()
    for plant in plants_list:
        if plant.name == plant_name:
            plant.last_watered_date = today_str
            save_plants_to_json(plants_list)  # Save after marking as watered
            return f"'{plant.name}' has been marked as watered today."
    return f"Plant named '{plant_name}' not found."
