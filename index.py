"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

class Index:

    def indexer(self, documents, out_file):
        dictionary=dict()
        output_file=open(out_file, "w")

        for doc_id,token_list in documents.items():
            pos=0
            for token in token_list:
                if token in dictionary:
                    dictionary[token].add((doc_id, pos))
                else:
                    dictionary[token]= {(doc_id,pos)}
                pos+=1
        output_file.write(str(dictionary))
        return dictionary

