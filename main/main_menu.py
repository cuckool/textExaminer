import main.processing
import feeder.webpage_scrapper, feeder.txt_opening
import visual.wordcloud

if __name__ == '__main__':
    processeur = main.processing.WordCounter(words=True, letters=True)
    for line in feeder.txt_opening.open_file_simple(r'D:\boi\PyCharm Programs\textProcessing\bible.txt'):
    # for line in feeder.webpage_scrapper.get_webpage_content('https://lxml.de/lxmlhtml.html'):
        processeur.process(line)
    res = processeur.get_frequency()
    print(res[0])
    print(res[1])
    visual.wordcloud.display_cloud(res[0], width=2000, height=2000, background_color="black")




    #chopper des mots depuis twitter, depuis site web, depuis txt et autre format doc