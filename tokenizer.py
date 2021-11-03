"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Tokenizer tokenizes each document of a given corpus, filtering small words, stopwords, 
spaces and punctuation and returns a list of tokens
"""


import re


class Tokenizer:

    def __init__(self):
        self.stopwords = {}
        self.token_lists = dict()

    def tokenize(self, docs, filter = 3, option = ""):

        ##### CREATING STOPWORDS LIST #####
        if not option:
            try:
                f = open('stopwords.txt','r')
                self.stopwords = f.readlines()
                f.close()
            except IOError:
                self.stopwords = {'a', 'the', 'is', 'are', 'who', 'i', 'a', 'an'}
        elif option == "disable":
            self.stopwords = {}
        else:
            self.stopwords = set(option.replace('{','').replace('}','').replace(' ','').split(','))

        ##### FILTERING SMALL WORDS #####
        try:
            length_threshold = int(filter)
        except ValueError:
            if filter != "disable":
                length_threshold = 3 #default
            else:
                length_threshold = 0

        ##### SPLITTING BY SPACES AND PUNCTUATION #####
        for id,doc in docs.items():
            text_tokens = re.split('\W+', doc['review_headline']) + re.split('\W+', doc['review_body']) 
            self.token_lists[id] = [word for word in text_tokens if len(word) > length_threshold and not word in self.stopwords]

        return self.token_lists

