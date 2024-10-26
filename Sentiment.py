from skllm.config import SKLLMConfig
from datetime import datetime
from preprocess import review_clean
import pickle
import random

with open('key.txt') as keys:
    keys = keys.readlines(0)
    secret = keys[0].replace('\n','')
    org = keys[1]

OPENAI_SECRET_KEY = secret
OPENAI_ORG_ID = org

SKLLMConfig.set_openai_key(OPENAI_SECRET_KEY)
SKLLMConfig.set_openai_org(OPENAI_ORG_ID)

sentiment_classifier = pickle.load(open("weights/sentiment_classifier.pkl", 'rb'))

def get_sentiment(review: str, drugname: str):
    """predict sentiment from text review"""

    review = review_clean(review)
    sentiment = sentiment_classifier.predict(X=[review])

    if sentiment[0] == "Positive":
        rating = random.randint(7, 10)
    elif sentiment[0] == "Neutral":
        rating = random.randint(4, 6)
    elif sentiment[0] == "Negative":
        rating = random.randint(0, 3)
    else:
        rating = None

    result = {
        "drugName": drugname,
        "rating": rating, 
        "usefulCount": 0, 
        "Review_Sentiment": sentiment, 
        "review_clean": review, 
        "Year": datetime.now().year, 
        "month": datetime.now().month, 
        "day": datetime.now().day
    }

    # return new_sentiment
    return result