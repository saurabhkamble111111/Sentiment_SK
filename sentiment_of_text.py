# from happytransformer import HappyTextToText
# happy_tt1 = HappyTextToText("BERT", "sshleifer/distilbart-cnn-12-6")
from transformers import pipeline


sentiment_analyzer=pipeline("sentiment-analysis",model = "finiteautomata/bertweet-base-sentiment-analysis")
# sentiment_analyzer=pipeline("sentiment-analysis",model = "distilbert-base-cased")
# sentiment_analyzer=pipeline("sentiment-analysis",model = "distilroberta-base")
# sentiment_analyzer=pipeline("sentiment-analysis",model = "distilbert-base-multilingual-cased")
# sentiment_analyzer=pipeline("sentiment-analysis",model = "distilbert-base-uncased-distilled-squad")
# sentiment_analyzer=pipeline("sentiment-analysis",model = "distilgpt2")


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
stopwords=list(STOP_WORDS)
nlp=spacy.load('en_core_web_sm')
import pandas as pd
import re
def sentiment_of_text(docs):
    # try:
        # print(docs)
        # print(type(docs))
        # docs = re.sub(r'[^A-Za-z. 0-9, ?]+', ' ',docs[0])
        # docs=[docs]
        result=sentiment_analyzer(docs)
        print(">>>>>Recd results")
        adict=result[0]
        print(">>>>>Recd adict")
        senti_label=adict['label']
        senti_value=adict['score']
        # print(senti_label)
        # print(senti_value)
        output1=senti_label
        output2=senti_value
    # except Exception as e: 
    #     print(e)
    #     print("It has gone to except.")
    #     output1="NEU"
    #     output2=0.5
        return output1,output2

