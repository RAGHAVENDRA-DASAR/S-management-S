import tkinter as tk
import os,openpyxl
import pandas as pd
import shutil
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from openpyxl import Workbook

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        
        # Create four frames
        self.frame1 = tk.Frame(root, bg="lightblue", bd=2, relief=tk.RIDGE)
        self.frame2 = tk.Frame(root, bg="lightgreen", bd=2, relief=tk.RIDGE)
        self.frame3 = tk.Frame(root, bg="#d8bfd8", bd=2, relief=tk.RIDGE)  # Changed color to light purple
        self.frame4 = tk.Frame(root, bg="lightcoral", bd=2, relief=tk.RIDGE)
        
        # Pack frames to fill the window and equally distribute vertically and horizontally
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")
        self.frame3.grid(row=1, column=0, sticky="nsew")
        self.frame4.grid(row=1, column=1, sticky="nsew")
        
        # Configure grid weights to make all frames equally sized
        for i in range(2):  # Iterate over rows
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)

        # Create Student Details Section in Frame 1
        self.create_student_details_section()

        # Create Contact Information Section in Frame 1
        self.create_contact_information_section()

        # Create Personal Information Section in Frame 1
        self.create_personal_information_section()

        # Create Qualification Section in Frame 1
        self.create_qualification_section()

        # Create Fee Details Section in Frame 1
        self.create_fee_details_section()

        # Create Teacher Reviews Section in Frame 3
        self.create_teacher_reviews_section()

        #Create Happiest Moment Section In Frame 4
        self.create_happiest_moment_section()

        #Create Future Plan Section In Frame 4
        self.create_future_plan_section()

        #Create Suggestion Section In Frame 4
        self.create_suggestion_section()

        #Create Expectation Section In Frame 4
        self.create_expectation_section()

        #Create How Do Get Know About Us Section In Frame 4
        self.create_how_do_get_know_about_us_section()

        #Create Future Plan Section In Frame 2
        self.create_treeview_section()

        #Create Button In Frame 1
        self.create_buttons()

    def create_student_details_section(self):
        # Label for Student Details
        ttk.Label(self.frame1, text="Student Details", font=("Arial", 14, "bold"),background="lightblue").place(x=10, y=10)
        
        # Labels and Entry widgets for Student Details
        ttk.Label(self.frame1, text="Name:",background="lightblue").place(x=10, y=40)
        self.name_entry = ttk.Entry(self.frame1)
        self.name_entry.place(x=130, y=40)

        ttk.Label(self.frame1, text="ID:",background="lightblue").place(x=10, y=70)
        self.id_entry = ttk.Entry(self.frame1)
        self.id_entry.place(x=130, y=70)

        ttk.Label(self.frame1, text="Sex:",background="lightblue").place(x=10, y=100)
        self.sex_combobox = ttk.Combobox(self.frame1, values=["Male", "Female"])
        self.sex_combobox.place(x=130, y=100)

        ttk.Label(self.frame1, text="Age:",background="lightblue").place(x=10, y=130)
        self.age_entry = ttk.Entry(self.frame1)
        self.age_entry.place(x=130, y=130)

        ttk.Label(self.frame1, text="Joining Date:",background="lightblue").place(x=10, y=160)
        self.joining_date_entry = DateEntry(self.frame1, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.joining_date_entry.place(x=130, y=160)

        ttk.Label(self.frame1, text="Faculty Name:",background="lightblue").place(x=10, y=190)
        self.faculty_name_combobox = ttk.Combobox(self.frame1, values=["Livewire", "Cadd Center"])
        self.faculty_name_combobox.place(x=130, y=190)

        ttk.Label(self.frame1, text="Course Name:",background="lightblue").place(x=10, y=220)
        self.course_name_entry = ttk.Entry(self.frame1)
        self.course_name_entry.place(x=130, y=220)

        ttk.Label(self.frame1, text="Teacher Name:",background="lightblue").place(x=10, y=250)
        self.teacher_name_entry = ttk.Entry(self.frame1)
        self.teacher_name_entry.place(x=130, y=250)

    def create_contact_information_section(self):
        # Label for Contact Information
        ttk.Label(self.frame1, text="Contact Information", font=("Arial", 14, "bold"),background="lightblue").place(x=300, y=10)
        
        # Labels and Entry widgets for Contact Information
        ttk.Label(self.frame1, text="Phone Number:",background="lightblue").place(x=300, y=40)
        self.phone_number_entry = ttk.Entry(self.frame1)
        self.phone_number_entry.place(x=420, y=40)

        ttk.Label(self.frame1, text="E-mail:",background="lightblue").place(x=300, y=70)
        self.email_entry = ttk.Entry(self.frame1)
        self.email_entry.place(x=420, y=70)

        ttk.Label(self.frame1, text="Address:",background="lightblue").place(x=300, y=100)
        self.address_entry = ttk.Entry(self.frame1)
        self.address_entry.place(x=420, y=100)

    def create_personal_information_section(self):
        # Label for Personal Information
        ttk.Label(self.frame1, text="Personal Information", font=("Arial", 14, "bold"),background="lightblue").place(x=10, y=280)
        
        # Labels and Entry widgets for Personal Information
        ttk.Label(self.frame1, text="Father's Name:",background="lightblue").place(x=10, y=310)
        self.father_name_entry = ttk.Entry(self.frame1)
        self.father_name_entry.place(x=130, y=310)

        ttk.Label(self.frame1, text="Mother's Name:",background="lightblue").place(x=10, y=340)
        self.mother_name_entry = ttk.Entry(self.frame1)
        self.mother_name_entry.place(x=130, y=340)

        ttk.Label(self.frame1, text="Skills:",background="lightblue").place(x=10, y=370)
        self.skills_combobox = ttk.Combobox(self.frame1, values=["Programming", "Design", "Communication"])
        self.skills_combobox.place(x=130, y=370)

    def create_qualification_section(self):
        # Label for Qualification
        ttk.Label(self.frame1, text="Qualification", font=("Arial", 14, "bold"),background="lightblue").place(x=350, y=150)
        
        # Combobox for Qualification
        self.qualification_combobox = ttk.Combobox(self.frame1, values=["10th pass","12th Pass","Bachelor's Degree", "Master's Degree", "Ph.D.", "Certification"])
        self.qualification_combobox.place(x=340, y=180)

    def create_fee_details_section(self):
        # Label for Fee Details
        ttk.Label(self.frame1, text="Fee Details", font=("Arial", 14, "bold"),background="lightblue").place(x=350, y=220)
        
        # Labels and Entry widgets for Fees
        ttk.Label(self.frame1, text="Total Fee:",background="lightblue").place(x=300, y=250)
        self.total_fee_entry = ttk.Entry(self.frame1)
        self.total_fee_entry.place(x=420, y=250)

        ttk.Label(self.frame1, text="Paid:",background="lightblue").place(x=300, y=280)
        self.paid_entry = ttk.Entry(self.frame1)
        self.paid_entry.place(x=420, y=280)

        ttk.Label(self.frame1, text="Balance:",background="lightblue").place(x=300, y=310)
        self.balance_entry = ttk.Entry(self.frame1)
        self.balance_entry.place(x=420, y=310)

    def create_teacher_reviews_section(self):
        # Label for Teacher Reviews
        ttk.Label(self.frame3, text="Teacher Reviews", font=("Arial", 14, "bold"),background="#d8bfd8").place(x=280, y=10)
        
        # Textboxes for positive and negative points
        ttk.Label(self.frame3, text="Positive Points:", font=("Arial", 10, "bold"),background="#d8bfd8").place(x=110, y=40)
        self.point1_text_area = tk.Text(self.frame3, height=3, width=40)
        self.point1_text_area.place(x=10, y=70)

        self.point2_text_area = tk.Text(self.frame3, height=3, width=40)
        self.point2_text_area.place(x=10, y=130)

        self.point3_text_area = tk.Text(self.frame3, height=3, width=40)
        self.point3_text_area.place(x=10, y=190)

        self.point4_text_area = tk.Text(self.frame3, height=3, width=40)
        self.point4_text_area.place(x=10, y=250)

        ttk.Label(self.frame3, text="Negative Points:", font=("Arial", 10, "bold"),background="#d8bfd8").place(x=500, y=40)
        self.neg_point1_text_area = tk.Text(self.frame3, height=3, width=40)
        self.neg_point1_text_area.place(x=400, y=70)

        self.neg_point2_text_area = tk.Text(self.frame3, height=3, width=40)
        self.neg_point2_text_area.place(x=400, y=130)

        self.neg_point3_text_area = tk.Text(self.frame3, height=3, width=40)
        self.neg_point3_text_area.place(x=400, y=190)

        self.neg_point4_text_area = tk.Text(self.frame3, height=3, width=40)
        self.neg_point4_text_area.place(x=400, y=250)

    def create_happiest_moment_section(self):
        # Label for Happiest Moment
        ttk.Label(self.frame4, text="|| Happiest Moment ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=90, y=10)
        
        # Textbox for Happiest Moment
        ttk.Label(self.frame4, text="Describe your happiest moment:", font=("Arial", 10, "bold"),background="lightcoral").place(x=70, y=40)
        self.happiest_moment_text_area = tk.Text(self.frame4, height=5, width=40)
        self.happiest_moment_text_area.place(x=10, y=70)

    def create_future_plan_section(self):
        # Label for Future Plan
        ttk.Label(self.frame4, text="|| Future Plan ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=120, y=170)
        
        # Textbox for Future Plan
        ttk.Label(self.frame4, text="Describe your future plan:", font=("Arial", 10, "bold"),background="lightcoral").place(x=90, y=200)
        self.future_plan_text_area = tk.Text(self.frame4, height=5, width=40)
        self.future_plan_text_area.place(x=10, y=230)

    def create_suggestion_section(self):
        # Label for Suggestion
        ttk.Label(self.frame4, text="|| Suggestions ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=500, y=10)
        
        # Textbox for Suggestion
        ttk.Label(self.frame4, text="Any suggestions:", font=("Arial", 10, "bold"),background="lightcoral").place(x=505, y=40)
        self.suggestion_text_area = tk.Text(self.frame4, height=5, width=40)
        self.suggestion_text_area.place(x=400, y=70)

    def create_expectation_section(self):
        # Label for Expectation
        ttk.Label(self.frame4, text="|| Expectation ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=505, y=170)
        
        # Textbox for Expectation
        ttk.Label(self.frame4, text="Describe your expectation:", font=("Arial", 10, "bold"),background="lightcoral").place(x=480, y=200)
        self.expectation_text_area = tk.Text(self.frame4, height=5, width=40)
        self.expectation_text_area.place(x=400, y=230)
    
    def create_how_do_get_know_about_us_section(self):
        # Label for About Us
        ttk.Label(self.frame4, text="|| How did you hear about us? ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=250, y=330)

        # Dropdown Box for About Us
        about_us_values = ["Word of Mouth", "Online Search", "Social Media", "Event", "Newspaper", "Other"]
        self.about_us_dropdown = ttk.Combobox(self.frame4, values=about_us_values, width=30,height=10)
        self.about_us_dropdown.place(x=280, y=360)
    
    def create_treeview_section(self):
        # Label For Student Records(Treeview in Frame 2)
        ttk.Label(self.frame2, text="Students Records", font=("Arial", 14, "bold"),background="lightgreen").place(x=300, y=10)

        # Create Treeview widget
        self.treeview = ttk.Treeview(self.frame2, columns=("Name", "ID", "Sex", "Age", "Joining Date", "Faculty Name", "Course Name", "Teacher Name"), show="headings")
        self.treeview.place(x=10, y=50, width=720, height=340)

        # Create style for column headings
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  # Set font for column headings


        # Add columns
        self.treeview.heading("Name", text="Name", anchor=tk.CENTER)
        self.treeview.heading("ID", text="ID", anchor=tk.CENTER)
        self.treeview.heading("Sex", text="Sex", anchor=tk.CENTER)
        self.treeview.heading("Age", text="Age", anchor=tk.CENTER)
        self.treeview.heading("Joining Date", text="Joining Date", anchor=tk.CENTER)
        self.treeview.heading("Faculty Name", text="Faculty Name", anchor=tk.CENTER)
        self.treeview.heading("Course Name", text="Course Name", anchor=tk.CENTER)
        self.treeview.heading("Teacher Name", text="Teacher Name", anchor=tk.CENTER)

        # Add scrollbars
        x_scrollbar = ttk.Scrollbar(self.frame2, orient="horizontal", command=self.treeview.xview)
        x_scrollbar.place(x=10, y=390, width=720)
        self.treeview.configure(xscrollcommand=x_scrollbar.set)

        y_scrollbar = ttk.Scrollbar(self.frame2, orient="vertical", command=self.treeview.yview)
        y_scrollbar.place(x=730, y=50, height=340)
        self.treeview.configure(yscrollcommand=y_scrollbar.set)

    def create_buttons(self):
        # Calculate Button
        ttk.Button(self.frame1, text="Calculate",command=self.calculate_balance).place(x=430, y=350, width=100, height=30)

        # Save Button
        ttk.Button(self.frame1, text="Save",command=self.save_data).place(x=650, y=60, width=100, height=30)
        
        # Edit Button
        ttk.Button(self.frame1, text="Edit").place(x=650, y=100, width=100, height=30)

        # Delete Button
        ttk.Button(self.frame1, text="Delete",command=self.delete_student).place(x=650, y=140, width=100, height=30)

        # Search Button
        ttk.Button(self.frame1, text="Search").place(x=650, y=180, width=100, height=30)

        # Excel Button
        ttk.Button(self.frame1, text="Clear").place(x=650, y=220, width=100, height=30)

        # Refresh Button
        ttk.Button(self.frame1, text="Refresh").place(x=650, y=260, width=100, height=30)

        # Clear Button
        ttk.Button(self.frame1, text="Exit").place(x=650, y=300, width=100, height=30)
    def calculate_balance(self):
        try:
            total_fee = float(self.total_fee_entry.get())
            paid_fee = float(self.paid_entry.get())
            balance = total_fee - paid_fee
            self.balance_entry.configure(state='normal')
            self.balance_entry.delete(0, tk.END)
            self.balance_entry.insert(0, f"{balance:.2f}")
            self.balance_entry.configure(state='readonly')
            return True
        except ValueError:
            # Check if entries contain alphabetic characters or symbols
            if any(char.isalpha() or not char.isdigit() for char in self.total_fee_entry.get() + self.paid_entry.get()):
                messagebox.showerror("Error", "Please enter valid numeric values for Total Fee and Paid Fee.")
            return False
        
    def save_data(self):
        # Get data from all entry fields and text areas
        data = {
            'name': self.name_entry.get(),
            'id': self.id_entry.get(),
            'sex': self.sex_combobox.get(),
            'age' : self.age_entry.get(),
            'joining_date': self.joining_date_entry.get_date(),
            'faculty_name': self.faculty_name_combobox.get(),
            'course_name': self.course_name_entry.get(),
            'teacher_name': self.teacher_name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'email': self.email_entry.get(),
            'address': self.address_entry.get(),
            'father_name': self.father_name_entry.get(),
            'mother_name': self.mother_name_entry.get(),
            'skills': self.skills_combobox.get(),
            'qualification': self.qualification_combobox.get(),
            'total_fee': self.total_fee_entry.get(),
            'paid': self.paid_entry.get(),
            'balance': self.balance_entry.get(),
            'positive_point1': self.point1_text_area.get("1.0", tk.END).strip() or "No DATA",
            'positive_point2': self.point2_text_area.get("1.0", tk.END).strip() or "No DATA",
            'positive_point3': self.point3_text_area.get("1.0", tk.END).strip() or "No DATA",
            'positive_point4': self.point4_text_area.get("1.0", tk.END).strip() or "No DATA",
            'negative_point1': self.neg_point1_text_area.get("1.0", tk.END).strip() or "No DATA",
            'negative_point2': self.neg_point2_text_area.get("1.0", tk.END).strip() or "No DATA",
            'negative_point3': self.neg_point3_text_area.get("1.0", tk.END).strip() or "No DATA",
            'negative_point4': self.neg_point4_text_area.get("1.0", tk.END).strip() or "No DATA",
            'future_plan': self.future_plan_text_area.get("1.0", tk.END).strip() or "No DATA",
            'happiest_moment': self.happiest_moment_text_area.get("1.0", tk.END).strip() or "No DATA",
            'suggestions': self.suggestion_text_area.get("1.0", tk.END).strip() or "No DATA",
            'expectations': self.expectation_text_area.get("1.0", tk.END).strip() or "No DATA",
            'how_know_about_us': self.about_us_dropdown.get() or "No DATA"
        }

        # Ask for confirmation before saving
        confirm_save = messagebox.askyesno("Confirm Save", "Do you want to save the data?")
        if confirm_save:
            # Save data to the database
            self.save_to_database(data)
            
            messagebox.showinfo("Info", "Data saved successfully.")
        else:
            messagebox.showinfo("Info", "Data not saved.")

        # Save data to the database
        self.save_to_database(data)

    def save_to_database(self, data):
        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Combine script directory with the database file name
        db_file_path = os.path.join(script_dir, 'Students_Records_DB_File.db')

        # Connect to SQLite database or create a new one
        connection = sqlite3.connect(db_file_path)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # Create the Students table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                sex TEXT,
                age TEXT,
                joining_date TEXT,
                faculty_name TEXT,
                course_name TEXT,
                teacher_name TEXT,
                phone_number TEXT,
                email TEXT,
                address TEXT,
                father_name TEXT,
                mother_name TEXT,
                skills TEXT,
                qualification TEXT,
                total_fee TEXT,
                paid TEXT,
                balance TEXT,
                positive_point1 TEXT,
                positive_point2 TEXT,
                positive_point3 TEXT,
                positive_point4 TEXT,
                negative_point1 TEXT,
                negative_point2 TEXT,
                negative_point3 TEXT,
                negative_point4 TEXT,
                future_plan TEXT,
                happiest_moment TEXT,
                suggestions TEXT,
                expectations TEXT,
                how_know_about_us TEXT
            )
        ''')
        try:
            # Insert the data into the Students table
            cursor.execute('''
            INSERT INTO Students (
                name, id, sex, age, joining_date, faculty_name, course_name, teacher_name,
                phone_number, email, address, father_name, mother_name, skills,
                qualification, total_fee, paid, balance, positive_point1, positive_point2,
                positive_point3, positive_point4, negative_point1, negative_point2,
                negative_point3, negative_point4, future_plan, happiest_moment,
                suggestions, expectations, how_know_about_us
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,? ,? ,?)
        ''', tuple(data.values()))


            # Commit changes and close the connection
            connection.commit()
            # Show success message
            messagebox.showinfo("Success", "Data saved successfully!")

        except Exception as e:
            # Handle any exceptions (e.g., database errors)
            messagebox.showerror("Error", f"Failed to save data. Error: {str(e)}")

        finally:
            # Close the connection
            connection.close()

    def delete_student(self):
        # Get the student ID to delete
        student_id = self.id_entry.get()

        # Check if the student record exists in the SQLite database
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
        student_record = cursor.fetchone()
        conn.close()

        if student_record:
            # Ask for confirmation
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete student data?")

            if confirmation:
                # Delete student from SQLite database
                conn = sqlite3.connect('students.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Student information deleted successfully!")
        else:
            messagebox.showerror("Error", "Student record not found in the database!")

    def clear_fields(self):
        # Clear all entry fields and text areas
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.sex_combobox.set('')
        self.age_entry.delete(0,tk.END)
        #joining_date is at bottom
        self.faculty_name_combobox.delete(0, tk.END)
        self.course_name_entry.delete(0, tk.END)
        self.teacher_name_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.father_name_entry.delete(0, tk.END)
        self.mother_name_entry.delete(0, tk.END)
        self.skills_combobox.set('')
        self.qualification_combobox.set('')
        self.total_fee_entry.delete(0, tk.END)
        self.paid_entry.delete(0, tk.END)
        self.balance_entry.delete(0, tk.END)

        # Clear text areas
        self.point1_text_area.delete(1.0, tk.END)
        self.point2_text_area.delete(1.0, tk.END)
        self.point3_text_area.delete(1.0, tk.END)
        self.point4_text_area.delete(1.0, tk.END)
        self.neg_point1_text_area.delete(1.0, tk.END)
        self.neg_point2_text_area.delete(1.0, tk.END)
        self.neg_point3_text_area.delete(1.0, tk.END)
        self.neg_point4_text_area.delete(1.0, tk.END)
        self.future_plan_text_area.delete(1.0, tk.END)
        self.happiest_moment_text_area.delete(1.0, tk.END)
        self.suggestion_text_area.delete(1.0, tk.END)
        self.expectation_text_area.delete(1.0, tk.END)

        # Reset about_us_dropdown to default
        self.about_us_dropdown.set('')
        # Clear joining date entry
        if hasattr(self.joining_date_entry, 'set_date'):
            self.joining_date_entry.set_date(None)  # or set_date('')

    def search_student(self):
        # Get the student ID from the entry field
        student_id = self.id_entry.get()

        # Check if the ID is provided
        if not student_id:
            messagebox.showerror("Error", "Please enter a student ID to search.")
            return

        # Get the data from the database for the provided ID
        student_data = self.get_student_data(student_id)

        # Check if the student with the provided ID exists
        if student_data:
            # Update entry fields and text areas with the student's data
            name = student_data[1]  # Assuming 'name' is the second column in your Students table
            sex = student_data[2]
            joining_date = student_data[3]
            faculty_name = student_data[4]
            course_name = student_data[5]
            teacher_name = student_data[6]
            phone_number = student_data[7]
            email = student_data[8]
            address = student_data[9]
            father_name = student_data[10]
            mother_name = student_data[11]
            skills = student_data[12]
            qualification = student_data[13]
            total_fee = student_data[14]
            paid = student_data[15]
            balance = student_data[16]
            positive_point1 = student_data[17]
            positive_point2 = student_data[18]
            positive_point3 = student_data[19]
            positive_point4 = student_data[20]
            negative_point1 = student_data[21]
            negative_point2 = student_data[22]
            negative_point3 = student_data[23]
            negative_point4 = student_data[24]
            future_plan = student_data[25]
            happiest_moment = student_data[26]
            suggestions = student_data[27]
            expectations = student_data[28]
            how_know_about_us = student_data[29]
            
            # Update entry fields and text areas with the student's data
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

            self.sex_combobox.set(sex)

           #Joining Date Is at End Of function
            self.faculty_name_combobox.delete(0, tk.END)
            self.faculty_name_combobox.insert(0, faculty_name)
            self.course_name_entry.delete(0, tk.END)
            self.course_name_entry.insert(0, course_name)
            self.teacher_name_entry.delete(0, tk.END)
            self.teacher_name_entry.insert(0, teacher_name)
            self.phone_number_entry.delete(0, tk.END)
            self.phone_number_entry.insert(0, phone_number)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, email)
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, address)
            self.father_name_entry.delete(0, tk.END)
            self.father_name_entry.insert(0, father_name)
            self.mother_name_entry.delete(0, tk.END)
            self.mother_name_entry.insert(0, mother_name)
            self.skills_combobox.set(skills)
            self.qualification_combobox.set(qualification)
            self.total_fee_entry.delete(0, tk.END)
            self.total_fee_entry.insert(0, total_fee)
            self.paid_entry.delete(0, tk.END)
            self.paid_entry.insert(0, paid)
            self.balance_entry.delete(0, tk.END)
            self.balance_entry.insert(0, balance)
            
            #all Text box 
            self.point1_text_area.delete("1.0", tk.END)
            self.point1_text_area.insert(tk.END, positive_point1)

            self.point2_text_area.delete("1.0", tk.END)
            self.point2_text_area.insert(tk.END, positive_point2)

            self.point3_text_area.delete("1.0", tk.END)
            self.point3_text_area.insert(tk.END, positive_point3)

            self.point4_text_area.delete("1.0", tk.END)
            self.point4_text_area.insert(tk.END, positive_point4)

            self.neg_point1_text_area.delete("1.0", tk.END)
            self.neg_point1_text_area.insert(tk.END, negative_point1)

            self.neg_point2_text_area.delete("1.0", tk.END)
            self.neg_point2_text_area.insert(tk.END, negative_point2)

            self.neg_point3_text_area.delete("1.0", tk.END)
            self.neg_point3_text_area.insert(tk.END, negative_point3)

            self.neg_point4_text_area.delete("1.0", tk.END)
            self.neg_point4_text_area.insert(tk.END, negative_point4)

            self.future_plan_text_area.delete("1.0", tk.END)
            self.future_plan_text_area.insert(tk.END, future_plan)

            self.happiest_moment_text_area.delete("1.0", tk.END)
            self.happiest_moment_text_area.insert(tk.END, happiest_moment)

            self.suggestion_text_area.delete("1.0", tk.END)
            self.suggestion_text_area.insert(tk.END, suggestions)

            self.expectation_text_area.delete("1.0", tk.END)
            self.expectation_text_area.insert(tk.END, expectations)

            self.about_us_dropdown.set(how_know_about_us)

            self.joining_date_entry.set_date(joining_date)

        else:
            messagebox.showinfo("Info", f"No student found with ID: {student_id}")

    def get_student_data(self, student_id):
        # Get the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Combine script directory with the database file name
        db_file_path = os.path.join(script_dir, 'Students_Records_DB_File.db')

        # Connect to SQLite database
        connection = sqlite3.connect(db_file_path)
        cursor = connection.cursor()

        # Query to get student data by ID
        cursor.execute('''
            SELECT * FROM Students
            WHERE id = ?
        ''', (student_id,))

        # Fetch the result
        student_data = cursor.fetchone()

        # Close the connection
        connection.close()

        # Return the student data
        return student_data
    
    def edit_student(self):
        # Get the student ID from the entry field
        student_id = self.id_entry.get()

        # Check if the ID is provided
        if not student_id:
            messagebox.showerror("Error", "Please enter a student ID to edit.")
            return

        # Get the data from the database for the provided ID
        student_data = self.get_student_data(student_id)

        # Check if the student with the provided ID exists
        if student_data:
            # Ask for confirmation
            confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to edit student information?", icon='warning')

            if confirmation == 'yes':
                # Update the student's data in the database
                updated_data = {
                    'name': self.name_entry.get(),
                    'sex': self.sex_combobox.get(),
                    'age' : self.age_entry.get(),
                    'joining_date': self.joining_date_entry.get_date(),
                    'faculty_name': self.faculty_name_combobox.get(),
                    'course_name': self.course_name_entry.get(),
                    'teacher_name': self.teacher_name_entry.get(),
                    'phone_number': self.phone_number_entry.get(),
                    'email': self.email_entry.get(),
                    'address': self.address_entry.get(),
                    'father_name': self.father_name_entry.get(),
                    'mother_name': self.mother_name_entry.get(),
                    'skills': self.skills_combobox.get(),
                    'qualification': self.qualification_combobox.get(),
                    'total_fee': self.total_fee_entry.get(),
                    'paid': self.paid_entry.get(),
                    'positive_point1': self.point1_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'positive_point2': self.point2_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'positive_point3': self.point3_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'positive_point4': self.point4_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'negative_point1': self.neg_point1_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'negative_point2': self.neg_point2_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'negative_point3': self.neg_point3_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'negative_point4': self.neg_point4_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'future_plan': self.future_plan_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'happiest_moment': self.happiest_moment_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'suggestions': self.suggestion_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'expectations': self.expectation_text_area.get("1.0", tk.END).strip() or "No DATA",
                    'how_know_about_us': self.about_us_dropdown.get() or "No DATA"
                }
 
                # Update data in the database
                self.update_student_data(student_id, updated_data)

                messagebox.showinfo("Info", f"Student data updated successfully.")

            else:
                messagebox.showinfo("Info", "Student information not edited.")

        else:
            messagebox.showinfo("Info", f"No student found with ID: {student_id}")

    def update_student_data(self, student_id, updated_data):
        # Connect to SQLite database
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

        # Update the data in the Students table
        cursor.execute('''
            UPDATE Students
            SET
                name = ?,
                sex = ?,
                age =?,
                joining_date = ?,
                faculty_name = ?,
                course_name = ?,
                teacher_name = ?,
                phone_number = ?,
                email = ?,
                address = ?,
                father_name = ?,
                mother_name = ?,
                skills = ?,
                qualification = ?,
                total_fee = ?,
                paid = ?,
                positive_point1 = ?,
                positive_point2 = ?,
                positive_point3 = ?,
                positive_point4 = ?,
                negative_point1 = ?,
                negative_point2 = ?,
                negative_point3 = ?,
                negative_point4 = ?,
                future_plan = ?,
                happiest_moment = ?,
                suggestions = ?,
                expectations = ?,
                how_know_about_us = ?
            WHERE id = ?
        ''', tuple(updated_data.values()) + (student_id,))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
