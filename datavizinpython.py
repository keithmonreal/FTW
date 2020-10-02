# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:43:42 2020

@author: Keith Monreal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv (r'C:\Users\Keith Monreal\OneDrive - University of the Philippines\FTW\Statistics\nyc-rolling-sales.csv')
print (df)

#know the number of rows and columns
len(df.axes[0]) #rows
len(df.axes[1]) #columns

#descriptives before data cleaning 
stats1 = df.describe()

#data cleaning
df.columns
df.head

#subsetting the data frame -------------
final = df[["YEAR BUILT","BOROUGH", "TAX CLASS AT TIME OF SALE", "RESIDENTIAL UNITS", "COMMERCIAL UNITS", "TOTAL UNITS", "LAND SQUARE FEET","GROSS SQUARE FEET", "SALE PRICE"]]
final.describe()
final2 = final.dropna()
final2.describe()

#categorical variables ---------------

bo = final2['BOROUGH']
final2['BOROUGH'].unique() #array([1, 2, 3, 4, 5], dtype=int64)
tax = final2['TAX CLASS AT TIME OF SALE']
df['TAX CLASS AT TIME OF SALE'].unique() #array([2, 4, 1, 3], dtype=int64)

#numerical variables -----------------
ru = final2['RESIDENTIAL UNITS']
final2['RESIDENTIAL UNITS'].describe()

cu = final2['COMMERCIAL UNITS']
final2['COMMERCIAL UNITS'].describe()

tu = final2['TOTAL UNITS']
final2['TOTAL UNITS'].describe()

#cast object to numeric 

ls = final2['LAND SQUARE FEET'] 
final2['LAND SQUARE FEET'] = pd.to_numeric(df['LAND SQUARE FEET'], errors ='coerce')
final2['LAND SQUARE FEET'].describe()

gs = final2['GROSS SQUARE FEET']
final2['GROSS SQUARE FEET'] = pd.to_numeric(df['GROSS SQUARE FEET'], errors ='coerce')
final2['GROSS SQUARE FEET'].describe()

sp = final2['SALE PRICE']
final2['SALE PRICE'] = pd.to_numeric(df['SALE PRICE'], errors ='coerce')
final2['SALE PRICE'].describe()


#by_borough vs total units
by_borough_tu = final2.groupby('BOROUGH')['TOTAL UNITS'].mean()
by_borough_tu.plot(kind='bar', color = 'k')

#by_borough vs land square feet
by_borough_ls = final2.groupby('BOROUGH')['LAND SQUARE FEET'].mean()
by_borough_ls.plot(kind='bar', color = 'k' )

#by_borough vs sale price
by_borough_sp = final2.groupby('BOROUGH')['SALE PRICE'].mean()
by_borough_sp.plot(kind='bar', color = 'k')

#by_tax vs total units
by_borough_tu = final2.groupby('TAX CLASS AT TIME OF SALE')['TOTAL UNITS'].mean()
by_borough_tu.plot(kind='bar', color = 'b')

#by_tax vs land square feet
by_borough_ls = final2.groupby('TAX CLASS AT TIME OF SALE')['LAND SQUARE FEET'].mean()
by_borough_ls.plot(kind='bar', color = 'b')

