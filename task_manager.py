#===============================================================================
#----  HEADER  ----------------------------------------------------------------- 
#===============================================================================

"""
    Description:  Task Manager
    Author:       Jozef Katina
    Email:        jozef.katina@outlook.com
    Date:         Fri February 10 2023

"""

#===============================================================================
#----  IMPORTING MODULES  ------------------------------------------------------
#===============================================================================

import os
from datetime import datetime

#===============================================================================
#----  DECLARING VARIABLES  ----------------------------------------------------
#===============================================================================

initial_login = True
path_current = os.path.dirname(__file__)   

#===============================================================================
#----  DEFINING FUNCTIONS ------------------------------------------------------
#===============================================================================

def login_user():

    real_user = False
    real_password = False

    while not real_user:
        user_x = input("Please enter your username: ")
        for i in range(0, len(users)):
            if users[i][0] == user_x:
                real_user = True
                if real_user:
                    while not real_password:
                        password = input("Please enter your password: ")
                        if users[i][1] == password:
                            real_password = True
                        if not real_password:
                            print(("\n\033[91mYour password is incorrect."
                                   "Please try again.\033[00m"))
        if not real_user:
            print("\n\033[91mYour username is incorrect. Please try again.\033[00m")
        else:
            print("\n\033[93mWelcome to Task Manager.\033[00m")
            print("Enter \"m\" at any time to return to the Menu.")
    return user_x
    

def reg_user():
    
    unique_username = False
    unique_password = False

    if user_name == "admin":
        while not unique_username:
            unique = True
            new_user = input("Please enter a new username:\t\t")
            if new_user == "m":
                break
            elif new_user == "":
                print("\n\033[91mPlease enter a valid username.\033[00m\n")
            else:
                for i in range(0, len(users)):
                    if users[i][0] == new_user:
                        print(("\n\033[91mThe username already exists." 
                               "Please enter a different username.\033[00m\n"))
                        unique = False
                if unique:
                    unique_username = True
        if new_user == "m":
            pass
        else:
            while not unique_password:
                new_pass_x = input("Please enter a password:\t\t")
                if new_pass_x == "":
                    print("\n\033[91mPlease enter a valid password.\033[00m\n")
                elif new_pass_x == "m":
                    break
                else:
                    new_pass_y = input("Please confirm your password:\t")
                    if new_pass_y == "m":
                        break
                    elif new_pass_x == new_pass_y:
                        unique_password = True
                        user.write(f"\n{new_user}, {new_pass_x}")
                        print((f"\n\033[93mA new user has been added!\nWith the username:"
                               f"\t{new_user}\n With the password:\t{new_pass_x}\033[00m"))
                    else:
                        print(("\n\033[91mPasswords do not match." 
                               "Please try again.\033[00m\n"))
        unique_password = False
    else:
        print("\n\033[91mOnly admin can register new users.\033[00m")


def add_task():

    task_information = []
    info_title = ["Username:\t", "Task Title:\t", "Description:\t", "Date Assigned:\t", 
                  "Due Date:\t", "Completed:\t"]
    skip = False

    for i in range(0, 6):
        while True:
            data = input(f"{info_title[i]}")
            if data == "":
                print("\n\033[91mInvalid input. Please try again.\033[00m\n")
            else:
                task_information.append(data)
                break
        if task_information[i] == "m":
            skip = True
            break
    if not skip:
        task.write((f"\n{task_information[0]}, {task_information[1]}, {task_information[2]}," 
                    f"{task_information[3]}, {task_information[4]}, {task_information[5]}"))
        print("\nA new task has been added")
        print("----------------------------------------------------")
        print("Username:\t" + task_information[0])
        print("Task Title:\t" + task_information[1])
        print("Description:\t" + task_information[2])
        print("Date Assigned:\t" + task_information[3])
        print("Due Date:\t" + task_information[4])
        print("Completed:\t" + task_information[5])
        print("----------------------------------------------------")
    
 
