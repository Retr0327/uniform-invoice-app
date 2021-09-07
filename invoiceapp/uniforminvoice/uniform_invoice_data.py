import re
import bs4
from typing import Union
from bs4 import BeautifulSoup
from dataclasses import dataclass
from abc import ABC, abstractmethod


# --------------------------------------------------------------------
# abstract classes


class UniformInvoiceDownloader(ABC):
    @abstractmethod
    def find_in_html(self):
        pass

    @abstractmethod
    def extract_data(self, specified_tag: BeautifulSoup):
        pass

    def clean_data(self):
        pass


# --------------------------------------------------------------------
# public interface


@dataclass
class UniformInvoiceReward(UniformInvoiceDownloader):
    """
    The UniformInvoiceReward object finds the uniform-invoice winning numbers.
    """

    soup: BeautifulSoup

    def find_in_html(self) -> Union[bs4.Tag, bs4.element.NavigableString]:
        """The find_in_html method scans the entire html looking for results of a html tag.

        Return:
            a bs4.Tag or bs4.element.NavigableString
        """
        return self.soup.find("table", class_="mytablegreen")

    def extract_data(self, specified_tag: BeautifulSoup) -> Union[str, None]:
        """The extract_data method extracts the data from the html.

        Args:
            specified_tag (BeautifulSoup): the specified html tag

        Returns:
            a string if the winning number is found, a None otherwise
        """
        rewards = specified_tag.find(class_=re.compile("number|number\d"))
        if rewards:
            return rewards.text.strip()

    def clean_data(self) -> filter:
        """The clean_data method cleans the html tags.

        Returns:
            a filter object
        """
        table_tag = self.find_in_html()
        tr_lists = table_tag.find_all("tr", class_="tr")
        return map(self.extract_data, tr_lists)


@dataclass
class UniformInvoiceTitle(UniformInvoiceDownloader):
    """
    The UniformInvoiceTitle finds the title of the webpage, including the reward date and the claiming date.
    """

    soup: BeautifulSoup

    def find_in_html(self) -> Union[bs4.Tag, bs4.element.NavigableString]:
        """The find_in_html method scans the entire html looking for results of a html tag.

        Return:
            a bs4.Tag or bs4.element.NavigableString
        """
        return self.soup.find("table", class_="mytablegreen")

    def extract_data(self, specified_tag: BeautifulSoup) -> str:
        """The extract_data method extracts the data from the html.

        Args:
            specified_tag (BeautifulSoup): the specified html tag

        Returns:
            a string if the winning number is found, a None otherwise
        """
        receipt_info = specified_tag.find_next("tr")
        return receipt_info.text.strip()

    def clean_data(self) -> map:
        """The clean_data method cleans the html tags.

        Returns:
            a map object
        """
        table_tag = self.find_in_html()
        tr_lists = table_tag.find("tr", class_="htitlepink")
        return map(self.extract_data, tr_lists)
