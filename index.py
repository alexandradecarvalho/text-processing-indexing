"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

import psutil
import os
import heapq

class Index:

    def merge_files(self, out_file, i):

        open_files=[open((str(n) + ".").join(out_file.split('.')),"r") for n in range(i+1)]
        heap=[]
        with open(out_file, "w+") as f:
            #going through the temp files
            [heapq.heappush(heap, (fi.readline(),fi)) for fi in open_files]
            
            smallest=heap.pop(0)
            smallest_word=smallest[0].split()[0]
            c_smallest_word = smallest_word
            next_line=smallest[1].readline()
            f.write(smallest[0].split()[0])
            if len(next_line)!=0:
                heapq.heappush(heap,(next_line,smallest[1]))

            while len(heap)>0:
                if c_smallest_word==smallest_word:
                    f.write("".join(smallest[0].split()[1:]))
                else:
                    f.write("\n")
                    c_smallest_word= smallest_word
                    f.write(smallest[0].split()[0])
                    f.write("".join(smallest[0].split()[1:]))
                    f.write(" ")
                  
                smallest=heap.pop(0)
                smallest_word=smallest[0].split()[0]
                next_line=smallest[1].readline()
                if len(next_line)!=0:
                    heapq.heappush(heap,(next_line,smallest[1]))

                

        [f.close() for f in open_files]

        """
            for n in range(i+1):
                sep = str(n) + "."
                filename = sep.join(out_file.split('.'))
                
                #do stuff here
                with open(filename, "r") as fi:
                    line_f=f.readline()
                    line_fi=fi.readline()
                    while line_fi:
                        while line_f and len(line_f.split())>0 and line_f.split()[0] <  line_fi.split()[0]:
                            line_f=f.readline()

                        if line_f and len(line_f.split())>0 and line_f.split()[0]== line_fi.split()[0]:
                            print(f.tell())
                            f.seek(f.tell())
                            print("".join(line_fi.split()[1:]))
                            print(line_fi.split()[0])
                            f.write("".join(line_fi.split()[1:])+"\n")
                            print(f.tell())
                        elif not line_f or len(line_f.split())==0 or  line_f.split()[0]>line_fi.split()[0]:
                            f.write(line_fi)
                        
                        line_fi= fi.readline()
                f.seek(0)

                
                #when we're done, removing it
        """
        #[os.remove((str(n) + ".").join(out_file.split('.'))) for n in range(i+1)]
                       
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
        
        output_file.close()

        #merge files
        self.merge_files(out_file, i)
        return dictionary