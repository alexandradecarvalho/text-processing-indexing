class DocParser:

    def __init__(self, filename):
        self.file=open(filename, "r")
    
    def read_file(self):
        return self.file.read()
    
    def close_file(self):
        self.file.close()
