from bertopic import BERTopic
from preprocess import review_clean_lematize, review_clean
from datetime import datetime

# Load the topic model
topic_model = BERTopic.load("weights/contraceptive_topic_model")	

import warnings
warnings.filterwarnings("ignore")

def get_topic(review: str):
    
    review_cleaned = review_clean_lematize(review)

    similar_topics, similarity = topic_model.find_topics(review_cleaned, top_n=1)

    Cluster1 = [17, 1, 9, 15] # Acne
    Cluster2 = [4, 2, 7] # Implants
    Cluster3 = [0, 14, 5] # Adverse effects
    all = Cluster1 + Cluster2 + Cluster3
    Cluster4 = [n for n in range(20) if n not in all] # Weight

    topic = similar_topics[0]

    if topic == -1:
        topic_text = None
    elif topic in Cluster1:
        topic_text = "Acne"
    elif topic in Cluster2:
        topic_text = "Implants"
    elif topic in Cluster3:
        topic_text = "Adverse effects"
    elif topic in Cluster4:
        topic_text = "Weight"
    else:
        pass

    result = {
        "review_clean": review_clean(review), 
        "Year": datetime.now().year, 
        "month": datetime.now().month, 
        "day": datetime.now().day, 
        "topics": topic_text
    }

    return result