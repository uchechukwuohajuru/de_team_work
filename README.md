# === Tasks ===

Task 1.
Modify the code in the file named project1.py such that:
    a. Names will appear in all caps
    b. Age will be of the int data type
    c. Colour will start with a Capital letter

Task 2.
Add error handling lines of code to take care of:
    a. Non digit input for age
    b. Non alphabet input for names

Task 3.
Use appropriate control structures to control: 
    a. the number of items on the list before breaking or exiting

Task 4.
Make your team work readable using comments and docstrings.

## === How to Submit === 
1. After your work, modify this readme file to include:
    a. List of active team members
    b. Detail of work done
2. The team lead alone should:
    a. modify the .gitignore file to include proper ignore list
    b. add all changes
    c. commit all changes with proper message
    d. push the code to me on a branch whoes name is your team name


## === Names of Active Team Members ===
    1. Isiguzoro Celine Chinonyerem
    2. Godslead Agwu Johnson 
    3. Onyekere Michael
    4. Otuonye Chinanuekpere Rachael
    5. Nwachineke Ulochiwuru Chimgozirim
    6. Kalu Joshua Ifeanyi
    7. Jacob Charity Chidinma
    8. Chimezie Philomena Ogechi 
    9. Nwankwo Chukwudozie Oliver
    10. Emeh Glory Chiamaka 
    

## === Details of work done ===

# Project 1 – Simple ETL Pipeline

#   Overview

This project implements a simple ETL (Extract, Transform, Load) pipeline in Python to collect user data and save it to a CSV file. The program ensures proper data validation, formatting, and safe row-by-row storage of records.

The solution is modular, uses descriptive method names for readability, and includes docstrings and comments to explain the workflow.


#   Detail of Work Done

#   1. CSV File Creation

* Created a CSV file (`record.csv`) with the correct headers: `Id, Name, Age, Colour`.
* Implemented in the method *`set_file()`*.
* Ensures the file is ready before any data entry.


#   2. Data Collection and Transformation

* Collected user input for **Name, Age, and Favourite Colour.

* Applied input validations:

  | Field  | Validation                      | Transformation           |
  | ------ | ------------------------------- | ------------------------ |
  | Name   | Only letters and spaces allowed | Converted to ALL CAPS    |
  | Age    | Only digits allowed             | Converted to integer     |
  | Colour | Only letters allowed            | Capitalized first letter |



#   3. Row-by-Row Data Saving

* Each record is saved immediately to the CSV using `load_data(record)`.
* This prevents data loss in case the program stops unexpectedly.
* Implements the ETL principle: Extract → Transform → Load.



#   4. Controlled Number of Records

    Program prompts the user:

  ```
  How many records do you want to input?
  ```
     Uses a loop to collect exactly the number of records requested or stops early if the user chooses:

  ```
  Do you want to enter another record (y/n)?
  ```


#   5. Auto-incrementing ID

 *Each record is assigned a unique ID using a global counter.*
 *Ensures data integrity in the CSV file.*


#   6. Code Readability and Documentation**

     Descriptive method names improve code readability:

  | Function                            | Purpose                                     |
  | ----------------------------------- | ------------------------------------------- |
  | `set_file()`                        | Setup CSV file                              |
  | `get_data()`                        | Validate and format name,colour, convert age|     
  |`load_data(record)`                  | Append record to CSV                        |
  | `main()`                            | Controls program flow and user interaction  |

* All functions include *docstrings* and *inline comments*.

* Modular design follows best practices for Python ETL scripts.


# 7. Error Handling

    a. Non-alphabet names are rejected.
    b. Non-digit ages are rejected.
    c.Invalid colours (numbers or symbols) are rejected.
* User is prompted repeatedly until correct input is provided.



# 8. Program Output

* Data saved in `record.csv` with each record as one row:

Example:

| Id | Name         | Age | Colour |
| -- | ----------   | --- | ------ |
| 1  | EMEH GLORY   | 25  | Blue   |
| 2  | KALU LAWRENCE| 30  | Red    |



