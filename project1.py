"""
Simple ETL Pipeline
Author: Uche Ohajuru
Date: 2025-11-17

Modified by: Team Avengers _ Data Engineering Class A
Date: 2025-11-26



"""

import csv  # import library

# Global list to store just the current row (not all rows)
data = []   

# Global ID counter
user_id = 0


def set_file():

    """
    Creates the CSV file with the correct column headers.
    This runs only once at the beginning.
    """
    header_row = ['Id', 'Name', 'Age', 'Colour']

    # Create file and write header
    with open("record.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_row)

    return "file created successfully"


def get_data():

    """
    Collects ONE record from the user with validations.
    Returns a list representing a single row.
    """

    # NAME VALIDATION 
    while True:
        user_name = input("Enter your name: ")      # accets input from user
        if user_name.replace(" ", "").isalpha():     # allows spaces between names
            user_name = user_name.upper()            # Task 1: make name all caps
            break
        else:
            print("Error: Name must contain alphabets only.\n")

    #  AGE VALIDATION 
    while True:
        user_age = input("Enter your age: ")
        if user_age.isdigit():                       # ensures digits only
            user_age = int(user_age)                 # Task 1: convert to int
            break
        else:
            print("Error: Age must be a number only.\n")

    # COLOUR VALIDATION 
    while True:
        user_colour = input("Enter your favourite colour: ")
        if user_colour.replace(" ", "").isalpha():   # alphabets only
            user_colour = user_colour.capitalize()   # Task 1: Capitalize
            break
        else:
            print("Error: Colour must contain alphabets only.\n")

    # Auto-increment ID
    global user_id
    user_id += 1

    # Prepare a SINGLE RECORD
    record = [user_id, user_name, user_age, user_colour]

    return record



def load_data(record):
    """
    Writes ONE record row-by-row into the CSV file.
    """
    with open("record.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

    print("Record saved successfully!\n")



def main():
    """
    Controls program flow:
    - Creates file
    - Asks user how many records to input
    - Repeats data entry until limit reached or user stops
    """

    # Create CSV file
    set_file()

    # Ask the user how many records they want to input
    while True:
        max_rec = input("How many records do you want to input? ")  # Ask user to input maximum record he wants to input
        if max_rec.isdigit():       # check if the input from user is number
            max_rec = int(max_rec)
            break
        else:
            print("Please enter digits only.\n")


    # Loop to collect records
    for count in range(max_rec):
        record = get_data()          # collect one record
        load_data(record)            # save one record

        # Ask if user wants to continue
        cont = input("Do you want to enter another record (y/n)? ").strip().lower()
        if cont in ("n", "no"):
            break

    print("All records have been successfully saved.")


# Run program
if __name__ == "__main__":
    main()
    # print(get_data())