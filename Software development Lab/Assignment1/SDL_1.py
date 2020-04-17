#SDL Assignment -1
#Perform data processing and cleaning of dataset using Python.

import pandas as pd
import numpy as np

data = pd.read_csv("movies.csv")    #IMPORT files into VAR = data

print data.head()   #Print First-5 lines of DATA
print data.shape    #Dimensions of DATA [Row,Column]
print type(data.shape)  #Type = Tuple

A = data.iloc[:5,:] #1st 5 Rows & All Columns
print A
print data.loc[:5,['rating','year']]    #1st 5 Rows of RATING & YEAR
print data['year']                      #All Rows of Column= YEAR

print type(data['rating']) #Type = pandas.core.series.Series

#Create a Series
S = pd.Series([5,10])   #Series of Type= int
print S

_S = pd.Series(['Bhargav','Ankit','Machine','Learning','Using','PYTHON'])   #Series of Type= String
print _S

#Creating Data Frames: [By Adding Multiple SERIES]
#METHOD - 1
_DataFrame = pd.DataFrame([S,_S])
print _DataFrame

#METHOD - 2
_DataFrame = pd.DataFrame(
    [
        [5,10],
        ['Bhargav','Ankit','Machine','Learning','Using','PYTHON']
    ]
)
print _DataFrame
#METHOD - 3 [NAMING 'Rows' & 'Columns']
_DataFrame = pd.DataFrame(
    [
        [5,10],
        ['Bhargav','Ankit','Machine','Learning','Using','PYTHON']
    ],
    columns=['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH'],
    index=['ROW-1','ROW-2']
)
print _DataFrame

#SOME OPERATIONS IN DATA FRAME
#1. AVERAGE
print data['rating'].mean() #Average of Column 'RATING'
print data.mean(axis=1)     #Average of Each Row

#2. Filter Operations
_FILTER = data['rating'] > 3.8 #Filters the data on given constraints
print _FILTER                   #Filter Output = [True/False]
print data[_FILTER]             #Displays Data on given Filter

_FILTER = (data['rating'] > 3.8) & (data['year'] < 2000)    #MULTIPLE Filters
print _FILTER
print data[_FILTER]

print dir(data) #SHOWS ALL FUNCTIONs Possible on DATA-FRAME 'data'
data[_FILTER].to_csv('movies2.csv') #Writes Filtered DATA into file