def view_all():

    for line in tasks:
        print("----------------------------------------------------")
        print("Username:\t" + line[0])
        print("Task Title:\t" + line[1])
        print("Description:\t" + line[2])
        print("Date Assigned:\t" + line[3])
        print("Due Date:\t" + line[4])
        print("Completed:\t" + line[5])
        print("----------------------------------------------------")

 
def view_mine():

    user_found = False
    my_tasks = []
    
    for i in range(0, len(tasks)):
        if user_name == tasks[i][0]:
            my_tasks.append(tasks[i])
            user_found = True
    if user_found:
        for i in range(0, len(my_tasks)):
            print(f"\nTask {i+1}")
            print("----------------------------------------------------")
            print("Username:\t" + my_tasks[i][0])
            print("Task Title:\t" + my_tasks[i][1])
            print("Description:\t" + my_tasks[i][2])
            print("Date Assigned:\t" + my_tasks[i][3])
            print("Due Date:\t" + my_tasks[i][4])
            print("Completed:\t" + my_tasks[i][5])
            print("----------------------------------------------------")
        while True:
            try:
                task_number = int(input("Please enter a task number to edit: "))
                if task_number == "m":
                    break
                elif task_number > 0 and task_number <= len(my_tasks):
                    for i in range(0, len(my_tasks)):
                        tasks.remove(my_tasks[i])
                    while True:
                        print("\nPlease choose an option:")
                        print("c - mark task as complete\ne - edit the task")
                        menu_choice = input()
                        if menu_choice == "c":
                            my_tasks[task_number-1][5] = "Yes"
                            print(f"\nTask {task_number} has been marked as complete.")
                            break
                        elif menu_choice == "m":
                            break
                        elif menu_choice == "e":
                            if my_tasks[task_number-1][5] == "Yes":
                                print("\nThe task has been completed. Unable to edit.")
                                break
                            else:
                                print("\nPlease enter the new 'Username' and 'Due Date'")
                                user_x = input("Please edit Username:\t")
                                due_date = input("Please edit Due Date:\t")
                                if user_x != "":
                                    my_tasks[task_number-1][0] = user_x
                                if due_date != "":
                                    my_tasks[task_number-1][4] = due_date
                                print("\nUpdated details:")
                                print("Username:\t" + my_tasks[task_number-1][0])
                                print("Due Date:\t" + my_tasks[task_number-1][4])
                                break
                        else:
                            print("\nUnrecognized input.")
                    task.seek(0)
                    task.truncate(0)
                    for i in range(0, len(my_tasks)):
                        tasks.append(my_tasks[i])
                    for i in range(0, len(tasks)):
                        task.write(", ".join(tasks[i]))
                        if i != len(tasks)-1:
                            task.write("\n")
                    break
                else:
                    print("\nThe selected task does not exist. Please try again.\n")
            except:
                print("\nNo task number entered. Please try again.\n")
    if not user_found:
        print("No tasks found for selected user.")
    

