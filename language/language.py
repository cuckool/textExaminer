"""This file will show you the structures that the language files are supposed to present in order to be used by the
processing module."""

# way 1
languageName_words = {"word_1": "category_1", "word_2": "category _2"}

class Language:
    """Word category must be a tuple containing words (str) and not begin by '__'.
    See the exemple below:
    category_1 = ("word_11", "word_12", "word_13")
    category_2 = ("word_21", "word_22", "word_23")
    """

    @classmethod
    def get_frozenset(cls):
        """Iterate the tuple of the class, then create a global frozenset with all the words in the class, following
        this structure : word : word_category"""
        word_dict = dict()
        for attr, value in cls.__dict__.items():
            if attr[:2] != '__' and isinstance(value, tuple):
                #print(attr, value)
                for w in value:
                    word_dict[w] = attr
        return word_dict





# # way 2
# class Language:
#     category_1 = frozenset(["word81", "word_2"])
#     category_2 = frozenset(['word_3', 'word_4'])
#
#     @classmethod
#     def get_words(cls):
#         for k, value in vars(cls).items():
#             if isinstance(value, frozenset):
#                 print(value)
#
# #search global frozenset, if in there, search in sub frozenset
#
if __name__ == '__main__':
    print(Language.get_frozenset())


# choose the right datastructures : http://matthewrocklin.com/blog/work/2017/11/03/data-structure-benchmark
# some infos on Python datastructures : https://www.quora.com/Which-data-structure-is-the-fastest-in-Python