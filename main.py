from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk
import sys
import numpy as np
import networkx as nx
import json
import scipy.special as sp

def read_review(file_name, business_id):
    file = open(file_name, "r")
    filedata = file.readlines()
    dataset = []

    filedata = json.loads(filedata[0])
    for line in filedata:

        data = line
        # print('data', data, '\n\n')
        # print(type(data))
        if data['business_id'] == business_id:
            dataset.append(data['text'])

    return dataset

def read_sentences(file_name, business_id):
    file = open(file_name, "r")
    filedata = file.readlines()
    sentences = []

    filedata = json.loads(filedata[0])
    for line in filedata:

        data = line
        # print('data', data, '\n\n')
        # print(type(data))
        if data['business_id'] == business_id:
            text = data['text']
            tokenized_text = sent_tokenize(text)
            sentences.extend(tokenized_text)

    return sentences

def cosine_similarity(i_sentence, j_sentence, stop_words):
    i_set = {w.lower() for w in i_sentence if not w in stop_words}
    j_set = {w.lower() for w in j_sentence if not w in stop_words}

    union_vector = list(i_set.union(j_set))
    vector_size = len(union_vector)
    i_vector, j_vector = np.zeros(vector_size), np.zeros(vector_size)

    for w in union_vector:
        if w in i_set:
            i_vector[union_vector.index(w)] += 1
        if w in j_set:
            j_vector[union_vector.index(w)] += 1

    return cosine_distance(i_vector, j_vector)

def similarity_matrix(review, stop_words):
    similarity_matrix = np.zeros((len(review), len(review)))

    for i in range(similarity_matrix.shape[0]):
        for j in range(similarity_matrix.shape[1]):
            similarity_matrix[i][j] = cosine_similarity(review[i], review[j], stop_words)

    return similarity_matrix

def create_review_summary(file_name, business_id):
    stop_words = stopwords.words('english')

    sentences = read_sentences(file_name, business_id)
    reviews = read_review(file_name, business_id)
    avg_len = len(sentences) / len(reviews)

    similarity_martix = similarity_matrix(sentences, stop_words)
    similarity_graph  = nx.from_numpy_array(similarity_martix)

    page_rank = nx.pagerank(similarity_graph, alpha=0.9)
    most_similar_review_list = [(page_rank[i], sentence) for i,sentence in enumerate(sentences)]


    most_similar_review_list.sort(key=lambda tup: tup[0])
    # print(most_similar_review_list)

    output_review = ""
    for i in range(int(avg_len)):
      output_review+=most_similar_review_list[i][1]+' '

    return output_review


def main():
    file_name = sys.argv[1]
    business_id = sys.argv[2]

    review = create_review_summary(file_name, business_id)
    print(review)

# nltk.download('stopwords')
# nltk.download('punkt')
# main("yelp_dataset/review.json", "iojTeSaoPuxm4WeCzDUA6w")

if __name__ == '__main__':
    main()
