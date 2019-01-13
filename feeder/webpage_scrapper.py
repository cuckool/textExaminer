import requests


def get_webpage_content(url: str, auth: tuple = False):
    """

    :param url:
    :param auth: ('username', 'password')
    :return:
    """
    req = requests.get(url=url, auth=auth) if auth else requests.get(url=url)
    return req.text, req.json()


if __name__ == '__main__':
    a = get_webpage_content('https://fr.wikipedia.org/wiki/Samuel_L._Jackson')
    print(a)