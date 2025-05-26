import json
import os # For checking if file exists
from plant_app.logic.models import Plant

DATA_FILE_PATH = "plant_app/data/plants.json"

def save_plants_to_json(plants_list: list[Plant]):
    """
    Saves the list of Plant objects to a JSON file.

    Args:
        plants_list: A list of Plant objects.
    """
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)
        
        plants_data = [plant.__dict__ for plant in plants_list]
        with open(DATA_FILE_PATH, 'w') as f:
            json.dump(plants_data, f, indent=4)
        # print(f"Data saved to {DATA_FILE_PATH}") # Optional: for debugging
    except IOError as e:
        print(f"Error saving plants to JSON: {e}")
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred during saving: {e}")

def load_plants_from_json() -> list[Plant]:
    """
    Loads the list of Plant objects from a JSON file.

    Returns:
        A list of Plant objects. Returns an empty list if the file doesn't exist
        or if an error occurs during loading.
    """
    if not os.path.exists(DATA_FILE_PATH):
        # print(f"Data file not found at {DATA_FILE_PATH}. Starting with an empty plant list.") # Optional
        return []

    try:
        with open(DATA_FILE_PATH, 'r') as f:
            if os.path.getsize(DATA_FILE_PATH) == 0: # Check if file is empty
                # print(f"Data file {DATA_FILE_PATH} is empty. Starting with an empty plant list.") # Optional
                return []
            plants_data = json.load(f)
            plants_list = [Plant(**data) for data in plants_data]
            # print(f"Data loaded from {DATA_FILE_PATH}") # Optional: for debugging
            return plants_list
    except IOError as e:
        print(f"Error loading plants from JSON: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {DATA_FILE_PATH}: {e}. Starting with an empty plant list.")
        # Optionally, you could back up the corrupted file here
        return []
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred during loading: {e}")
        return []
