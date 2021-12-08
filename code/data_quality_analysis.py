# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:54:49 2021

@author: alex.black
"""

import os
import seaborn as sns

root_dir = 'D:\Dropbox (PMX)\Personal Work\Python\Code\Projects\F1\\'
os.chdir(root_dir)

os.chdir(root_dir+'code')
from import_input_csv_files import results

df = results


df_updated = df.set_index('resultId')
sns.heatmap(df_updated.isnull(), cbar=False)


df.info()


positions = df[['position','positionText']]
positions.info()
positions['position'].value_counts().sort_index()

positions['positionText'].value_counts().sort_index()

positions_filtered = positions[positions['position'].isnull() & ~positions['positionText'].isnull()]


positions_filtered.info()
positions_filtered.head()
positions_filtered['positionText'].value_counts()
