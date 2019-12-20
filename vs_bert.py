from summarizer import Summarizer
from main import create_review_summary, read_review, read_sentences
import sys
import numpy as np


bert_model = Summarizer()


def bert_summarize(file_name, business_id):
    all_reviews = read_review(file_name, business_id)
    all_sentences = read_sentences(file_name, business_id)
    avg_len = len(all_sentences) / len(all_reviews)
    
    big_review = ' '.join(all_reviews)
    ratio = avg_len/len(all_sentences)
    result = bert_model(big_review, ratio=ratio)
    full = ''.join(result)
    return full

def main():
    
    file_name = sys.argv[1]
    business_id = sys.argv[2]

    all_reviews = read_review(file_name, business_id)

    our_review = create_review_summary(file_name, business_id)
    bert_review = bert_summarize(file_name, business_id)
    random_review = np.random.choice(all_reviews)

    print('our review: \n', our_review, '\n')
    print('bert review: \n', bert_review, '\n')
    print('real review: \n', random_review, '\n')


if __name__ == '__main__':
    main()