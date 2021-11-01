import re

class Tokenizer:

    def __init__(self):
        self.stopwords = {}
        self.token_list = []

    def tokenize(self, doc, filter = 3, option = ""):
        ##### CREATING STOPWORDS LIST #####
        if not option:
            try:
                f = open('stopwords.txt','r')
                self.stopwords = f.readlines()
            except IOError:
                self.stopwords = {'a', 'the', 'is', 'are', 'who', 'i', 'a', 'an'}
        elif option == "disable":
            self.stopwords = {}
        else:
            self.stopwords = set(option.replace('{','').replace('}','').replace(' ','').split(','))

        ##### SPLITTING BY SPACES AND PUNCTUATION #####
        text_tokens = re.split('\W+', doc)
        
        ##### FILTERING SMALL WORDS #####
        try:
            length_threshold = int(filter)
        except ValueError:
            if filter != "disable":
                length_threshold = 3 #default
            else:
                length_threshold = 0
        
        self.token_list = [word for word in text_tokens if len(word) > length_threshold and not word in self.stopwords]

        return self.token_list

