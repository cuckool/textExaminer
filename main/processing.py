import operator
import re

class WordCounter:
    def __init__(self, words: bool, letters: bool):
        self.processing_function = []
        if words is True:
            self.words = dict()
            self.processing_function.append(self.words_counting)
        if letters is True:
            self.letters = dict()
            self.processing_function.append(self.letters_counting)

    def process(self, line):
        #to clean the inputs
        line = re.sub(pattern=r"[\W\d_]", repl=' ', string=line, flags=re.UNICODE)
        for func in self.processing_function:
            func(line[:])


    # ajouter liste de mots : articles... pour chopper les noms propres et companie
    def words_counting(self, line):
        """
        Add the words in line to the dictionnary. Line must be stripped from ponctuation and numbers. Only letters must
        remain.
        """
        for w in line.split():
            if w in self.words:
                self.words[str(w)] += 1
            else:
                self.words[str(w)] = 1
#METTRE LES COUNTINGS EN PRIVATE !!!!
    def letters_counting(self, line):
        """
        Add the letters in line to the dictionnary. Line must be stripped from ponctuation and numbers. Only letters must
        remain.
        """
        for le in line.replace(r' ', ''):
            if str(le) in self.letters:
                self.letters[str(le)] += 1
            else:
                self.letters[str(le)] = 1

    def get_sorted_letters(self):
        return sorted(self.letters.items(), key=operator.itemgetter(1), reverse=True)

    def get_sorted_words(self):
        return sorted(self.words.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    boi = WordCounter()

