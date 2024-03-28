# Google Image Scraper
A library created to scrape Google Images.<br>

## Pre-requisites:
1. Google Chrome
2. Python3 packages (Pillow, Selenium, Requests)
3. Windows OS (Other OS is not tested)

## Setup:
1. Open command prompt
2. Clone\pull this repository
    ```
    git clone https://github.com/EduardoTrevino/ProjectTrace.git
    ```
3. Install Dependencies
    ```
    pip install -r requirements.txt
    ```
4. Edit your desired parameters in main.py
    ```
    search_keys         = Strings that will be searched for
    number of images    = Desired number of images
    headless            = Chrome GUI behaviour. If True, there will be no GUI
    min_resolution      = Minimum desired image resolution
    max_resolution      = Maximum desired image resolution
    max_missed          = Maximum number of failed image grabs before program terminates. Increase this number to ensure large queries do not exit.
    number_of_workers   = Number of sectioned jobs created. Restricted to one worker per search term and thread.
    ```
4. Run the program
    ```
    python main.py
    ```

## Usage:
This project was created to bypass Google Chrome's new restrictions on web scraping from Google Images. 
To use it, define your desired parameters in main.py and run through the command line:
```
python main.py
```

## IMPORTANT:
It must be run in the command line/ terminal not on VSCODE IDE play button.

This program will install an updated webdriver automatically. There is no need to install your own.

