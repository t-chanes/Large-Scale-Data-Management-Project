
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
# Title = []
# URL = []
# Text = []
# Summary = []

f = open('./exportedNews.csv', 'w')
writer = csv.DictWriter(f, fieldnames=fieldnames)

writer.writeheader()

fin = open('./NSF_all_final.csv', 'r')
reader = csv.DictReader(fin)

isExist = os.path.exists("./text")
if not isExist:
    os.mkdir("./text")

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'
config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10 

gn = GoogleNews()

for x, row in enumerate(reader):
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

    # for entry in s["entries"]:
    #     print(entry["title"])
    # news = {
    #     "Title" : "t",
    #     "URL" : "url",
    #     "Text" : "t",
    # }
    # aritclesFound = []

    for item in s["entries"]:
        story = item.title
        url = item.link
        article = Article(url, language='en')
        
        try:
            article.download()
            article.parse()
            # authors = ", ".join(author for author in article.authors) 
        except:
            pass

        title = article.title
        # date = article.publish_date
        text = article.text
        # print("text: %s", article.text)
        image = article.images
        videos = article.movies
        url = article.url
        summ = article.summary
        # print("summ: ", article.summary)

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

    ##For Finding Images/Videos from webpage
        # for x, image in enumerate(image):
        #     print(image)
        #     exten = re.search(".\w+$", image)
        #     # print(exten.group(0))
        #     file_name = str(projNum) + "-" + str(x) + exten.group(0)
        #     print(file_name)
        #     res = requests.get(image, stream = True)
            
        #     try:
        #         if res.status_code == 200:
        #             with open(file_name,'wb') as f:
        #                 shutil.copyfileobj(res.raw, f)
        #             print('Image sucessfully Downloaded: ', file_name)
        #         else:
        #             print('Image Couldn\'t be retrieved')
        #     except:
        #         pass
        #     x+1

        # for videos in videos:
        #     print(videos)

        # aritclesFound.append(news)
        writer.writerow(news)
        # Title.append(story)
        # URL.append(url)
        # Text.append(text)

    # print(aritclesFound)
    # f.close()
    print("done with ", x)
    x+1

#print(s["entries"]["title"])