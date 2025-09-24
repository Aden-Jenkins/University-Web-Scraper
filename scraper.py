# File Name: manager.py
#
# Author: Aden Jenkins

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from task_utility_functions import can_convert_to_int
from task_utility_functions import save_tasks_to_file
import task

######################################################################
# month_name_to_number():
# Converts a strung representing a month's english name to its
# corresponding number respresentation
#
# name: the name of the month to be converted
# returns a number from 1-12 depending on the month entered
######################################################################
def month_name_to_number(name):
    if name == "January":
        return 1
    elif name == "Febuary":
        return 2
    elif name == "March":
        return 3
    elif name == "April":
        return 4
    elif name == "May":
        return 5
    elif name == "June":
        return 6
    elif name == "July":
        return 7
    elif name == "August":
        return 8
    elif name == "September":
        return 9
    elif name == "October":
        return 10
    elif name == "November":
        return 11
    elif name == "December":
        return 12
    else:
        raise ValueError("Invalid month. Month must be capitalized and spelled out in full")

username = ""
password = ""
driver = None
wait = None
locator = None
element = None
days = []
assignments = []
tasks = []
date = []

# Get username and password
username = input("Please Input your Username now: ")
password = input("Please Input your Password now: ")

# Create webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# navigate to the Texas State Canvas login website
driver.get("https://discovery.canvas.txst.edu")
locator = (By.ID, "txst-login")
element = wait.until(EC.element_to_be_clickable(locator))
element.click()

# Enter Username
locator = (By.ID, "username")
element = wait.until(EC.presence_of_element_located(locator))
element.send_keys(username)

# Enter password
element = driver.find_element(By.ID, "password")
element.send_keys(password)

# Click login
element = driver.find_element(By.TAG_NAME, "button")
element.click()

# Wait for canvas dashboard to be opened
try:
    wait.until(EC.title_is("Dashboard"))
except TimeoutError:
    raise ValueError("The Username or Password you used was incorrect")

# Open page view opions
locator = (By.ID, "DashboardOptionsMenu_Container")
element = wait.until(EC.element_to_be_clickable(locator))
element.click()

# Change Page view to list view
locator = (By.CSS_SELECTOR, "span[data-testid=list-view-menu-item]")
element = wait.until(EC.element_to_be_clickable(locator))
element.click()

# load all future assignments 
# Find the footer where the load more button resides
locator = (By.CLASS_NAME, "css-6jho3r-view")
element = wait.until(EC.presence_of_element_located(locator))

# Change wait context to the footer
wait = WebDriverWait(element, 10)

# Find the load more button
locator = (By.TAG_NAME, "button")

# While the load more button can be found, click the load more button
try:
    element = wait.until(EC.element_to_be_clickable(locator))

    element.click()
except:
    element = None


while not element == None:
    try:
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    except:
        element = None

# Change wait back to a gloabal context
wait = WebDriverWait(driver, 10)

# Get the elements containing all the day data
locator = (By.CSS_SELECTOR, "div[data-testid=day]")
days = wait.until(EC.presence_of_all_elements_located(locator))

i = 0
for day in days:
    # Input date to new task
    date = day.find_element(By.CLASS_NAME, "Day-styles__secondary").text.split(" ", 2)
    
    # If today or tomorrow was printed before the date, then first remove those words
    if not can_convert_to_int(date[1]):
        date[0] = date[1]
        date[1] = date[2]


    # Find all of the assignment elements
    assignments = day.find_elements(By.CSS_SELECTOR, "div[data-testid=planner-item-raw]")
    for assignment in assignments:
        # Change wait context to be in the given assignment
        wait = WebDriverWait(assignment, 30)

        tasks.append(task.Task())

        tasks[i].setDuedate(int(date[1]), month_name_to_number(date[0]), 2025)

        # Ensure all relevent text has loaded
        locator = (By.TAG_NAME, "a")
        element = wait.until(EC.presence_of_element_located(locator))

        # Get title from the assignment name
        element = element.find_elements(By.TAG_NAME, "span")[1]
        tasks[i].setTitle(element.text)

        # Get the description from the assignment type
        locator = (By.CLASS_NAME, "css-65c5ma-text")
        element = wait.until(EC.presence_of_element_located(locator))
        tasks[i].setDescription(element.text)

        i += 1



driver.quit()

save_tasks_to_file("task_data.txt", tasks, 0)

