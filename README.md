# University-Web-Scraper
An example program made using python. 

manager.py is the executable that acts as a rudamentary task manager to handle the data collected by this project's web scraping.
scraper.py is the executable that gathers all relevent task data. scraper.py requires the user to input their username, password, and navigate their duo security. Everything else is automated by selenium.

This project uses selenium and google chrome to access and interact with the web. 

While this project is in a working state, there are two small bugs in the system:
First, some assignment titles are unable to be captured by the selenium prompts used.
Second, the complete function in the task manager is handled by booleans leading to the user being unable to accurately predict the outcome of completeing certain tasks.

The second issue will eventually be fixed with the implomentation of a linked list.
