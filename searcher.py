"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins

Class Searcher loads the dictionary from the disk, and its search function receives a term and returns its total frequency
"""


from os import posix_fadvise


class Searcher:

    def __init__(self, index_file):
        self.frequencies = dict()

        f = open(index_file, 'r')

        for line in f:
            dict_entry = line.strip().split()
            postings_list = "".join(dict_entry[1:])
            sum = 0
            print(type(postings_list))
            for tup in eval(postings_list):
                sum += tup[1]

            self.frequencies[dict_entry[0]] = self.frequencies.get(dict_entry[0],0) + sum

        f.close()

    def search(self):
        while True:
            inpt = input("search: ")
            if not inpt:
                break

            if inpt in self.frequencies:
                print(self.frequencies[inpt])
            else:
                print(0)