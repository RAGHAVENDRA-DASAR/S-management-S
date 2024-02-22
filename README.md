# Student Records Management System

## Introduction
This Student Records Management System is a Python application designed to manage and store information about students. It provides a user-friendly interface for performing operations such as adding, updating, deleting, searching, and exporting student records. The application uses SQLite for data storage and Tkinter for the graphical user interface.

## Features
- **Add New Student:** Enter details about a new student, including personal information, contact details, and academic information.
- **Edit Student Information:** Modify the details of an existing student in the database.
- **Delete Student Record:** Remove a student's information from the database.
- **Search Student:** Retrieve and display details of a student based on their unique ID.
- **Calculate Balance:** Automatically calculate the balance amount based on the total fee and amount paid.
- **Export to Excel:** Export all student records to an Excel file for easy sharing and analysis.

## Getting Started
1. **Dependencies:**
   - Ensure you have Python installed on your machine.
   - Install the required dependencies using the following command:
     ```
     pip install openpyxl
     pip install sqlite3
     ```

2. **Running the Application:**
   - Execute the main program (`main.py`) to launch the application.
   - The application will open a login panel where you can enter your credentials.

3. **Database:**
   - The application uses an SQLite database (`Students_Records_DB_File.db`) to store student information.
   - The database file is created in the same directory as the application.

## Usage
- **Login:**
  - Use the login panel to enter your credentials. The default username and password are provided in the code.

- **Main Application:**
  - Once logged in, you'll have access to the main application with various buttons for performing operations.
  - The TreeView displays a list of students with their basic details.

- **Adding and Editing Students:**
  - Click the "Save" button to add a new student or update existing student information.

- **Deleting Students:**
  - Select a student from the list and click the "Delete" button to remove the student's record.

- **Searching Students:**
  - Enter a student ID and click the "Search" button to retrieve and display the student's details.

- **Exporting to Excel:**
  - Click the "Excel File" button to export all student records to an Excel file.

- **Exiting the Application:**
  - Click the "Exit" button to close the application.

## Contributing
Contributions are welcome! Feel free to open issues, submit pull requests, or provide feedback.
.
