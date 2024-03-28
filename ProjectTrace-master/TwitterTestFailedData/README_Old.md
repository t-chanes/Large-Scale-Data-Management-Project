# ProjectTrace
This project will trace the lifecycle/progress path of the projects funded by the federal agencies.

All the teams should maintain a work-log of progress made each week (This will be collected from commits on this github repo)

Final datasets and code needs to be shared via a GitHub repository (We will need to add steps see below)

## System Design and Project Plan
### Project Plan

This project will trace the lifecycle/progress path of the projects funded by the federal agencies.

Go to the NSF website: https://www.nsf.gov/awardsearch/simpleSearchResult?queryText=CSSI 

Go to the NIH website: https://report.nih.gov/

Go to the DOE website:

Go to the DOJ website (not sure if this is the correct link: https://bja.ojp.gov/funding/expired?search=CSSI%2C+SI2%2C+DIBBS%2C+CICI%2C+MRI%2C+OAC%2C+CCF&fiscal_year=&sort_by=field_closing_date_value&sort_order=DESC#funding-opportunities-block-3-doe-2a5tck9yjpue

(if they are not easily accessible, email the departmental point-of-contact to procure the data)

Search for the awarded projects on the basis of the keywords below, export the data to CSV files, download each file separately first, and then later merge them all

CSSI, SI2, DIBBS, CICI, MRI, OAC, CCF

Perform “topic modeling” on the abstracts and titles of the awards and find the keywords that describe the awards - "Abstracts based on correlation based on content, ex say someone did parallel compute in ER1 or ER2 but we want to be able to cluster both projects together because they both have parallelization in compute in abstracts so matching projects based on award type would not be recommended"

For each project, on the basis of the keywords scrape the web to find the publications, news articles, tweets, videos, etc related to the project

Create a database on the basis of the captured data

Create a web-interface for the database

On the basis of the collected data, create a catalog of the products

On each catalog page, list all the information about the project captured from different sources in a standardized format

On the basis of the gathered information, derive insights/statistics that show the impact of the projects on the society

Please discuss the types of heuristics that you would be adopting for defining the impact of the projects with the instructor

Please secure the website appropriately

### Grading Criteria
Software engineering
guidelines should be
followed and the
project plan should
be prepared and
discussed with the
instructor ✅
### Notes
Submit the project
plan over email and
receive approval,
then work on the
system design and
discuss with the
instructor
![SystemDesignApproval](https://github.com/EduardoTrevino/ProjectTrace/blob/master/System%20Design%20and%20Project%20Plan.jpg?raw=true)

## Data Gathering
### Grading Criteria
The data is collected
from the agreed
upon or discussed
sources, and the
code for collecting
data is fullyfunctional
### Notes
Implement the
code/scripts for
automatic data
collection and data
cleaning

Data has been collected under the data folder for NSF, NIH DOE ✅ **See "Data collection" in https://github.com/EduardoTrevino/ProjectTrace/blob/master/README.md#data-collection**

DOJ is **SCRATCHED**

Data cleaning for merging of the datasets is ✅ **See "Abstract cleaning & further processing" in https://github.com/EduardoTrevino/ProjectTrace/blob/master/README.md#abstract-cleaning--further-processing**

## Database/Data Repository Creation
### Grading Criteria
The database is setup on a server that is
reachable via a webinterface ❌ **See "MongoDB" in project outline**
### Notes
Create a database
and/or a repository
that can be queried
for generating
reports

## Secure Web-interface (UI), statistic dashboards
### Grading Criteria
The interface should
include a search
feature according to
the project being
implemented;
Project-specific
features as discussed
with the instructor
should be
implemented.
The project website
should use https and
not http
### Notes
Support user
accounts were
applicable, the webinterface should be
tested across
different browsers. The test-plan should
consider testing for
security
vulnerabilities

## Features Delivered
### Grading Criteria
All the
discussed/agreed
upon features should
be implemented and
code should be
shared via a GitHub
repository ✅ **https://github.com/EduardoTrevino/ProjectTrace/commits/master**
### Notes
A fully-functional
code with steps to
install (README file)
A test-plan to test all
the features
implemented should
be submitted ✅ **See Project outline below 😊 https://github.com/EduardoTrevino/ProjectTrace/blob/master/README.md#project-outline**

## Presentation & Team Work
### Grading Criteria
A video-recording of
the presentation
should be submitted
by each team,
worklog should be
shared, in-class
presentation is also
required
### Notes
The presentation
should include a
demonstration of the
working prototype
All team members
should be
appropriately
engaged
Worklog should be
shared to track
progress on the
project

## Report/Paper
### Grading Criteria
A paper on the
project
### Notes
The report/paper
should be of a
publishable quality

# Project Outline
## Data collection
Eduardo has Data collected 3 folders each representing an agency (DOE, NIH, NSF), as you can tell we are missing DOJ, I have emailed them but they have not gotten back to me so either we find an online database that has them for me, or maybe there exists a website that I have not ran into yet.

Inside each folder I have placed all their availble data on the basis of the following keywords CSSI, SI2, DIBBS, CICI, MRI, OAC, CCF. If there is a keyword missing under {AGENCYNAME}_{KEYWORD} it is because there was NO AWARD for that agency in that keyword.

To get started on topic modeling:
Our goal is to perform topic modeling on the abstracts and titles of the awards and find the keywords that describe the awards.

1. Preprocess the text data: Remove stop words, punctuation, and other unnecessary characters from the abstracts and titles. Tokenize the text into individual words or phrases, and stem or lemmatize the words to reduce the dimensionality of the dataset.

2. Create a document-term matrix: This matrix will represent the frequency of occurrence of each term in each document. Each row in the matrix represents a document (i.e., an abstract or title), and each column represents a term. (Rememeber EX. we did in R in class)

3. Choose a topic modeling algorithm: There are several popular algorithms for topic modeling, including Latent Dirichlet Allocation (LDA), Non-negative Matrix Factorization (NMF), and Latent Semantic Analysis (LSA). I (Eduardo) have decided to use a LDA model using Gensim.

4. Train the model. This will assign a weight to each term in each topic, indicating how strongly that term is associated with that topic.

5. Analyze the output of the topic model to identify the most relevant topics and the keywords associated with each topic. Examine the top words or phrases in each topic, as well as the probability of each document belonging to each topic.

### Code prep and Guide

Libraies 
```
pip install nltk
pip install gensim
pip install pandas
```

Go on the python notebook (If you wanted to learn R, I didnt use R so you'll have to use a language translator to know what is going on) 

In english what is going on is you will see how I first got all the data from the .csv files which are from the NSF dataset, and NIH datasets and merged the abstracts and titles of them into a pandas dataframe where I appended that into a list. 

Then I did the same for the excel files.

Concatenated into a data frame.

Exported into a csv file (this is good practice to see the preprocessing was done correctly, and serve as a middle point).

Tokenize

Stop words

Stem words

Frequency Dictionary

Document Term matrix

LDA model

Print topics and top keywords. We will use this to scrape the web.




Note that the naming convention we used is:

{Author}_{Algorithm}_{Tokenized}_{STEM or LEM}_{Stopwords rem}


## Abstract cleaning & further processing

For this part of the text we are using a LDA model for each paper in each document to get the top 8 topics of each paper, to cut out the noise we are focusing on the NSF dataset which contains the following segements of information: "AwardNumber", "Title", "NSFOrganization", "PrincipalInvestigator", "PIEmailAddress", "Abstract"

This code processes NSF project data from multiple CSV files, extracts keywords from the abstracts using LDA (Latent Dirichlet Allocation), searches for related news articles using the googlesearch-python library, and saves the results in processed CSV files. Below is a step-by-step explanation of the code, including the prerequisites for running it on your machine.

### Prerequisites
Install Python 3.x.
Install the necessary Python libraries: pandas, gensim, googlesearch-python, nltk, and requests.
You can install them using pip: 
```
pip install pandas gensim googlesearch-python nltk requests
```

### Code Breakdown
Import the necessary libraries.

Download the required NLTK data:
```
nltk.download('stopwords')
nltk.download('wordnet')
```
Define the preprocess_abstract() function to clean and preprocess the abstract text. This function removes HTML tags, converts text to lowercase, removes special characters and numbers, tokenizes the text, removes stopwords, and lemmatizes words.

Define the get_lda_keywords() function to extract keywords from a given LDA model and Bag-of-Words (BoW) representation of a document. The function returns the top keywords for the dominant topic in the document.

Define the search_news() function to search for news articles related to a given title using the googlesearch-python library. The function returns a formatted string containing the title, URL, and description of the search results.

Define the clean_abstract() function to remove HTML tags and extra whitespaces from the abstract text.

List the input NSF CSV files to be processed.

Initialize an empty DataFrame to store the processed data from all the CSV files.

Loop through each input CSV file and perform the following steps:

1. Read the CSV file using pandas and select the required columns.

2. Preprocess the abstracts and create a dictionary and corpus for LDA.

3. Train an LDA model with the corpus and dictionary.

4. Extract the LDA keywords for each abstract.

5. Search for related news articles using the project titles.

6. Clean the abstracts.

7. Rename the columns and reorganize the DataFrame.

8. Save the processed data to a new CSV file with the appropriate name.

9. Append the processed data to the all_projects DataFrame.

Save the combined processed data from all the CSV files to a single output merged CSV file.

To run the code on your machine, make sure you have installed the necessary prerequisites and placed the input NSF CSV files in the correct directory. Then, execute the Python script containing the code. The processed data will be saved in the specified output CSV files, and you'll see a message indicating the successful completion of each file.
