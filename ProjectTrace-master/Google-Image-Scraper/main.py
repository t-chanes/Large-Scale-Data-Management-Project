# -*- coding: utf-8 -*-
"""

@author: Eduardo Trevino

"""
import os
import concurrent.futures
import pandas as pd
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable

import csv

def initialize_csv(output_file="NSFimage_urls.csv"):
    with open(output_file, mode="w", newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Award_number", "ImageLink1", "ImageLink2", "ImageLink3", "ImageLink4", "ImageLink5"])

def write_to_csv(award_number, image_urls, output_file="NSFimage_urls.csv"):
    with open(output_file, mode="a", newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([award_number] + image_urls)
        #write_to_csv function will handle cases where there are 0 or less than 5 links. If there are fewer than 5 image URLs, the function will write the available URLs to the CSV file, and the remaining cells in the row will be left empty.


def worker_thread(search_key, image_path, award_number):
    image_scraper = GoogleImageScraper(
        webdriver_path,
        image_path,
        search_key,
        number_of_images,
        headless,
        min_resolution,
        max_resolution,
        max_missed)
    image_urls = image_scraper.find_image_urls()
    # Send image_url to csv file with Award_number
    write_to_csv(award_number, image_urls)
    image_scraper.save_images(image_urls, keep_filenames, award_number)

    # Release resources
    del image_scraper


def sanitize_folder_name(folder_name):
    return folder_name.replace(':', '_')


def preprocess_title(title):
    # Remove special characters
    title = "".join(c for c in title if c.isalnum() or c.isspace())
    # Remove excess spaces
    title = " ".join(title.split())
    return title


if __name__ == "__main__":
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(r"D:\Spring 2023 Senior Year\CS 4243 Large Scale Data Management\Assignments\Project\GoogleImagesData\NSFMergedDataImagesOfficial")

    # Read CSV file and extract Project_titles and Award_numbers
    csv_path = r"D:\Spring 2023 Senior Year\CS 4243 Large Scale Data Management\Assignments\Project\NSFDataProcessedFinal\NSF_all_final.csv"
    df = pd.read_csv(csv_path)
    project_titles = df["Project_name"].tolist()
    award_numbers = df["Award_number"].tolist()

    # Parameters
    number_of_images = 5                # Desired number of images
    headless = True                     # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (9999, 9999)       # Maximum desired image resolution
    max_missed = 10                     # Max number of failed images before exit
    number_of_workers = 1               # Number of "workers" used
    keep_filenames = False              # Keep original URL image filenames

    # Create the GoogleImagesData\NSF_DIBBS directory if it doesn't exist
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    # Initialize CSV file
    initialize_csv()

    # Run each project_title in a separate thread
    # Automatically waits for all threads to finish
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        for idx, (title, award_number) in enumerate(zip(project_titles, award_numbers)):
            preprocessed_title = preprocess_title(title)
            sanitized_title = sanitize_folder_name(preprocessed_title)
            award_number_folder = os.path.join(image_path, str(award_number))
            if not os.path.exists(award_number_folder):
                os.makedirs(award_number_folder)

            # Save the current row number in a text file
            with open('current_row.txt', 'w') as f:
                f.write(str(idx))

            executor.submit(worker_thread, title, award_number_folder, award_number)




