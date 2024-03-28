import pandas as pd
import glob

xls_file_list = []

#must create a folder named xlsdata in the Downloads directory if none, then add the files to the folder

for file in glob.glob('Downloads/xlsdata/*.xls', recursive=True):
  xls_file_list.append(file)

#merge xls files into one  super xls file

df_final = pd.DataFrame()

for file in xls_file_list:
  excel_file = pd.ExcelFile(file)
  sheets = excel_file.sheet_names  #make sure that xls file has one or multiple sheets
  for sheet in sheets:
    df = excel_file.parse(sheet_name=sheet)
    df_final = df_final.append(df)

#print(df_final.head)
#remove unwanted columns in excel sfile
col_list = list(df_final.columns)
col_list=[col_list[0],col_list[1],col_list[2],col_list[6],col_list[11],col_list[25]]  #columns we wanted


df_final= df_final[col_list]


#write it in one excel and sends it to current directory. not in the downloads
df_final.to_excel('DOE_final.xlsx')