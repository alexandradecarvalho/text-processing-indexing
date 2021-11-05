"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

import psutil
import os

class Index:

    def merge_files(self, out_file, i):
        with open(out_file, "w+") as f:

            #going through the temp files
            for n in range(i+1):
                sep = str(n) + "."
                filename = sep.join(out_file.split('.'))
                
                #do stuff here
                with open(filename, "r") as fi:
                    line_f=f.readline()
                    line_fi=fi.readline()
                    while line_fi:
                        print("Linha ficheiro out:",line_f)
                        print("Linha ficheiro temp:",line_fi)
                        print(line_fi.split()[0])
                        while line_f and line_f.split()[0] <  line_fi.split()[0]:
                            line_f=f.readline()
                        
                        if line_f and line_f.split()[0]== line_fi.split()[0]:
                            pass 
                        elif not line_f or  line_f.split()[0]>line_fi.split()[0]:
                            f.write(line_fi)
                        
                        line_fi= fi.readline()
                f.seek(0)

                
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

        sep = str(i) + "."
        output_file=open(sep.join(out_file.split('.')), "w")
        
        #writing the ordered dict in the file
        for key in sorted(dictionary.keys()):
            output_file.write(key + " " + str(dictionary[key]) + "\n")
        
        output_file.close()

        #merge files
        self.merge_files(out_file, i)
        return dictionary