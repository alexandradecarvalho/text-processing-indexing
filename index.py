"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Index
"""

import psutil
import os
import heapq
import time
import resource

class Index:

    def merge_files(self, out_file,final_file, i, init=0):
        print(i)
        print(init)
        with open("temp"+out_file, 'w+') as output_file:
            open_files = [open((str(n) + ".").join(out_file.split('.'))) for n in range(init,i+1)]
            output_file.writelines(heapq.merge(*open_files))
            [f.close() for f in open_files]

        [os.remove((str(n) + ".").join(out_file.split('.'))) for n in range(init,i+1)]

        with open("temp"+out_file, 'r') as temp_file, open(final_file,'w') as output_file:
            term = ""
            postings_list = dict()
            for line in temp_file:
                contents = line.split()
                if term:
                    if contents[0] == term:
                        term_content= contents[1:]
                        for term_i in term_content:
                            term_i=term_i.split(":")
                            term_info[term_i[0]]= term_info.get(term_i[0],0)+ int(term_i[1].replace(",",""))
                    else:
                        output_file.writelines(str(term_info).replace("{","").replace("}","").replace(": ",":"))
                        output_file.writelines("\n")
                        term = contents[0]
                        term_info= contents[1:]
                        term_info={item.split(":")[0]:int(item.split(":")[1].replace(",","")) for item in term_info}
                        output_file.write(contents[0] + " ")
                else:
                    term = contents[0]
                    term_info= contents[1:]
                    term_info={item.split(":")[0]:int(item.split(":")[1].replace(",","")) for item in term_info}
                    output_file.write(contents[0] + " ")

        os.remove("temp"+out_file)
                       
    def indexer(self, documents, out_file, threshold):
        init_time= time.time()
        dictionary=dict()
        npostings=0
        i=0

        for doc_id,token_list in documents.items():
            pos=0
            for token in token_list:
                if not token in dictionary: 
                    dictionary[token] = dict()
                dictionary[token][doc_id]=dictionary[token].get(doc_id,0)+1
                
                npostings+=1

            if (not threshold and psutil.virtual_memory().percent >= 90) or (threshold and npostings >= threshold) :
                sep = str(i) + "."
                output_file=open(sep.join(out_file.split('.')), "w")
                
                #writing the ordered dict in the file
                for key in sorted(dictionary.keys()):
                    output_file.write(key + " " + str(dictionary[key]).replace("{","").replace("}","").replace(": ",":") + "\n")
                
                output_file.close()
                dictionary=dict()
                npostings=0
                i+=1

        sep = str(i) + "."
        output_file=open(sep.join(out_file.split('.')), "w")
        
        #writing the ordered dict in the file
        for key in sorted(dictionary.keys()):
            output_file.write(key + " " + str(dictionary[key]).replace("{","").replace("}","").replace(": ",":") + "\n")
        
        output_file.close()

        file_threashold= resource.getrlimit(resource.RLIMIT_NOFILE)[0]//2

        #merge files
        if i < file_threashold:
            self.merge_files(out_file, out_file,i)
        else:
            j=0
            for j in range((i//file_threashold)):
                self.merge_files(out_file,(str(j) + ".").join(out_file.split('.')),(j+1)*(i//file_threashold)-1, j*(file_threashold))
            self.merge_files(out_file,(str(j+1) + ".").join(out_file.split('.')),i,(j+1)*(file_threashold))
            self.merge_files(out_file,out_file,j+1 )

        print(f'Indexing time: {time.time()-init_time} s')
        print(f'Total index size on disk: {os.path.getsize(out_file)/(1024*1024)} MB' )
        print(f'Temporary index segments: {i+1}')
        return dictionary