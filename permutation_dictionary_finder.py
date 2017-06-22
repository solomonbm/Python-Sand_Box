import os

class words_dictionary(object):
    def __init__(self, words_file):
        self.words_file = words_file
        self.words_dict = {}

    def set_words_dictionary(self):    
        if not self.words_dict:
            with open(self.words_file) as file: #"words.txt"
                for line in file: #low memory consumption iterator. even TB files can be read on a standard laptop.
                    line = line.strip() #or some other preprocessing
                    self.words_dict.setdefault(''.join(sorted(line)), []).append(line)
    
    def get_word_permutations(self, word):
        self.set_words_dictionary()
        ans = []
        sorted_word = ''.join(sorted(word))
        if sorted_word in self.words_dict.keys():
            ans = self.words_dict[sorted_word]
        return ans

def main():
    my_words_dict = words_dictionary("words.txt")
    word = 'Benji'
    print(my_words_dict.get_word_permutations(word))

if __name__ == '__main__':
    main()
    
