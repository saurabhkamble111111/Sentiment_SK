import numpy as np # linear algebra
import pandas as pd # data processing,
import os
from sentiment_of_text import sentiment_of_text
#from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
# dfx=pd.DataFrame()
# dfx["sentences"]=pd.DataFrame(aa)
# dfx["url"]=bb
# dfx = dfx[['url','sentences']]
def sentiment_on_complete_article(docs,article_number):
    
    # dfx=pd.DataFrame()
    pp=sentiment_of_text([docs])
    x1=pp[0]
    print(pp[0])
# #     aa1=sent_tokenize(docs)
# #     print(aa1)
# #     sentence_sentiment_evaluation=[]
# #     sentence_sentiment_score=[]
# #     for iii in range(len(aa1)):
# #         x1,x2=sentiment_of_text(aa1[iii])
# # #         print(x1)
# # # -       print(x2)
# #         sentence_sentiment_evaluation.append(str(x1))
# #         sentence_sentiment_score.append(str(x2))

# #     # print(aa1)
# #     # print(sentence_sentiment_evaluation)

    
#     # dfx.loc[:]['Ids'] = 'foo'
#     # dfx["segBody"]=pd.DataFrame(aa1)
#     dfx["sentiment"]=x1
#     dfx["segID"]=str(article_number)
#     dfx["confidenceScore"]=x2
#     dfx=dfx.loc[:,["segID","sentiment","confidenceScore"]]
#     pp=len(dfx.loc[dfx['sentiment'] == 'POS'])-len(dfx.loc[dfx['sentiment'] == 'NEG'])
#     if pp>0:
#         overall_sentiment='POS'
#     elif(pp<0):
#         overall_sentiment='NEG'
#     else:
#         overall_sentiment='NEU'
    
    # df_masterxx_neg=df_masterxx.loc[df_masterxx['sentiment'] == 'neg']
    # df_masterxx_neu=df_masterxx.loc[df_masterxx['sentiment'] == 'neu']
    return {"articleID" :article_number,"articleSentiment" :x1}

    

# # posts_title=['','','']
# # df1 = pd.DataFrame({'posts_title':posts_title,'posts_text':posts_text})
# # print (df1)
# # A1,A2,A3=
# text='''I like pizza. I hate pizza.'''
# print(sentiment_on_complete_article(text,10))
