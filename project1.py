"""
Simple ETL Pipeline
Author: Uche Ohajuru
Date: 2025-11-17
"""

import csv

data = []     # Stores all user records
user_id = 0   # Unique ID for each entry


def set_file():
    '''This function helps you set up your CSV file with the right headers.'''
    header_row = ['Id', 'Name', 'Age', 'Colour']
    with open("record.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header_row)
    return "File created successfully"


def get_data():
    """This function should allow you get data from the user and 
    append it to the list as a list of lists"""
    global user_id

    # Validate name
    while True:
        user_name = input("Enter your name: ")
        if user_name.replace(" ", "").isalpha():
            user_name = user_name.upper()        
            break
        else:
            print("Name must contain only alphabets. Try again.")

    # Validate age
    while True:
        user_age = input("Enter your age: ")
        if user_age.isdigit():
            user_age = int(user_age)             
            break
        else:
            print("Age must be a number. Try again.")

    # Colour (capitalize first letter)
    user_colour = input("Enter your favourite colour: ")
    user_colour = user_colour.capitalize()       

    user_id += 1

    # Construct and return a record list
    record = [user_id, user_name, user_age, user_colour]
    return record


def load_data(record):
    """Load data to destination using the append mode."""

    with open("record.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record)

    print("Data loaded successfully!")


def main():
     # ETL process
    print(set_file())
   
    MAX_RECORDS = 3
    count = 0

    while count < MAX_RECORDS:
        record = get_data()   # get one complete user record
        data.append(record)   # store record in list 
        load_data(record)     # write record to CSV

        count += 1
        print(f"Record {count}/{MAX_RECORDS} saved.\n")


if __name__ == "__main__":
    main()

# get_data()
# print(data)