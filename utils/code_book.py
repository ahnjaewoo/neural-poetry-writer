import codecs
import numpy as np

# represent character as a number, vector
# 
class code_book():
    def __init__(self):
        self.vector_size = 0
        self.codes = dict()
    # gather - if given character is unknown, create mapping and add it to codes
    def gather(self, character):
        if(self.codes.get(character) == None):
            self.codes[character] = self.vector_size
            self.vector_size += 1
    # save to a file with specific format, use codes
    def save_to(self, filename):
        f = codecs.open(filename, "w", 'utf-8')
        codes = self.codes
        for key, value in codes.items():
            f.write(key+str(value)+'\n')
        f.close()
    # load from a file of format assumption, form codes
    def load_from(self, filename):
        self.codes.clear()
        f = codecs.open(filename, "r", 'utf-8')
        lines = f.readlines()
        for value in lines:
            self.codes[value[0]] = int(value[1:-1])
        f.close()
    # get numpy vector representation of string, based on codes
    def get_vectors(self, text):
        text_num = [self.codes[character] for character in text]
        vectors = np.zeros((len(text), self.vector_size))
        for i in range(len(text)):
            vectors[i][text_num[i]] = 1
        return vectors
    # length of a vector (=vector size)
    def size(self):
        return self.vector_size
    # debug purpose only
    def debug_print(self):
        print(self.vector_size)
        print(self.codes)
        