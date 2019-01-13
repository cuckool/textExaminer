import locale
import re

def open_file_simple(filename, **options):
    """

    :param filename:
    :param options:
    encoding : encoding used to read the file
    :return:
    """
    with open(file=filename, mode='r', encoding=options.get('encoding', get_default_encoding())) as f:
        content = f.readline().lower()
        while content:
            yield re.sub(pattern=r"[\W\d_]", repl=' ', string=content, flags=re.UNICODE)
            content = f.readline().lower()


def get_default_encoding():
    return locale.getpreferredencoding()


if __name__ == '__main__':
    for a in open_file_simple(filename='test.txt'):
        print(a)
