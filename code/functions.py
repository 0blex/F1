# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:17:48 2021

@author: alex.black
"""

import pandas as pd

# Import CSV file
#last updated 2021/06/19
def csv_upload(path,index=False,na=None):
    '''import csv file and drop all empty rows'''
    df = pd.read_csv(path, index_col = index,na_values=na)
    df = pd.DataFrame(df).dropna(how='all')
    df = df.dropna(how='all', axis=1)
    print('Upload Successful: {} {} rows & {} columns'.format(path,df.shape[0],df.shape[1]))
    return df