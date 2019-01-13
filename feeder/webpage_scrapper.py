import requests
from lxml import html

def get_webpage_content(url: str, auth: tuple = False):
    """

    :param url:
    :param auth: ('username', 'password')
    :return:
    """
    req = requests.get(url=url, auth=auth) if auth else requests.get(url=url)
    for line in html.fromstring(req.content).text_content().splitlines():
        yield line


if __name__ == '__main__':
    for a in get_webpage_content('https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string'):
        print(a)