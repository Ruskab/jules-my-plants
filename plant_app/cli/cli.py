from plant_app.logic.actions import add_plant, view_plants, mark_plant_as_watered
from plant_app.logic.models import Plant # Imported for potential type hinting or future use

def run_cli():
    """Runs the command-line interface for the Plant Watering App."""
    print("Welcome to the Plant Watering App!")

    while True:
        print("\nMenu:")
        print("1. Add a new plant")
        print("2. View all plants")
        print("3. Mark a plant as watered")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n--- Add a New Plant ---")
            name = input("Enter plant name: ")
            while True:
                try:
                    watering_frequency_str = input("Enter watering frequency (in days): ")
                    watering_frequency = int(watering_frequency_str)
                    if watering_frequency <= 0:
                        print("Watering frequency must be a positive number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for watering frequency.")

            # Basic validation for date format (YYYY-MM-DD) can be added here if desired
            # For simplicity, we'll assume correct format for now, as full validation
            # can be complex without external libraries or more extensive regex.
            # A more robust solution might involve date parsing and validation.
            last_watered_date = input("Enter last watered date (YYYY-MM-DD): ")

            # Basic check for date format
            if not (len(last_watered_date) == 10 and last_watered_date[4] == '-' and last_watered_date[7] == '-'):
                print("Invalid date format. Please use YYYY-MM-DD. Plant not added.")
                continue
            try:
                # Further check if year, month, day are numbers
                year, month, day = map(int, last_watered_date.split('-'))
                # This doesn't check for valid day/month ranges (e.g. 31st Feb)
                # For true date validation, datetime.date.fromisoformat would be better
                # but we want to keep it simple as per instructions.
            except ValueError:
                print("Invalid date components. Please use YYYY-MM-DD with numbers. Plant not added.")
                continue


            added_plant = add_plant(name, watering_frequency, last_watered_date)
            print(f"\nPlant '{added_plant.name}' added successfully!")
            print(f"  Watering Frequency: {added_plant.watering_frequency} days")
            print(f"  Last Watered: {added_plant.last_watered_date}")

        elif choice == "2":
            print("\n--- View All Plants ---")
            plant_info = view_plants()
            if isinstance(plant_info, str):
                print(plant_info)
            else:
                for info_str in plant_info:
                    print(info_str)

        elif choice == "3":
            print("\n--- Mark a Plant as Watered ---")
            name = input("Enter the name of the plant to mark as watered: ")
            message = mark_plant_as_watered(name)
            print(message)

        elif choice == "4":
            print("Exiting Plant Watering App. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # This allows direct execution of cli.py for testing if needed,
    # but the main entry point will be through plant_app/main.py
    run_cli()
