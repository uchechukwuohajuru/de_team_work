import csv

data = []        # Will hold each user entry as a list of lists
user_id = 0      # Auto-increment user ID

def set_file():
    """
    Creates the CSV file (record.csv) and writes the header row.
    This ensures the destination file has the correct structure.
    """
    header_row = ['Id', 'Name', 'Age', 'Colour']
    with open("record.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_row)
    return "File created successfully"


def get_data():
    """
    Collects user input, validates it, formats it properly:
     - Name in ALL CAPS
     - Age as an integer
     - Colour capitalized
    Returns a single record as a list.
    """
    global user_id

    # Name validation to ensure that name is alphabet and is in all CAPS using Try/Except
    while True:
        try:
            user_name = input("Enter your name: ")
            if not user_name.isalpha(): # This allows the input to accept word names
                raise ValueError("Name must contain only letters")
            user_name = user_name.upper() # This converts all inputs to Capital letter (UpperCase)
            break # This stops the while loop (code), if the above condition is met
        except ValueError as e:
            print(f"❌ {e}\nTry again.")


    # Age validation using Try/Except for error handling
    while True:
        try:
            user_age = int(input("Enter your age: "))  # This accepts age as integer
            break
        except ValueError:
            print("❌ Invalid input. Age must be numbers only. \n Try again.")

    # Formating color to Intial capitalization using .capitalize()
    user_colour = input("Enter your favourite colour: ").capitalize()  # Task 1c

    # Adding to the user_id variable above (Incrementing)
    user_id += 1

    # Create a single user record instead of appending individual fields to data
    record = [user_id, user_name, user_age, user_colour]

    # Append record to the main data list
    data.append(record)
    return record


def load_data():
    """
    Loads all records from the data list into the CSV file.
    Uses append mode so each new entry is written to the file.
    """
    # Open file in append mode
    with open('record.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        # write each record in the data list into the csv file
        for record in data:
            writer.writerow(record)

    print("Data loaded successfully!")


def main():
    """
    Controls the entire ETL process.
    Limits the number of entries using a loop (Task 3).
    """
    set_file()     # Step 1: Create file
    max_entries = 5   # Control structure (limit number of users)
    count = 0
    while count < max_entries:
        print(f"\n--- Enter Record {count + 1} ---")
        get_data()
        count += 1
    load_data()    # Step 3: Load data into .CSV file
if __name__ == "__main__":
    main()
# This script collects user data, validates it, and writes it to a CSV file.