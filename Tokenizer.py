import re

class Tokenizer:

    def __init__(self):
        self.stopwords = {}
        self.token_list = []

    def word_split(self, doc):
        return doc.split("[\\p{Punct}\\s]+")

    def tokenize(self, doc, option = ""):
        if not option:
            try:
                f = open('stopwords.txt','r')
                self.stopwords = f.readlines()
            except IOError:
                self.stopwords = {'a', 'the', 'is', 'are', 'who', 'i', 'a', 'an'}
        elif option == "not":
            self.stopwords = {}
        else:
            self.stopwords = option # TBD: is option passed as a set?? isn't it a string?? in that case, does the string has brackets??

        text_tokens = re.split('\W+', doc)

        tokens_without_sw = [word for word in text_tokens if not word in self.stopwords]

        return tokens_without_sw

        