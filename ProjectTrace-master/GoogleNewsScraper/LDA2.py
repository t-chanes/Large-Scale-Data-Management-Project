from multi_rake import Rake

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import csv
import re

csvFilePath = 'NSF_DIBBS_final3_output.csv'

numRows = 0
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter=',')
    numRows = sum(1 for row in csvReader)
    # for row in csv_reader:
 
    #     # adding the first row
    #     columnNames.append(row)
 
    #     # breaking the loop after the
    #     # first iteration itself
    #     break

print(numRows)

# keywordsFound = []*numRows

x=0
with open(csvFilePath) as csvFile, open('NSF_DIBBS_newLDAoutput.csv', 'w') as outFile:
    csvReader = csv.DictReader(csvFile)
    writer = csv.writer(outFile)
    for x, row in enumerate(csvReader):
        data = [row["Abstracts"]]

        rake = Rake()
        keywords = rake.apply(str([data]))
        #keywords[row]=(keywords[:10])
        print("\n")
        print(x)
        # print(data)
        print("\n")
        print(keywords[:10])
        LDA_abstract_keywords= re.sub("[()[\]{}\d,.]", "", str(keywords[:10]))
        print(LDA_abstract_keywords)
        writer.writerow([LDA_abstract_keywords])
        x+1

# print("len of keywordsFound:", len(keywordsFound))
print(LDA_abstract_keywords)