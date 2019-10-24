from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import pandas as pd
import json

def read_article(file_name):
    total_words, total_sentences, total_reviews = 0, 0, 0
    with open(file_name, 'r') as f:
        for line in f:
            data = json.loads(line)
            total_reviews += 1
            total_words += len(data['text'].split())
            total_sentences += data['text'].count('.')
        print("Total Reviews: %i\n Total Words: %i\n Total Sentences: %i\n" % (total_reviews, total_words, total_sentences))
        print("Avg #Word/Review: %i\n Avg #Sentence/Review: %i" % (total_words/total_reviews, total_sentences/total_reviews))

    total_business, total_reviews = 0, 0
    with open("dataset/yelp_dataset/business.json", 'r') as f:
        for line in f:
            data = json.loads(line)
            total_business += 1
            total_reviews += data['review_count']
        print("Total Businesses: %i\n Avg #Review/Business: %i" % (total_business, total_reviews/total_business))


def gather_all_business_reviews(dataset):
    for dab in dict.items(dataset):
        if dab['business_id'] == "1SWheh84yJXfytovILXOAQ":
            print (dab['business_id'])

read_article("dataset/yelp_dataset/review.json")
