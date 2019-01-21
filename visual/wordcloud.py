from wordcloud import WordCloud
import matplotlib.pyplot as plt

# This a part of this file is taken from the matplotlib exemple on how to use Wordcloud
# https://python-graph-gallery.com/260-basic-wordcloud/


def display_cloud(data, width=480, height=480, margin=0, background_color="white", max_words=1000):
    """data should be a list/tuple with the following structure :
    ((obj_1 : number of occurences), (obj_2 : number of occurences))"""
    # Create the wordcloud object
    wordcloud = WordCloud(width=width, height=height, margin=margin, background_color=background_color,
                          max_words=max_words)
    wordcloud.generate_from_frequencies(dict(data))

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()