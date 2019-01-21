import operator
import re


class WordCounter:
    def __init__(self, words: bool, letters: bool):
        self.processing_function = []
        if words is True:
            self.words = dict()
            self.processing_function.append(self.words_counting)
            self.words_nb = 0
            self.sorted_words = []
        if letters is True:
            self.letters = dict()
            self.processing_function.append(self.letters_counting)
            self.letters_nb = 0
            self.sorted_letters = []

    def process(self, line):
        # to clean the inputs
        line = re.sub(pattern=r"[\W\d_]", repl=' ', string=line, flags=re.UNICODE)
        for func in self.processing_function:
            func(line[:])

    # ajouter liste de mots : articles... pour chopper les noms propres et companie
    def words_counting(self, line):
        """
        Add the words in line to the dictionnary. Line must be stripped from ponctuation and numbers. Only letters must
        remain.
        """
        for w in line.lower().split():
            self.words_nb += 1
            if w in self.words:
                self.words[str(w)] += 1
            else:
                self.words[str(w)] = 1
# METTRE LES COUNTINGS EN PRIVATE !!!!

    def letters_counting(self, line):
        """
        Add the letters in line to the dictionnary. Line must be stripped from ponctuation and numbers. Only letters must
        remain.
        """
        for le in line.lower().replace(r' ', ''):
            self.letters_nb += 1
            if str(le) in self.letters:
                self.letters[str(le)] += 1
            else:
                self.letters[str(le)] = 1

    def get_sorted_letters(self):
        if not self.sorted_letters:
            self.sorted_letters = tuple(sorted(self.letters.items(), key=operator.itemgetter(1), reverse=True))
        return self.sorted_letters

    def get_sorted_words(self):
        if not self.sorted_words:
            self.sorted_words = tuple(sorted(self.words.items(), key=operator.itemgetter(1), reverse=True))
        return self.sorted_words

    def get_frequency(self):
        results = []
        if self.words_counting in self.processing_function:
            if not self.words:
                print("You should feed the processor first!")
                return 1
            if not self.sorted_words:
                self.get_sorted_words()
            results.append(self.frequency_in_list(self.get_sorted_words(), self.words_nb))
        if self.letters_counting in self.processing_function:
            if not self.letters:
                print("You should feed the processor first!")
                return 1
            if not self.sorted_letters:
                self.get_sorted_letters()
            results.append(self.frequency_in_list(self.get_sorted_letters(), self.letters_nb))
        return results

    def frequency_in_list(self, data, total):
        """A function that should be called only by the get_frequency() method. Data is the list/tuple that will be used,
        it form should be the following : ((obj_1 : number of occurences), (obj_2 : number of occurences)). Total is the
        addition of all the occurences."""
        freq_data = []
        for ob, occ in data:
            freq_data.append((ob, occ/total))
        return tuple(freq_data)



if __name__ == '__main__':
    boi = WordCounter(words=True, letters=False)
    if boi.letters:
        print('boi.letters')
    if boi.words:
        print('boi.words')
    boi.process("bonjour c'est pour un test, hola senor")
    if boi.letters:
        print('boi.letters')
    if boi.words:
        print('boi.words')