import task
import datetime

######################################################################
# clear_screen():
# This function will clear the console screen by printing empty lines
######################################################################
def clear_screen():
    i = 0

    while i < 50:
        print("\n")
        i += 1

######################################################################
# save_tasks_to_file():
# Saves each element in an array of tasks to a text file. Will create
# a text file if none exists.
#
# fileName: the name of the text file that will store the task data
# tasks: the list of tasks that will be stored in the text file
######################################################################
def save_tasks_to_file(fileName, tasks, numTasksCompleted):
    # clear the file fileName or creates it if it does not exist
    file = open(fileName, "w")
    file.close()

    # write new data to the cleared file
    file = open(fileName, 'a')

    # write the number of tasks to the top of the file
    file.write(str(len(tasks) - numTasksCompleted))

    for task in tasks:
        # writes task to file in the format of title, date, then description
        # each task's data is seperated with a new line
        if not task.isCompleted():
            file.write(f"\n{task}")

    file.close()

######################################################################
# read_tasks_from_file():
# Reads data formatted by the save_tasks_to_file() function and stores
# the data in an array of tasks.
#
# fileName: the name of the text file containing the task data
# returns an array of tasks
######################################################################
def read_tasks_from_file(fileName):
    tasks = []
    title = ""
    day = 0
    month = 0
    year = 0
    description = ""

    file = open(fileName, "r")

    i = 0
    # Get the number of stored tasks from the first line in the file
    numOfTasks = int(file.readline())

    # FOR each saved task
    while i < numOfTasks:
        # Get each task element form the file (order is important)
        title = file.readline().strip("\n")
        year = int(file.readline().strip("\n"))
        month = int(file.readline().strip("\n"))
        day = int(file.readline().strip("\n"))
        description = file.readline().strip("\n")

        # Save each elements information as a new task in an array of tasks
        tasks.append(task.Task(title, datetime.date(year, month, day), description))

        i+= 1

    file.close()

    return tasks


######################################################################
# print_task_list():
# Prints a formatted list of all tasks to the console
#
# tasks: the array of tasks that will be printed to the console
######################################################################
def print_task_list(tasks):
    num = 1

    for task in tasks:
        if not task.isCompleted():
            print(f"{num}.")
            task.print()
            print("\n")

            num += 1


######################################################################
# add_new_task(): 
# Creates and adds a new task to the end of a given list of tasks. 
# This function adds a new task through user input.
#
# tasks: the list of tasks that will be changed by this function
######################################################################
def add_new_task(tasks):
    newTask = task.Task()
    user_input = None
    day = -1
    month = -1
    year = -1

    # get the new title
    clear_screen()

    print("Write a short title for the task in 30 characters or less.")
    user_input = input("Enter title now: ")
    while not newTask.setTitle(user_input):
        clear_screen()

        print("Your title must be 30 characters or less")
        user_input = input("Enter title now: ")
        
    # get the new date
    clear_screen()

    print("When does the task need to be completed?\n")

    while not newTask.setDuedate(int(day), int(month), int(year)):
        try:
            day = int(input("Enter the day now: "))
            month = int(input("Enter the month now: "))
            year = int(input("Enter the year now: "))
        
        except ValueError:
            day = -1
            month = -1
            year = -1

        print("The date you entered was invalid. Please try again.")
        clear_screen()


    # get the new description
    clear_screen()

    print("Write a short description for the task.\n")
    user_input = input("Write description now:\n")

    while not newTask.setDescription(user_input):
        clear_screen()

        print("Description must be 80 characters or less")
        user_input = input("Write description now:\n")

    tasks.append(newTask)

######################################################################
# complete_task():
# All tasks are listed starting at 1. The user is asked to input a 
# number associated with a task. That task is marked as complete
#
# tasks: the list of tasks to be evaluated by this function
######################################################################
def complete_task(tasks):
    valid_input = False

    while not valid_input:
        print_task_list(tasks)
        user_input = input("Enter the number of the task you would like to complete: ")

        # FIXME: Wrong imput messages do not display to console
        if can_convert_to_int(user_input) == False: 
            print("You must enter a number.")
        elif int(user_input) < 0 or int(user_input) > len(tasks):
            print("The number you entered is out of bounds.")
        else:
            valid_input = True

    # FIXME: Change implomentation to use a linked list
    if tasks[int(user_input)-1].isCompleted():
            print("This task is already complete")
    else:
        tasks[int(user_input)-1].markComplete()

######################################################################
# can_convert_to_int():
# Checks to see if a variable can be converted to an integer value
#
# val: the variable to be evaluated
# returns true if the variable can be converted to an integer
# returns false if the variable cannot be converted to an integer
######################################################################
def can_convert_to_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False