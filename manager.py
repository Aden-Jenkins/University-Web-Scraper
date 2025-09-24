# File Name: time_management.py
#
# Author: Aden Jenkins
# Date: July 25, 2025
# Description

import os
import task_utility_functions as TUF

# CONSTANTS #
FILE_NAME = "task_data.txt"

######################################################################
# print_welcome_message():
# Prints a welcome to the user and instructions on how to use this 
# application properly
######################################################################
def print_user_action_list():
    print("list: generate a list of all your tasks")
    print("add: create and add a new task")
    print("complete: mark a task as complete")
    print("quit: exit the application")
    print("\n")

# VARIABLES #
tasks = [] 
numTasksCompleted = 0
user_input = ""
valid_input = False

# PROGRAM #
# IF the file FILE_NAME exists
if os.path.exists(FILE_NAME):
    # THEN read all the data from the file
    with open(FILE_NAME, "r") as file:
        # AND store the data in the runtime variable called tasks
        tasks = TUF.read_tasks_from_file(FILE_NAME)

while user_input != "quit":
    TUF.clear_screen()
    print_user_action_list()

    user_input = input("Pick your action now: ")

    if user_input == "list":
        TUF.clear_screen()
        TUF.print_task_list(tasks)
        input("Press ENTER To Continue")
    
    elif user_input == "add":
        TUF.add_new_task(tasks)
    
    elif user_input == "complete":
        TUF.clear_screen()
        if len(tasks) > 0:
            TUF.complete_task(tasks)
            numTasksCompleted += 1

        else:
            print("There are no tasks to complete\n")
            input("Press ENTER To Continue")

TUF.save_tasks_to_file(FILE_NAME, tasks, numTasksCompleted)
