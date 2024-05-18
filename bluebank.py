# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 08:41:59 2024

@author: nanab
"""



import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#opening and loading json data 
json_file = open('loan_data_json.json')
data = json.load(json_file)

#with open('loan_data_json.json') as jsonfile:
    #data = json.load(jasonfile)

#transforming to dataframe
loandata=pd.DataFrame(data)

#finding uniue values for the purpose column
loandata.info()
loandata['purpose'].unique()

#describe
loandata.describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get annual incme
#rem we installed numpy and imported first

loandata['income'] = np.exp(loandata['log.annual.inc'])

#working with if statements
print(loandata['fico'][0])

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'

length = len(loandata)
cat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category < 400: 
        ficocat = 'Very Poor' 
    elif category >= 601 and category < 660: 
        ficocat = 'Very Poor' 
    elif category >= 660 and category < 700: 
        ficocat = 'good'
    elif category >= 700:
        ficocat = 'excellent'
    else:
        ficocat ='unknown'
    cat.append(ficocat) #storing value of ficocat in a var
cat = pd.Series(cat) #converting list to series
loandata['fico_category']= cat

#while loop
         # i=1
         # while i<10:
         #     print(i)
         #     i+=1
     
#dfloc as conditional statement 
#df.loc[df[colunname] condition, newcolumn] = value if condition is met
loandata.loc[loandata['int.rate'] > 0.12, 'interest rate type'] = 'high'
loandata.loc[loandata['int.rate'] <= 0.12, 'interest rate type'] = 'low'

catplot = loandata.groupby(['fico_category']).size()
catplot.plot.hist(color = 'red')
plt.show
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.pie()
plt.show

#scatter plot
#say annual income against dti
xpoint = loandata['dti']
ypoint = loandata['income']
plt.scatter(xpoint,ypoint)
plt.show()

#writing to csv
loandata.to_csv('loandata.csv',index = True)
