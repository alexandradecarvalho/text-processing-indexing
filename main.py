from doc_parser import DocParser

parser = DocParser("datasets/amazon_reviews_us_Digital_Video_Games_v1_00.tsv")
contents=parser.read_file_csv()
parser.close_file()
print(contents)