import requests
from bs4 import BeautifulSoup


def download_html(url: str) -> BeautifulSoup:
    """The download_html method downloads the html tree based on the argument `url`.
    Args:
        url (str): the url that users want to scrap
    Returns:
        a BeautifulSoup object
    """

    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "lxml")
    return soup
