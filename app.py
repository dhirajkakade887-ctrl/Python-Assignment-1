# Student Record and Academic Management System

# Initialize global data structures
students_db = {}  # Dictionary to store complete student profiles
departments_set = set()  # Set to store unique departments
subjects_set = set()  # Set to store unique subjects across courses
student_clubs = set()  # Set to track active student clubs


def add_student():
  """Adds a new student record integrating lists, tuples, sets, and dictionaries."""
  print("\n--- Add New Student Record ---")
  roll_number = input(
      "Enter Roll Number (e.g., R001) [Tuple identifier]: "
  ).strip()

  if roll_number in students_db:
    print("Error: Student with this roll number already exists!")
    return

  # Tuple for immutable unique identifiers and personal details
  reg_number = input("Enter Registration Number: ").strip()
  dob = input("Enter Date of Birth (DD-MM-YYYY): ").strip()
  identifier_tuple = (roll_number, reg_number, dob)

  # Strings for basic info
  name = input("Enter Student Name: ").strip()
  department = input("Enter Department: ").strip()
  departments_set.add(department)  # Adding to Set

  email = input("Enter Email ID: ").strip()
  address = input("Enter Address: ").strip()

  # Lists for subjects, marks, and attendance
  print("Enter Subjects (comma-separated):")
  subjects_input = input().strip()
  subject_list = [sub.strip() for sub in subjects_input.split(",")]
  for sub in subject_list:
    subjects_set.add(sub)  # Adding to Set

  marks_list = []
  print("Enter marks corresponding to each subject:")
  for sub in subject_list:
    while True:
      try:
        mark = float(input(f"Marks for {sub}: "))
        if 0 <= mark <= 100:
          marks_list.append(mark)
          break
        print("Marks should be between 0 and 100.")
      except ValueError:
        print("Invalid input. Please enter a valid number.")

  attendance_list = []
  print("Enter monthly attendance percentage (comma-separated for 6 months):")
  while True:
    try:
      att_input = input().strip()
      attendance_list = [float(a.strip()) for a in att_input.split(",")]
      if len(attendance_list) > 0:
        break
      print("Please enter at least one attendance entry.")
    except ValueError:
      print("Invalid input. Please enter numbers separated by commas.")

  # Dictionary to compile the complete profile
  student_profile = {
      "Identifiers": identifier_tuple,
      "Name": name,
      "Department": department,
      "Subjects": subject_list,
      "Marks": marks_list,
      "Attendance": attendance_list,
      "Contact": {"Email": email, "Address": address},
  }

  students_db[roll_number] = student_profile
  print(f"Success: Student {name} added successfully!")


def search_student():
  """Searches for a student by roll number."""
  print("\n--- Search Student ---")
  roll_number = input("Enter Roll Number to search: ").strip()

  if roll_number in students_db:
    profile = students_db[roll_number]
    print(f"\nRecord Found for Roll Number: {roll_number}")
    print(f"Name: {profile['Name']}")
    print(f"Department: {profile['Department']}")
    print(f"Registration Number: {profile['Identifiers'][1]}")
    print(f"Date of Birth: {profile['Identifiers'][2]}")
    print(f"Subjects & Marks: {dict(zip(profile['Subjects'], profile['Marks']))}")
    print(f"Attendance Records: {profile['Attendance']}")
    print(
        f"Contact - Email: {profile['Contact']['Email']}, Address:"
        f" {profile['Contact']['Address']}"
    )
  else:
    print("Error: Student record not found.")


def update_student():
  """Updates an existing student's information."""
  print("\n--- Update Student Record ---")
  roll_number = input("Enter Roll Number to update: ").strip()

  if roll_number not in students_db:
    print("Error: Student record not found.")
    return

  profile = students_db[roll_number]
  print(f"Updating record for: {profile['Name']}")
  print("1. Update Department")
  print("2. Update Marks")
  print("3. Update Contact Information")
  choice = input("Enter your choice (1-3): ").strip()

  if choice == "1":
    new_dept = input("Enter new Department: ").strip()
    profile["Department"] = new_dept
    departments_set.add(new_dept)
    print("Department updated successfully!")
  elif choice == "2":
    print("Current Subjects:", profile["Subjects"])
    new_marks = []
    for sub in profile["Subjects"]:
      mark = float(input(f"Enter new marks for {sub}: "))
      new_marks.append(mark)
    profile["Marks"] = new_marks
    print("Marks updated successfully!")
  elif choice == "3":
    profile["Contact"]["Email"] = input("Enter new Email: ").strip()
    profile["Contact"]["Address"] = input("Enter new Address: ").strip()
    print("Contact information updated successfully!")
  else:
    print("Invalid choice.")


def delete_student():
  """Deletes a student record using their roll number."""
  print("\n--- Delete Student Record ---")
  roll_number = input("Enter Roll Number to delete: ").strip()

  if roll_number in students_db:
    del students_db[roll_number]
    print(f"Success: Record for roll number {roll_number} has been deleted.")
  else:
    print("Error: Student record not found.")


def calculate_average_and_highest():
  """Calculates average marks and identifies the highest scorer."""
  print("\n--- Academic Performance Analysis ---")
  if not students_db:
    print("No student records available.")
    return

  highest_avg = -1
  top_student = ""

  for roll, profile in students_db.items():
    marks = profile["Marks"]
    if marks:
      avg = sum(marks) / len(marks)
      print(f"Student: {profile['Name']} ({roll}) - Average Marks: {avg:.2f}")
      if avg > highest_avg:
        highest_avg = avg
        top_student = profile["Name"]

  if top_student:
    print(
        f"\n Highest Scorer: {top_student} with an average of"
        f" {highest_avg:.2f} marks!"
    )


def list_by_department():
  """Lists students belonging to a specific department using set data."""
  print("\n--- List Students by Department ---")
  if not departments_set:
    print("No departments recorded yet.")
    return

  print("Available Departments:", list(departments_set))
  dept_query = input("Enter department name to filter: ").strip()

  found = False
  print(f"\nStudents in {dept_query}:")
  for roll, profile in students_db.items():
    if profile["Department"].lower() == dept_query.lower():
      print(f"- {profile['Name']} (Roll No: {roll})")
      found = True

  if not found:
    print("No students found in this department.")


def main_menu():
  """Main driving loop for the management system."""
  while True:
    print("\n==============================================")
    print("   STUDENT RECORD & ACADEMIC MANAGEMENT SYS   ")
    print("==============================================")
    print("1. Add New Student Record")
    print("2. Search Student by Roll Number")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Calculate Average Marks & Find Highest Scorer")
    print("6. List Students by Department")
    print("7. Total Student Count")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
      add_student()
    elif choice == "2":
      search_student()
    elif choice == "3":
      update_student()
    elif choice == "4":
      delete_student()
    elif choice == "5":
      calculate_average_and_highest()
    elif choice == "6":
      list_by_department()
    elif choice == "7":
      print(f"\nTotal Registered Students: {len(students_db)}")
    elif choice == "8":
      print("\nExiting system. Thank you!")
      break
    else:
      print("Invalid choice! Please select a valid option between 1 and 8.")


if __name__ == "__main__":
  main_menu()