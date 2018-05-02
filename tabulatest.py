from tabula import wrapper

import pandas as pd
import numpy as np 

from datetime import timedelta, datetime

import tkinter as tk
from tkinter import filedialog

tkroot = tk.Tk()
tkroot.withdraw()
file = filedialog.askopenfilename()

invoice = file[0:7]

#tkinter etc 

df = wrapper.read_pdf(file)

#rename columns
df = df.rename(columns={
    'AGCO International GmbH': 'data', 
    'Unnamed: 1': 'data1',
    'Unnamed: 2': 'data2',
})

#get invoice from filename

#df['connection'] = 

# new df with relevant rows


df['mask'] = df['data'].str.contains('[FGWXYE]\d{7}\s')
df = (df[df['mask'] == True]).drop('mask', axis = 1)

df['connection'] = 'invoice'

df['part'] = df['data'].str.extract(r'[FGWXYE]\d{7}\s(.*)\s') #working

df['qty'] = df['data2'].str.extract(r'(\d*)\s') #working

df['price'] = df['data2'].str.extract(r'\d*\s*\d*\s*(.*)\s') # need to round

df['po'] = df['data'].str.extract(r'[FGWXYE]\d{7}\s*.*\s(.*)') #working

df['date'] = (datetime.now() + timedelta(days=7)).strftime("%Y%m%d")

df['total'] = df['data2'].str.extract(r'\d*\s*\d*\s*.*\s(.*)') #working

df['duplicate'] = df.duplicated(subset=['part', 'po'], keep=False)


df = df.drop(['data', 'data1', 'data2'], axis=1)

df.part = df.part.str.strip()

df.part = df.part.apply('="{}"'.format)


df.to_csv('ConfirmPOLines.csv', encoding='utf-8', index=False)

