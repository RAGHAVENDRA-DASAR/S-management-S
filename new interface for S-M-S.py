import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry  # Assuming you have installed tkcalendar

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
        happiest_moment_text_area = tk.Text(self.frame4, height=5, width=40)
        happiest_moment_text_area.place(x=10, y=70)

    def create_future_plan_section(self):
        # Label for Future Plan
        ttk.Label(self.frame4, text="|| Future Plan ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=120, y=170)
        
        # Textbox for Future Plan
        ttk.Label(self.frame4, text="Describe your future plan:", font=("Arial", 10, "bold"),background="lightcoral").place(x=90, y=200)
        future_plan_text_area = tk.Text(self.frame4, height=5, width=40)
        future_plan_text_area.place(x=10, y=230)

    def create_suggestion_section(self):
        # Label for Suggestion
        ttk.Label(self.frame4, text="|| Suggestions ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=500, y=10)
        
        # Textbox for Suggestion
        ttk.Label(self.frame4, text="Any suggestions:", font=("Arial", 10, "bold"),background="lightcoral").place(x=505, y=40)
        suggestion_text_area = tk.Text(self.frame4, height=5, width=40)
        suggestion_text_area.place(x=400, y=70)

    def create_expectation_section(self):
        # Label for Expectation
        ttk.Label(self.frame4, text="|| Expectation ||", font=("Arial", 14, "bold"),background="lightcoral").place(x=505, y=170)
        
        # Textbox for Expectation
        ttk.Label(self.frame4, text="Describe your expectation:", font=("Arial", 10, "bold"),background="lightcoral").place(x=480, y=200)
        expectation_text_area = tk.Text(self.frame4, height=5, width=40)
        expectation_text_area.place(x=400, y=230)
    
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
        ttk.Button(self.frame1, text="Calculate").place(x=430, y=350, width=100, height=30)

        # Save Button
        ttk.Button(self.frame1, text="Save").place(x=650, y=60, width=100, height=30)
        
        # Edit Button
        ttk.Button(self.frame1, text="Edit").place(x=650, y=100, width=100, height=30)

        # Delete Button
        ttk.Button(self.frame1, text="Delete").place(x=650, y=140, width=100, height=30)

        # Search Button
        ttk.Button(self.frame1, text="Search").place(x=650, y=180, width=100, height=30)

        # Excel Button
        ttk.Button(self.frame1, text="Clear").place(x=650, y=220, width=100, height=30)

        # Refresh Button
        ttk.Button(self.frame1, text="Refresh").place(x=650, y=260, width=100, height=30)

        # Clear Button
        ttk.Button(self.frame1, text="Exit").place(x=650, y=300, width=100, height=30)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
