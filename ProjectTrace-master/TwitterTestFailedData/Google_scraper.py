import os
import csv
from googlesearch import search
from google_images_search import GoogleImagesSearch

# Your Google Custom Search JSON API key and cx value
api_key = 'your_api_key'
cx = 'your_cx_value'

# Initialize the Google Images Search object
gis = GoogleImagesSearch(api_key, cx)

# Set the daily query limit
daily_query_limit = 100
current_query_count = 0

def main():
    # Read the CSV file
    with open(r'D:\Spring 2023 Senior Year\CS 4243 Large Scale Data Management\Assignments\Project\NSF_DIBBS_final3_output.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Create the main directory for the images
        main_dir = 'images'
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)

        # Load the last processed row from a file (if it exists)
        last_processed_row_file = 'last_processed_row.txt'
        if os.path.exists(last_processed_row_file):
            with open(last_processed_row_file, 'r') as f:
                start_row = int(f.read())
        else:
            start_row = 1

        # Iterate through the rows and get the project titles
        for i, row in enumerate(reader):
            if i + 1 < start_row:
                continue

            title = row['Project_title']
            if not title:
                continue

            # Create a folder for each project
            project_dir = os.path.join(main_dir, title)
            if not os.path.exists(project_dir):
                os.makedirs(project_dir)

            # Search and download images
            gis.search({'q': title, 'num': 10})
            current_query_count += 1

            for image in gis.results():
                image.download(project_dir)

            # Check if the daily query limit is reached
            if current_query_count >= daily_query_limit:
                print("Daily query limit reached.")
                break

            # Save the last processed row
            with open(last_processed_row_file, 'w') as f:
                f.write(str(i + 1))

if __name__ == '__main__':
    main()
