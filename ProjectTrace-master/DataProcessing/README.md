# Project Trace: Data Cleaning and Processing
This repository contains code for cleaning and processing datasets from three different funding agencies: National Science Foundation (NSF), National Institutes of Health (NIH), and Department of Energy (DOE). The code is organized in three separate Jupyter Notebook files named clean_{AgencyName(NSF,NIH,DOE)}_data.ipynb.

## Overview
The code in each notebook performs the following tasks:

1. Import necessary libraries and define helper functions.
2. Read data from specified files for each agency.
3. Preprocess the abstracts of the projects by removing HTML tags, converting text to lowercase, removing special characters and numbers, tokenizing the text, removing stopwords, and lemmatizing words.
4. Use Latent Dirichlet Allocation (LDA) to extract keywords from the abstracts.
5. Clean abstracts by removing HTML tags and extra whitespaces.
6. Rename columns to standardize the data across all agencies.
7. Save the processed data in CSV format.

## Setup
Before running the code, ensure the following libraries are installed:

* pandas
* gensim
* nltk
* chardet
* requests

You can install these libraries using pip:
```
pip install pandas gensim nltk chardet requests
```

## Data
For each agency, the raw data is stored in separate CSV or Excel files. Below are the file paths for each agency:

NSF: NSFdata/NSF_CCF.csv, NSFdata/NSF_CICI.csv, NSFdata/NSF_CSSI.csv, NSFdata/NSF_DIBBS.csv, NSFdata/NSF_MRI.csv, NSFdata/NSF_OAC.csv, NSFdata/NSF_SI2.csv

NIH: /home/gra248/projects/ProjectTrace/NIHdata/NIH_CCF.csv, /home/gra248/projects/ProjectTrace/NIHdata/NIH_CICI.csv, /home/gra248/projects/ProjectTrace/NIHdata/NIH_CSSI.csv, /home/gra248/projects/ProjectTrace/NIHdata/NIH_MRI.csv, /home/gra248/projects/ProjectTrace/NIHdata/NIH_OAC.csv

DOE: /home/gra248/projects/ProjectTrace/DOEdata/DOE_CCF.xls, /home/gra248/projects/ProjectTrace/DOEdata/DOE_MRI.xls, /home/gra248/projects/ProjectTrace/DOEdata/DOE_OAC.xls

Make sure to adjust the file paths according to your local setup.

## Running the Code

1. Open the desired Jupyter Notebook file in a Jupyter environment.
2. Update the file paths to match your local setup.
3. Run the code cells in the notebook sequentially.
4. The processed data will be saved as a CSV file with the suffix _processed.csv (e.g., NSF_CCF_processed.csv).
