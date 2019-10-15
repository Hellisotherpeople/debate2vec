import glob
import os
from bs4 import BeautifulSoup
import bs4
import string
import flair
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.embeddings import WordEmbeddings, FlairEmbeddings, StackedEmbeddings, DocumentPoolEmbeddings, BertEmbeddings, ELMoEmbeddings
import torch
# create a StackedEmbedding object that combines glove and forward/backward flair embeddings
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_similarity_score
#import numpy as np
from docx import Document
import sys
import numpy as np
from itertools import islice
from collections import deque
import sys
from sklearn.externals import joblib
import nltk

def parse_string(s):
    ret_str = ""
    if s:
        s_list = s.split()
        for c in s_list:
            to_test = c.lower().strip(string.punctuation)
            if to_test:
                ret_str += to_test
                ret_str += " "
        return ret_str



    #return ''.join(c for c in s.lower() if c.isalnum() or c.isspace())

print(parse_string("this * is * a - string_example"))

num_of_cards = 1
os.chdir("/home/lain/CX_DB8/card_data")

card_set = set()

cards = dict()
with open('debate2vec.txt', 'a') as f:
    for file in glob.glob("*.html5"):
        print("File parsed: " + file)
        with open(file) as fp:
            soup = BeautifulSoup(fp, "lxml")
            all_card_tags = soup.find_all('h4')
            print(num_of_cards)
            for h4 in all_card_tags:
                try:
                    card_str = parse_string(h4.find_next("p").find_next("p").text)
                    #print(card_str)
                    if card_str:
                        if len(card_str) >= 200:
                            if card_str not in card_set:
                                card_set.add(card_str)
                                num_of_cards += 1
                                f.write(card_str)
                                f.write("\n")
                except AttributeError:
                    pass

#joblib.dump(cards, "card_dict.joblib")
print("written to disk!")
print("Number of cards processed: " + str(num_of_cards))

