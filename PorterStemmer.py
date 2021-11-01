from nltk.stem.snowball import SnowballStemmer

class PorterStemmer:
    def __init__(self):
        self.snow_stemmer = SnowballStemmer(language='english')
        self.stem_words = []

    def stemmer(self, tokens, option="snowball"):
        if option == "snowball":
            for word in tokens:
                self.stem_words += [self.snow_stemmer.stem(word)]
        else:
            self.stem_words = tokens
            
        return self.stem_words