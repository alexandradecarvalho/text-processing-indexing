"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

import psutil
import os
import heapq
import time

class Index:

    def merge_files(self, out_file, i):
        with open("temp"+out_file, 'w') as output_file:
            open_files = [open((str(n) + ".").join(out_file.split('.'))) for n in range(i+1)]
            output_file.writelines(heapq.merge(*open_files))
            [f.close() for f in open_files]

        [os.remove((str(n) + ".").join(out_file.split('.'))) for n in range(i+1)]

        with open("temp"+out_file, 'r') as temp_file, open(out_file,'w') as output_file:
            term = ""
            postings_list = dict()
            for line in temp_file:
                contents = line.split()
                if term:
                    if contents[0] == term:
                        postings_list[term] = postings_list.get(term, []) + [eval("".join(contents[1:]))]
                    else:
                        output_file.write(str(postings_list)+"\n")
                        term = contents[0]
                        postings_list = dict()
                        postings_list[term] = [eval("".join(contents[1:]))]
                else:
                    term = contents[0]
                    postings_list[term] = [eval("".join(contents[1:]))]
            output_file.writelines(str(postings_list)+"\n")

        os.remove("temp"+out_file)
                       
    def indexer(self, documents, out_file, threshold):
        init_time= time.time()
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
                    output_file.write(key + " " + str(dictionary[key]).replace("{","").replace("}","") + "\n")
                
                output_file.close()
                dictionary=dict()
                npostings=0
                i+=1

        sep = str(i) + "."
        output_file=open(sep.join(out_file.split('.')), "w")
        
        #writing the ordered dict in the file
        for key in sorted(dictionary.keys()):
            output_file.write(key + " " + str(dictionary[key]).replace("{","").replace("}","") + "\n")
        
        output_file.close

        #merge files
        self.merge_files(out_file, i)

        print(f'Indexing time: {time.time()-init_time} s')
        print(f'Total index size on disk: {os.path.getsize(out_file)/(1024*1024)} MB' )
        print(f'Temporary index segments: {i}')
        return dictionary