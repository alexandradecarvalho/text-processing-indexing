"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins
"""


from doc_parser import DocParser
from argparse import ArgumentParser
from tokenizer import Tokenizer
from porter_stemmer import PorterStemmer
from index import Index
from searcher import Searcher

arg_parser=ArgumentParser(prog='index creator')
arg_parser.add_argument('-f','--file',nargs=1,help='File of dataset to be used', required=True)
arg_parser.add_argument('-l','--length',nargs='?',type=int, default=3,help='Length filter default is 3 if value less than 1 the filter is disabled')
arg_parser.add_argument('-s','--stopword',nargs='?', default='stopwords.txt',help='File for stopword list if no file given no stopwords will be used')
arg_parser.add_argument('-p',help='Disable porter stemmer', action='store_false')
arg_parser.add_argument('-w',nargs='?',help='Use number of postings as threashold if flag not present default is memory usage', type=int, const=100000)
args = arg_parser.parse_args()


print("---PARSING DOCUMENTS--")
parser = DocParser(args.file[0])
contents=parser.read_file_csv()
parser.close_file()

print("---TOKENIZING DOCUMENTS--")
tokenizer = Tokenizer()
contents_tokenized= {key:tokenizer.tokenize(text, filter=args.length, option=args.stopword) for key,text in contents.items()}

print("---STEMMING TOKENS--")
stemmer = PorterStemmer()
stemmed_tokens = {docID:stemmer.stem(token_list, option=args.p) for docID,token_list in contents_tokenized.items()}

fname_out = "out.txt"

print("---INDEXING--")
index= Index()
index.indexer(stemmed_tokens, fname_out, args.w)

#print("--SEARCHER--")
#s = Searcher(fname_out)
#s.search()
