"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

import psutil
import os

class Index:

    def write_to_disk(self, out_file, i):
        with open(out_file, "r+") as f:

            #going through the temp files
            for n in range(i):
                sep = str(i) + "."
                filename = sep.join(out_file.split('.'))

                #do stuff here
                with open(filename, "r") as fi:
                    for line in f:
                        element = line.split()[0]
                        while element > fi.split()[0]:  
                            pass
                
                #when we're done, removing it
                os.remove(filename)
                       
    def indexer(self, documents, out_file, threshold):
        
        dictionary=dict()
        npostings=0
        i=0

        for doc_id,token_list in documents.items():
            pos=0
            for token in token_list:
                if token in dictionary:
                    dictionary[token].add((doc_id, pos))
                else:
                    dictionary[token] = {(doc_id,pos)}
                pos+=1
                npostings+=1

            if (not threshold and psutil.virtual_memory().percent >= 90) or (threshold and npostings >= threshold) :
                sep = str(i) + "."
                output_file=open(sep.join(out_file.split('.')), "w")
                
                #writing the ordered dict in the file
                for key in sorted(dictionary.keys()):
                    output_file.write(key + " " + str(dictionary[key]) + "\n")
                
                output_file.close()
                dictionary=dict()
                npostings=0
                i+=1

        #merge files
        self.write_to_disk()
        return dictionary