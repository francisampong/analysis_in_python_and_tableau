# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:19:58 2024

@author: nanab
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

#reading slsx files
data = pd.read_excel('articles.xlsx')
data.info()
data.describe()

#counting the nmbr of articles per source
#format: df.groupby[('column to group')][colm to count].count()/sum()
data.groupby(['source_id'])['article_id'].count()

#adding nmbr of reactions by publisher
data.groupby(["source_id"])['engagement_reaction_count'].sum()

#dropping a colm
data = data.drop('engagement_comment_plugin_count', axis = 1)

#creating functions in python
#deh functionname():
    #what to do
    
#funtion to creat/return a variable

def aboutme(name):
    print('my name is: '+ name)
    return name #without return python wil creat val buh return no value n type
me = aboutme('Francis') #you have to also assign function

#for loop in funtion]

def favfood(food):
    for x in food:
        print('mekondo ' + x)
    
myfood = ('bankye', 'konkonte', 'banku')
favfood(myfood)


#for forloop to creat column, yu need to declare first
#extracting keyword in data
keyflag = []
keyword = 'crash'
#col_len = len(data) 
for x in range(0,10):
    col=data['title'][x]
    if keyword in col:
        code = 1
    else:
        code = 0
    keyflag.append(code)
    
# #creating funtion
# keyflag = []
# def keyword_flag(keyword):
#     for x in range(0,10):
#         col=data['title'][x]
#         if keyword in col:
#             code = 1
#         else:
#             code = 0
#         keyflag.append(code) 
#     return keyflag
# k = keyword_flag('government')

#doing for all
keyflag = []
col_len = len(data)
def keyword_flag(keyword):
    for x in range(0,col_len):
        col=data['title'][x]
        try:    
            if keyword in col:
                code = 1
            else:
                code = 0
        except:
            code = 0
        keyflag.append(code) 
    return keyflag
k = keyword_flag('murder')
data['keyword_flag'] = pd.Series(keyflag)

#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']




#adding a for loop to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = [] 
title_neu_sentiment = []
length = len(data)
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores (text)
        neg = sent ['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg) 
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment) 
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)
data['title_neg_sentiment'] = title_neg_sentiment 
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment
#writing the data
data.to_excel('blogme_clean.xlsx', sheet_name='bloghedata', index=False)


