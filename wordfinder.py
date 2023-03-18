"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    def __init__(self,address):
        self.address=address
        self.words=[]
        for line in open(address, 'r'):
            self.words.append(line.replace('\n', ''))
        print(f'{len(self.words)} words read.')
        
    def random(self):

        return self.words[randint(1,len(self.words))]
