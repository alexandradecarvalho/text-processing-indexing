"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class DocParser opens a tsv file and reads it returning a dictionary 
with review_id as key and review_headline and review_body as values
"""


import csv  

class DocParser:

    def __init__(self, filename):
        self.file=open(filename, "r")
        self.doc_contents=dict()
    
    def read_file_csv(self):
        reader=csv.DictReader(self.file, delimiter="\t", quoting=csv.QUOTE_NONE)
        
        for row in reader:
            self.doc_contents[row['review_id']]= {'review_headline':row['review_headline'], 'review_body':row['review_body']}
        
        return self.doc_contents

    
    def close_file(self):
        self.file.close()
