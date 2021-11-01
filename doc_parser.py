import csv  

class DocParser:

    def __init__(self, filename):
        self.file=open(filename, "r")
    
    def read_file_csv(self):
        return csv.DictReader(self.file,  dialect='unix')
    
    def close_file():
        self.file.close()
