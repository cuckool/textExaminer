import main.processing
import feeder.txt_opening

if __name__ == '__main__':
    processeur = main.processing.WordCounter(words=True, letters=True)
    for line in feeder.txt_opening.open_file_simple(r'D:\boi\PyCharm Programs\textProcessing\bible.txt'):
        processeur.process(line)
    print(processeur.get_sorted_letters())
    print(processeur.get_sorted_words())




    #chopper des mots depuis twitter, depuis site web, depuis txt et autre format doc