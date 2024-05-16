# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:28:39 2024

@author: nanab
"""
#when creating a new remember .py

#to install a library, run anaconda prompt as admin 
#pip install pandas
#importing a library(pandas),so not to write a whole code to read csv
import pandas as pd

#to read csv file
#filename = pd.read_csv('file,csv')
#make sure to locate file directory on right
data = pd.read_csv('transaction.csv')

#in such case we needed to seperate the columns which was ;
data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

##list=[list],range=range(2,5) tuple=(tuple)"cannot be altered, dic={'name':akua, 'age':'10'}, set ={'set1..'}

#calculations now
#defining vars

#adding column to dataframe
#var=dataframe[columnname]

CostPerItem=data['CostPerItem']
NumberOfItemsPurchased=data['NumberOfItemsPurchased']
SellingPricePerItem=data['SellingPricePerItem']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased
ProfitPerTransaction = SellingPricePerTransaction - CostPerTransaction
ProfitPerItem = SellingPricePerItem - CostPerItem

#adding new columns to dataframe
data['CostPerTransaction'] = CostPerTransaction
data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = (data['SellingPricePerTransaction'] - data['CostPerTransaction'])
data['markup'] = (data['ProfitPerTransaction'] / data['CostPerTransaction'])
data['markup'] = round(data['markup'],2)

#combining data fields
#or concactunate
# name= "francis" + "obiri"

#data['Date']= data['Day']+ ['-']  + data['Month'] + ['-']+ data['Year']
data.info()
#puthon does no support concuctunating str n int so we hv to convert usn .astype to str, NM//str
data['Date']= data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

data.head(-5) #view specific column
data.iloc[0:1] #view specific row
data.iloc[:,3] #column number
data.iloc[4,3] #4th row, 3rd col

#using split to seperate clientfield
#varname= columnname.str.split('sep',expand = True)
data[['client_age', 'business_type ', 'duration']] = data['ClientKeywords'].str.split(',' ,expand = True )

#using replace function
data['client_age'] = data['client_age'].str.replace('[','')
data['duration'] = data['duration'].str.replace(']','')

#changing to proper or lower case
data['ItemDescription']=data['ItemDescription'].str.title()

#merging file
#bringing in new file

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging using common keyword
#mergedf=pd.merge(olddf,newdf,on='coomonkeyword')
data=pd.merge(data,seasons, on= "Month")

#removing columns
#df = df.drop('column', axis = 1) axis=1 means column n 0 means row

data = data.drop('ClientKeywords',axis =1)
data = data.drop(['Day','Month','Year'],axis =1)

#exporting into csv
#data.to.csv
data.to_csv('ValueIncCleaned.csv',index=False)
