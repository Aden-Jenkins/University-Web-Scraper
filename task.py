# File name: task.py
#
# Author: Aden Jenkins
# Description: This file contains the full class description for a task
#
# This class uses setter functions to edit its variables during runtime

import datetime

class Task:
    # Static variables
    MAX_TITLE_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 80

    def __init__(self, title = "", duedate = datetime.date(1, 1, 1), description = ""):
        
        self.setTitle(title)        
        self.setDuedate(duedate.day, duedate.month, duedate.year)
        self.setDescription(description)    

    # The string representation for this class
    def __str__(self):
        return f"{self.title}\n{self.date.year}\n{self.date.month}\n{self.date.day}\n{self.description}"
    
######################################################################
# print():
# Prints the title, date, and description of the task instance to the
# console.
######################################################################
    def print(self):
        print(f"TO DO: {self.title}")
        print(f"DUE: {self.date}")
        print(f"DESCRIPTION: {self.description}")

######################################################################
# setTitle():
# The setter function for the title object variable. Ensures that the
# new title fits within length criteria
#
# newTitle: The new value for the title variable
# returns true if the title was changed successfully
# returns false if the title does not fit criteria (title not changed)
######################################################################
    def setTitle(self, newTitle):
        if len(newTitle) > self.MAX_TITLE_LENGTH:
            return False
        else:
            self.title = newTitle
            return True
    
######################################################################
# setDescription():
# The setter function for the description object variable
#
# newDescription: The new value for the description variable
# returns true if the description was changed successfully
# returns false if the description does not fit criteria
######################################################################
    def setDescription(self, newDescription):
        if len(newDescription) > self.MAX_DESCRIPTION_LENGTH:
            return False
        else:
            self.description = newDescription
            return True

######################################################################
# setDuedate():
# A setter function for the dueDate object variable
#
# day: the day value for the new dueDate. Must be between 1-31
# month: the month value for the new dueDate. Must be between 1-12
# year: the year value for the new dueDate. Must be between 1-9999
# returns true if the dueDate was changed successfully
# returns false if the dueDate falls outside of criteria
######################################################################
    def setDuedate(self, day, month, year): 
        # ensure all parameters are integers
        if not isinstance(day, int):
            return False
        elif not isinstance(month, int):
            return False
        elif not isinstance(month, int):
            return False

        # ensure all parameters are of a valid date
        if day < 1 or day > 31:
            return False
        elif month < 1 or month > 12:
            return False
        elif year < 1 or year > 9999:
            return False
        else:
        
        # set new date
            self.date = datetime.date(year, month, day)
            return True


