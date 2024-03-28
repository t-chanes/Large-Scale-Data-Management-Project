from pygooglenews import GoogleNews
from newspaper import Article
from newspaper import Config
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv
import re, os
import requests
import shutil 
import concurrent.futures

def filter(input):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(input)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(filtered_sentence)

    orAdded = re.sub("[\",]", "", str(filtered_sentence))
    print(orAdded)

    return orAdded

fieldnames = ['Award_number', 'Project_name', 'Funding_agency', 'PI_name', 'PI_contact', 'Description', 'Keyword', 'article_title', 'URL', 'article_text', 'article_summary']

f = open('./NIHexportedNews.csv', 'w')
writer = csv.DictWriter(f, fieldnames=fieldnames)

writer.writeheader()

fin = open('./NIH_all_final.csv', 'r')
reader = csv.DictReader(fin)

isExist = os.path.exists("./text")
if not isExist:
    os.mkdir("./text")

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10 

gn = GoogleNews()

def process_row(row):
    data = [row["Project_name"]]
    projNum = [row["Award_number"]]
    fundAg = [row["Funding_agency"]]
    piName = [row["PI_name"]]
    contact = [row["PI_contact"]]
    Description = [row["Description"]]
    Keyword = [row["Keyword"]]

    print(data)
    print(projNum)
    
    filteredData = filter(re.sub("[()[\]{},.\:]", "", str(data)))
    # print(filteredData)
    
    s = gn.search(filteredData)

    for item in s["entries"]:
        story = item.title
        url = item.link
        article = Article(url, language='en')
        
        try:
            article.download()
            article.parse()
        except:
            pass

        title = article.title
        text = article.text
        image = article.images
        videos = article.movies
        url = article.url
        summ = article.summary

        textFile_name = "./text/" + str(projNum) + "-" + str(x) + ".txt"

        f = open(textFile_name, "w")
        f.write(text)
        f.close()

        try:
            article.nlp()
        except:
            pass

        news = {
            'Award_number' : projNum, 
            'Project_name' : data, 
            'Funding_agency' : fundAg, 
            'PI_name' : piName, 
            'PI_contact' : contact, 
            'Description' : Description, 
            'Keyword' : Keyword,
            'article_title' : title, 
            'URL' : url, 
            'article_text' : text, 
            'article_summary' : summ
        }

        writer.writerow(news)

    print("done with ", projNum)


with concurrent.futures.ThreadPoolExecutor() as executor:
    for row in reader:
        executor.submit(process_row, row)

f
