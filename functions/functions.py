

import pandas as pd
from datetime import datetime

# Import CSV file
# last updated 2021/09/23
def csv_upload(path,index=False,dtype=None,encoding=None,na=None):
    '''import csv file and drop all empty rows'''
    df = pd.read_csv(path, index_col = index, dtype=dtype, encoding=encoding, na_values=na)
    df = pd.DataFrame(df).dropna(how='all')
    df = df.dropna(how='all', axis=1)
    print('Upload Successful: {} {} rows & {} columns'.format(path,df.shape[0],df.shape[1]))
    return df

# Import from xsl file
# last updated 2021/09/22
def xls_upload(path,sheet=0,index=False,dtype=None,usecols=None):
    '''import excel file and drop all empty rows'''
    df = pd.read_excel (path, sheet_name = sheet, index_col=index, dtype=dtype,usecols=usecols)
    df = pd.DataFrame(df).dropna(how='all')
    if sheet==0:
        print('Upload Successful: {} {} rows & {} columns'.format(path,df.shape[0],df.shape[1]))
    else:
        print('Upload Successful: '+sheet+' {} rows & {} columns'.format(df.shape[0],df.shape[1]))
    return df

# write to log file
def log(text):
    with open('RunLog.txt','a+') as file:
        file.write(str(datetime.now())+": "+text+'\n')
        
# read sql query and return variable
def read(text):
    with open(text, 'r') as file:
        query = file.read() 
    return query