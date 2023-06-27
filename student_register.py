# Ask the user how many students are registering
num_students = int(input("Enter the number of students registering: "))

# Open the file in write mode
with open("reg_form.txt", "w") as file:
    # Create a for loop that runs for the number of students
    for i in range(num_students):
        # Ask each student to enter their ID number
        student_id = input(f"Enter the ID number for student {i+1}: ")
        
        # Write the ID number to the file
        file.write(f"Student ID: {student_id}\n")
        file.write("Signature: _________\n")
        file.write("------------------------\n")

print("Registration form created successfully!")
