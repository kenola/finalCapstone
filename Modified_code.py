import datetime
import os
# Function to create login credentials
def create_credentials():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    with open("credentials.txt", "w") as file:
        file.write(f"{username},{password}")
    print("Credentials created successfully.")

# Function to check if login credentials are valid
def validate_credentials():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("credentials.txt", "r") as file:
        stored_username, stored_password = file.read().split(",")
        if username == stored_username and password == stored_password:
            return True
    return False


# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


# Function to register a new user
def reg_user():
    new_username = input("New Username: ")

        # - Request input of a new password
    new_password = input("New Password: ")

        # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
            print("Passwords do no match")
# Function to add a new task
def add_task():
    username = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (in the format DD MMM YYYY): ")
    completed = "No"
    with open("tasks.txt", "a") as file:
        file.write(f"\n{title},{username},{due_date},{completed},{description}")
    print("Task added successfully.")

# Function to view all tasks
def view_all():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(task.strip())

# Function to view tasks assigned to a specific user
def view_mine():
    username = input("Enter your username: ")
    tasks = []

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    print("Tasks assigned to you:")
    for i, task in enumerate(tasks):
        if username in task:
            print(f"{i+1}. {task.strip()}")

    choice = input("Enter the number of the task you want to select (or enter -1 to return to the main menu): ")
    if choice == "-1":
        return
    else:
        print("No task found.")

    try:
        task_index = int(choice) - 1
        print(f"Task index: {task_index}")
        print(f"Number of tasks: {len(tasks)}")

        # Check if the task index is out of bounds
        if task_index < 0 or task_index >= len(tasks):
            print("Task index is out of bounds. Task modification canceled.")
            return

        selected_task = tasks[task_index].strip().split(";")
        
        if len(selected_task) < 4:
            print("Invalid task format. Task modification canceled.")
            return

        assigned_to = selected_task[1]
        due_date = selected_task[2]
        completed = selected_task[3]

        print("Selected Task:")
        print(f"Task: {selected_task[0]}")
        print(f"Assigned to: {assigned_to}")
        print(f"Due Date: {due_date}")
        print(f"Completed: {completed}")

        edit_choice = input("Enter 'm' to mark the task as complete, 'e' to edit the task, or any other key to cancel: ")
        if edit_choice == "m":
            if completed.lower() != "yes":
                selected_task[3] = "Yes"
                tasks[task_index] = ";".join(selected_task) + "\n"
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task marked as complete.")
            else:
                print("Task is already marked as complete and cannot be modified.")
        elif edit_choice == "e":
            if completed.lower() != "yes":
                new_assigned_to = input("Enter new username for the task: ")
                new_due_date = input("Enter new due date for the task: ")
                selected_task[1] = new_assigned_to
                selected_task[2] = new_due_date
                tasks[task_index] = ";".join(selected_task) + "\n"
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task edited successfully.")
            else:
                print("Task is already marked as complete and cannot be modified.")
        else:
            print("Task modification canceled.")

    except ValueError:
        print("Invalid input. Task modification canceled.")



# Function to generate reports
import datetime

import datetime

def generate_reports():
    tasks = []
    users = []

    # Read the tasks from the file into a list
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # Read the users from the file into a list
    with open("user.txt", "r") as file:
        users = file.readlines()

    # Generate task overview report
    total_tasks = len(tasks)
    completed_tasks = sum("Yes" in task for task in tasks)
    uncompleted_tasks = total_tasks - completed_tasks
    overdue_tasks = sum(
        "No" in task and len(task.split(";")) >= 5 and datetime.datetime.strptime(task.split(";")[3].strip(), "%Y-%m-%d") < datetime.datetime.now()
        for task in tasks
    )
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    with open("task_overview.txt", "w") as file:
        file.write("Task Overview\n")
        file.write(f"Total tasks: {total_tasks}\n")
        file.write(f"Completed tasks: {completed_tasks}\n")
        file.write(f"Uncompleted tasks: {uncompleted_tasks}\n")
        file.write(f"Overdue tasks: {overdue_tasks}\n")
        file.write(f"Incomplete tasks percentage: {incomplete_percentage}%\n")
        file.write(f"Overdue tasks percentage: {overdue_percentage}%\n")

    # Generate user overview report
    total_users = len(users)
    user_tasks = [task for task in tasks if task.split(";")[1] != "-"]
    user_task_count = {}
    user_task_completion = {}

    for user in users:
        username = user.split(";")[0]
        user_task_count[username] = sum(username in task for task in user_tasks)
        user_task_completion[username] = sum(username in task and "Yes" in task for task in user_tasks)

    with open("user_overview.txt", "w") as file:
        file.write("User Overview\n")
        file.write(f"Total users: {total_users}\n")
        file.write(f"Total tasks: {total_tasks}\n")

        for user in users:
            username = user.split(";")[0]
            assigned_tasks = user_task_count.get(username, 0)
            assigned_percentage = (assigned_tasks / total_tasks) * 100

            if assigned_tasks == 0:
                completed_percentage = 0
            else:
                completed_percentage = (user_task_completion.get(username, 0) / assigned_tasks) * 100

            incomplete_percentage = 100 - completed_percentage

            file.write(f"\nUser: {username}\n")
            file.write(f"Assigned tasks: {assigned_tasks}\n")
            file.write(f"Percentage of tasks assigned: {assigned_percentage}%\n")
            file.write(f"Percentage of tasks completed: {completed_percentage}%\n")
            file.write(f"Percentage of tasks incomplete: {incomplete_percentage}%\n")
            file.write(f"Percentage of overdue tasks: {overdue_percentage}%\n")

    print("Reports generated successfully.")



# Function to display statistics
def display_statistics():
    try:
        with open("task_overview.txt", "r") as task_file, open("user_overview.txt", "r") as user_file:
            task_data = task_file.read()
            user_data = user_file.read()

            print("Task Overview:")
            print(task_data)
            print("User Overview:")
            print(user_data)

    except FileNotFoundError:
        print("Reports have not been generated yet. Please select 'gr' to generate the reports first.")


    # Main menu function
def main_menu():
    while True:
        print("Welcome to the Task Manager!")
        print("Please select an option:")
        print("r - Register user")
        print("a - Add task")
        print("va - View all tasks")
        print("vm - View my tasks")
        print("gr - Generate reports and display statistics")
        print("x - Exit")

        choice = input("Enter your choice: ")
        if choice == "r":
            reg_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all()
        elif choice == "vm":
            view_mine()
        elif choice == "gr":
            generate_reports()
            display_statistics()
        elif choice == "x":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
