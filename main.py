"""
Information Retrieval Assignment 1 2021/2022
Authors: Alexandra Carvalho, Margarida Martins
"""


from doc_parser import DocParser
from argparse import ArgumentParser
from Tokenizer import Tokenizer
from index import Index

arg_parser=ArgumentParser(prog='index creator')
arg_parser.add_argument('-f','--file',nargs=1,help='File of dataset to be used', required=True)
arg_parser.add_argument('-l','--length',nargs='?',type=int, default=3,help='Length filter default is 3 if value less than 1 the filter is disabled')
arg_parser.add_argument('-s','--stopword',nargs='?', default='stopwords.txt',help='File for stopword list if no file given no stopwords will be used')
arg_parser.add_argument('-p',help='Disable porter stemmer', action='store_false')
args = arg_parser.parse_args()


parser = DocParser(args.file[0])
contents=parser.read_file_csv()
parser.close_file()

tokenizer = Tokenizer()
contents_tokenized= {key:tokenizer.tokenize(text['review_body'])+tokenizer.tokenize(text['review_headline']) for key,text in contents.items()}

index= Index()
print(index.indexer(contents_tokenized, "out.txt"))
