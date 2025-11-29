# === Group 5: Team members [Base Bangers] ===
Tasie Chidera Olive
Chibuzor Elijah Izuchukwu
Oluchukwu Promise .C
Ehiemere Cyril Chikodi
Chidiebere Tonia Tochi
Ugochukwu Samuel
Ihemamma Ozioma Wisdom
Chigozie Mary Nnaemeka
Josiah Victor Ikechukwu

## === Details of work done === 
1. Ensured name is stored in uppercase.

The program validates that the user‑supplied name contains only alphabetic characters. Upon successful validation, the name is automatically converted to uppercase using the .upper() method. This enforces a consistent data format, eliminating variations such as “ada”, “Ada”, or “aDa”, and ensuring all stored names follow a uniform standard (e.g., “ADA”).

2. Converted age to integer and added proper error handling.

To avoid invalid age entries (e.g., text or symbols), the input is transformed into an integer via int(). The conversion is placed within a try‑except block; if the user enters a non‑numeric value (such as “twenty”), an error message is displayed and re‑prompt is issued. This guarantees that the age values persisted in the dataset are valid numeric entries.

3. Capitalized colour input.

The user‑provided colour is formatted with .capitalize(), which makes the first letter uppercase and the remaining letters lowercase (e.g., “blue” becomes “Blue”, “RED” becomes “Red”). This yields consistent colour representation across records and enhances data cleanliness for later analysis.

4. Added loop to control number of records.

A loop structure was introduced to restrict the number of user entries per execution. The program is configured to accept a maximum of three (3) records. After each entry, a counter is incremented, and once the limit is reached the loop terminates automatically. This provides controlled data entry, prevents inadvertent infinite looping, and satisfies the assignment’s requirement for a fixed input size.

5. Wrote clear comments and docstrings across all functions.

Every function is equipped with a docstring that describes its purpose, functionality, and contribution to the overall workflow. In addition, inline comments have been inserted to clarify complex operations, validation steps, formatting logic, and flow control. This improves code readability, facilitates maintenance, and ensures reviewers can understand each segment without ambiguity.

6. Loaded processed data into a CSV file.

After gathering and validating all records, the program writes the data to a CSV file named record.csv. First, a header row (Id, Name, Age, Colour) is created to structure the file. Then, the data rows are appended one by one using a CSV writer. This completes the ETL pipeline: Extract - input from the user 
Transform - through formatting and validation, and Load - into a CSV dataset..