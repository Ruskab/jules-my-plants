import unittest
import os
import json
from datetime import date, timedelta

from plant_app.logic.models import Plant
from plant_app.logic.actions import add_plant, view_plants, mark_plant_as_watered, plants_list
# We need to be able to patch the DATA_FILE_PATH used by actions indirectly
import plant_app.data.data_manager as data_manager_module
import plant_app.logic.actions # For test_data_persistence

# The actual data_manager functions will be tested through the actions module
# but we need these to manipulate the test data file directly for assertions.
from plant_app.data.data_manager import save_plants_to_json, load_plants_from_json


TEST_DATA_FILE = "plant_app/data/test_plants.json"
ORIGINAL_DATA_FILE_PATH_BACKUP = None

class TestPlantAppLogic(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test."""
        global ORIGINAL_DATA_FILE_PATH_BACKUP
        # Backup and patch the data file path in the data_manager module
        ORIGINAL_DATA_FILE_PATH_BACKUP = data_manager_module.DATA_FILE_PATH
        data_manager_module.DATA_FILE_PATH = TEST_DATA_FILE # Patch it for actions.py's load

        # Ensure the directory for TEST_DATA_FILE exists, create if not
        os.makedirs(os.path.dirname(TEST_DATA_FILE), exist_ok=True)

        # Ensure no test data file exists from previous (potentially failed) runs
        # before we try to load from it.
        if os.path.exists(TEST_DATA_FILE):
            os.remove(TEST_DATA_FILE)
        
        # Now that DATA_FILE_PATH is patched and TEST_DATA_FILE is clean,
        # reload plants_list in actions.py to ensure it's empty or reflects TEST_DATA_FILE.
        # This simulates the state of actions.plants_list at the start of the app
        # when the data file is TEST_DATA_FILE.
        plant_app.logic.actions.plants_list = load_plants_from_json() # Uses patched path, should be empty list

    def tearDown(self):
        """Clean up test environment after each test."""
        global ORIGINAL_DATA_FILE_PATH_BACKUP
        
        # Clean up the test data file first
        if os.path.exists(TEST_DATA_FILE):
            os.remove(TEST_DATA_FILE)

        # Restore the original data file path
        if ORIGINAL_DATA_FILE_PATH_BACKUP:
            data_manager_module.DATA_FILE_PATH = ORIGINAL_DATA_FILE_PATH_BACKUP
            # Reload actions.plants_list with the original data file to leave actions module in a clean state
            plant_app.logic.actions.plants_list = load_plants_from_json() 
        
        # plants_list.clear() might not be necessary here if we are reloading,
        # but doesn't hurt if load_plants_from_json() fails for some reason.
        # However, the primary mechanism should be the reload.
        # plants_list.clear() # This refers to the 'from... import plants_list' which is a direct reference

    def test_add_plant(self):
        """Test adding a plant and data persistence."""
        plant_name = "Cactus"
        watering_frequency = 14
        last_watered_date = "2023-01-01"

        added_plant = add_plant(plant_name, watering_frequency, last_watered_date)

        # Assert plant in memory (plant_app.logic.actions.plants_list)
        self.assertEqual(len(plant_app.logic.actions.plants_list), 1)
        self.assertEqual(plant_app.logic.actions.plants_list[0].name, plant_name)
        self.assertEqual(plant_app.logic.actions.plants_list[0].watering_frequency, watering_frequency)
        self.assertEqual(plant_app.logic.actions.plants_list[0].last_watered_date, last_watered_date)
        self.assertEqual(added_plant, plant_app.logic.actions.plants_list[0])

        # Assert plant in test data file
        self.assertTrue(os.path.exists(TEST_DATA_FILE))
        # load_plants_from_json directly uses the patched data_manager_module.DATA_FILE_PATH
        loaded_from_file = load_plants_from_json() 
        self.assertEqual(len(loaded_from_file), 1)
        self.assertEqual(loaded_from_file[0].name, plant_name)
        self.assertEqual(loaded_from_file[0].watering_frequency, watering_frequency)
        self.assertEqual(loaded_from_file[0].last_watered_date, last_watered_date)

    def test_mark_plant_as_watered(self):
        """Test marking a plant as watered and data persistence."""
        plant_name = "Fern"
        # add_plant uses and modifies plant_app.logic.actions.plants_list
        add_plant(plant_name, 7, "2023-01-01") 

        today_str = date.today().isoformat()
        message = mark_plant_as_watered(plant_name)

        self.assertEqual(message, f"'{plant_name}' has been marked as watered today.")
        
        # Assert plant in memory (plant_app.logic.actions.plants_list)
        self.assertEqual(len(plant_app.logic.actions.plants_list), 1)
        self.assertEqual(plant_app.logic.actions.plants_list[0].name, plant_name)
        self.assertEqual(plant_app.logic.actions.plants_list[0].last_watered_date, today_str)

        # Assert plant in test data file
        loaded_from_file = load_plants_from_json() # Uses patched path
        self.assertEqual(len(loaded_from_file), 1)
        self.assertEqual(loaded_from_file[0].name, plant_name)
        self.assertEqual(loaded_from_file[0].last_watered_date, today_str)

        # Test marking a non-existent plant
        non_existent_plant_name = "Ghost Plant"
        message_not_found = mark_plant_as_watered(non_existent_plant_name)
        self.assertEqual(message_not_found, f"Plant named '{non_existent_plant_name}' not found.")
        
        # Ensure data hasn't changed for the existing plant
        loaded_from_file_after_failed_mark = load_plants_from_json()
        self.assertEqual(len(loaded_from_file_after_failed_mark), 1)
        self.assertEqual(loaded_from_file_after_failed_mark[0].last_watered_date, today_str)

    def test_view_plants_logic(self):
        """Test the logic of view_plants for watering status."""
        today = date.today()
        needs_watering_date = (today - timedelta(days=10)).isoformat()
        ok_date = (today - timedelta(days=1)).isoformat()

        add_plant("Monstera", 7, needs_watering_date) # Needs watering
        add_plant("Snake Plant", 14, ok_date)      # OK

        plant_statuses = view_plants()
        
        self.assertIsInstance(plant_statuses, list)
        self.assertEqual(len(plant_statuses), 2)

        # Check Monstera (needs watering)
        self.assertIn("Plant: Monstera", plant_statuses[0])
        self.assertIn(f"Last Watered: {needs_watering_date}", plant_statuses[0])
        self.assertIn("Watering Frequency: 7 days", plant_statuses[0])
        self.assertIn("[NEEDS WATERING!]", plant_statuses[0])

        # Check Snake Plant (ok)
        self.assertIn("Plant: Snake Plant", plant_statuses[1])
        self.assertIn(f"Last Watered: {ok_date}", plant_statuses[1])
        self.assertIn("Watering Frequency: 14 days", plant_statuses[1])
        self.assertIn("[OK]", plant_statuses[1])

        # Test with invalid date format
        # Clear plant_app.logic.actions.plants_list for isolated test
        plant_app.logic.actions.plants_list.clear() 
        if os.path.exists(TEST_DATA_FILE): # clean slate for this specific sub-test
            os.remove(TEST_DATA_FILE)
            save_plants_to_json(plant_app.logic.actions.plants_list) # Ensure file reflects empty list

        add_plant("Spider Plant", 5, "invalid-date-format")
        plant_statuses_invalid = view_plants()
        self.assertIsInstance(plant_statuses_invalid, list)
        self.assertEqual(len(plant_statuses_invalid), 1) # Should be 1 after adding Spider Plant
        self.assertIn("Plant: Spider Plant", plant_statuses_invalid[0])
        self.assertIn("Last Watered: invalid-date-format (Invalid date format)", plant_statuses_invalid[0])
        self.assertIn("[UNKNOWN - Invalid Date]", plant_statuses_invalid[0])

    def test_view_plants_empty(self):
        """Test view_plants when no plants are added."""
        # setUp ensures plant_app.logic.actions.plants_list is empty (loaded from empty/non-existent TEST_DATA_FILE)
        self.assertEqual(len(plant_app.logic.actions.plants_list), 0) # Double check
        message = view_plants() # view_plants reads from plant_app.logic.actions.plants_list
        self.assertEqual(message, "No plants added yet.")

    def test_data_persistence(self):
        """Test saving and loading plants from JSON."""
        plant1_data = {"name": "Rose", "watering_frequency": 2, "last_watered_date": "2023-02-01"}
        plant2_data = {"name": "Tulip", "watering_frequency": 3, "last_watered_date": "2023-02-02"}

        # add_plant appends to plant_app.logic.actions.plants_list and saves
        add_plant(**plant1_data)
        add_plant(**plant2_data)

        self.assertEqual(len(plant_app.logic.actions.plants_list), 2)

        # Clear the in-memory list in actions.py to simulate app restart
        plant_app.logic.actions.plants_list.clear()
        self.assertEqual(len(plant_app.logic.actions.plants_list), 0)

        # Load plants from the test data file.
        # The actions.py module's plants_list is loaded at module import,
        # but for this test, we want to explicitly test the load_plants_from_json
        # and then re-assign to the actions.plants_list to simulate how it would
        # behave on a fresh start where it's populated by load_plants_from_json.
        
        # The setUp already patches data_manager_module.DATA_FILE_PATH to TEST_DATA_FILE
        # So load_plants_from_json() will read from TEST_DATA_FILE
        loaded_plants = load_plants_from_json()
        
        # Assign to the global list in actions module to mimic application load
        # This is what `plants_list: list[Plant] = load_plants_from_json()` does in actions.py
        plant_app.logic.actions.plants_list = loaded_plants # Use the imported module

        self.assertEqual(len(plant_app.logic.actions.plants_list), 2)
        
        # Access via the module path for consistency in this part of the test
        plant1_loaded = plant_app.logic.actions.plants_list[0]
        plant2_loaded = plant_app.logic.actions.plants_list[1]

        # Check in specific order if necessary, or find by name
        if plant1_loaded.name != plant1_data["name"]: # Ensure correct order for comparison
             plant1_loaded, plant2_loaded = plant2_loaded, plant1_loaded

        self.assertEqual(plant1_loaded.name, plant1_data["name"])
        self.assertEqual(plant1_loaded.watering_frequency, plant1_data["watering_frequency"])
        self.assertEqual(plant1_loaded.last_watered_date, plant1_data["last_watered_date"])

        self.assertEqual(plant2_loaded.name, plant2_data["name"])
        self.assertEqual(plant2_loaded.watering_frequency, plant2_data["watering_frequency"])
        self.assertEqual(plant2_loaded.last_watered_date, plant2_data["last_watered_date"])

if __name__ == '__main__':
    unittest.main()