def generate_reports():
    
    if user_name == "admin":
        task_over_w = open(os.path.join(path_current, "task_overview.txt"), "w+")
        user_over_w = open(os.path.join(path_current, "user_overview.txt"), "w+")
        total_tasks = len(tasks)
        num_completed = 0
        num_incomplete = 0
        num_inc_overdue = 0
        per_incomplete = 0
        per_overdue = 0
        for i in range(0, len(tasks)):
            if tasks[i][5] == "Yes":
                num_completed += 1
            elif tasks[i][5] == "No":
                num_incomplete += 1
                task_date = datetime.strptime(tasks[i][4], '%d %b %Y')
                if datetime.date(datetime.now()) < task_date.date():
                    num_inc_overdue += 1
        if total_tasks == 0:
            per_incomplete = 0
            per_overdue = 0
        else:
            per_incomplete = round(100*num_incomplete/total_tasks)
            per_overdue = round(100*num_inc_overdue/total_tasks)
        task_over_w.write("~ Task Overview ~\n\n")
        task_over_w.write((f"Total Tasks:\t\t{total_tasks}\n"
                           f"Completed Tasks:\t{num_completed}\n"
                           f"Incomplete Tasks:\t{num_incomplete}\n"
                           f"Overdue Tasks:\t\t{num_inc_overdue}\n"
                           f"Portion Incomplete:\t{per_incomplete}%\n"
                           f"Portion Overdue:\t{per_overdue}%"))
        num_users = len(users)
        user_over_w.write("~ User Overview ~\n\n")
        user_over_w.write(f"Total Users:\t\t{num_users}\n")
        user_over_w.write(f"Total Tasks:\t\t{total_tasks}")
        for i in range(0, len(users)):
            num_tasks = 0
            num_completed = 0
            num_incomplete = 0
            num_inc_overdue = 0
            per_incomplete = 0
            per_overdue = 0
            per_completed = 0
            por_tasks = 0
            user_over_w.write("\n----------------------------------------------------\n")
            user_over_w.write(f"User:\t\t\t\t\t{users[i][0]}\n")
            for j in range(0, len(tasks)):
                if users[i][0] == tasks[j][0]:
                    num_tasks +=1
                    if tasks[j][5] == "Yes":
                        num_completed += 1
                    elif tasks[j][5] == "No":
                        num_incomplete += 1
                        task_date = datetime.strptime(tasks[j][4], '%d %b %Y')
                        if datetime.date(datetime.now()) < task_date.date():
                            num_inc_overdue += 1
            if num_tasks == 0:
                per_incomplete = 0
                per_overdue = 0
                per_completed = 0
            else:
                per_incomplete = round(100*num_incomplete/num_tasks)
                per_overdue = round(100*num_inc_overdue/num_tasks)
                per_completed = round(100*num_completed/num_tasks)
            if total_tasks == 0:
                por_tasks = 0
            else:
                por_tasks = round(100*num_tasks/total_tasks)
            user_over_w.write((f"User Tasks:\t\t\t\t{num_tasks}\n"
                               f"Portion Total Tasks:\t{por_tasks}%\n"
                               f"Portion Completed:\t\t{per_completed}%\n"
                               f"Portion Incomplete:\t\t{per_incomplete}%\n"
                               f"Portion Overdue:\t\t{per_overdue}%"))
            user_over_w.write("\n----------------------------------------------------\n")
        print("\nReports have been generated: task_overview.txt, user_overview.txt")
        task_over_w.close()
        user_over_w.close()
    else:
        print("\nYou are not authorised to generate reports.\n")


def display_stats():
    
    if user_name == "admin":
        generate_reports()
        task_over_r = open(os.path.join(path_current, "task_overview.txt"), "r+")
        user_over_r = open(os.path.join(path_current, "user_overview.txt"), "r+")
        for line in task_over_r:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))
        for line in user_over_r:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))
            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))
    else:
        print("\nYou are not authorised to view statistics.\n")


#===============================================================================
#----  MAIN FUNCTION  ----------------------------------------------------------
#===============================================================================

if __name__ == "__main__":

    while True:

        user  = open(os.path.join(path_current, "user.txt"), "r+")
        users = user.readlines()
        users = [i.strip().split(", ") for i in users]
        task  = open(os.path.join(path_current, "tasks.txt"), "r+")
        tasks = task.readlines()
        tasks = [i.strip().split(", ") for i in tasks]

        if initial_login:
            user_name = login_user()
            initial_login = False    
    
        if user_name == "admin":
            print("\nPlease select one of the following options:")
            print(("r - register user\n"
                   "a - add task\n"
                   "va - view all tasks\n"
                   "vm - view my tasks\n"
                   "gr - generate reports\n"
                   "ds - display statistics\n"
                   "e - exit"))
            menu = input("")
        else:
            print("\nPlease select one of the following options:")
            print(("a - add task\n"
                   "va - view all tasks\n"
                   "vm - view my tasks\n"
                   "e - exit"))
            menu = input("")

        if menu == "r":
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine()
        elif menu == "gr":
            generate_reports()
        elif menu == "ds":
            display_stats()
        elif menu == "e":
            break
        else:
            print("\nInvalid input. Please retry.")

        user.close()
        task.close()




