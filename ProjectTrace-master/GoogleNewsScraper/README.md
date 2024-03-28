# News Scraper
A library created to scrape Google News for news links for given topics that are then ran through newspaper3k for extracting the text from the articles.<br>

## Pre-requisites:
1. Python modules: pygooglenews, newspaper3k, nltk, multi_rake

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
4. Edit your desired parameters in googleNewsScrap.py
    ```
    f                   = Output CSV file to which article text, URL, summary, and other colums from original CSV file are saved to 
    fin                 = Original CSV file from which to pull keywords from 
    USER_AGENT          = Must use the proper Mozilla Firefox useragent for your system 
    fieldnames          = Choose which colums from original CSV file needs to be kept
    ```
4. Run the program
    ```
    python3 googleNewsScrap.py
    ```

## Usage:
This project was created to bypass Google Chrome's new restrictions on web scraping from Google Images. 
To use it, define your desired parameters in main.py and run through the command line:
```
python main.py
```

## IMPORTANT:
You must identify and use the proper useragent for your system or the program can fail. Useragent can be found at: https://www.whatismybrowser.com/detect/what-is-my-user-agent/.

