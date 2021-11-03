"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class PorterStemmer uses SnowballStemmer in a dictionary of documents' tokens, returning the stemmed tokens
"""


from nltk.stem.snowball import SnowballStemmer


class PorterStemmer:
    def __init__(self):
        self.snow_stemmer = SnowballStemmer(language='english')
        self.stem_words = dict()

    def stemmer(self, tokens, option="snowball"):
        if option == "snowball":
            for doc_id,token_list in tokens.items():
                for word in token_list:
                    self.stem_words[doc_id] = self.stem_words.get(doc_id, []) + [self.snow_stemmer.stem(word)]
        else:
            self.stem_words = tokens

        return self.stem_words