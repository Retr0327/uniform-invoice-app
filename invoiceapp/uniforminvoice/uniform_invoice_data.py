import re
from typing import Union
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class UniformInvoiceInfo:
    """
    The UniformInvoiceInfo object keeps track of an item in inventory, including title and winning_numbers (i.e. rewards).`
    """
    title: str
    winning_numbers: list


@dataclass
class UniformInvoiceData:
    """
    The UniformInvoiceData object finds the crucial data of the uniform-invoice webpage, namely title and winning numbers. 
    """

    soup: BeautifulSoup

    def __post_init__(self) -> None:
        self.table_tag = self.soup.find("table", class_="mytablegreen")
 
    def extract_title(self, title_tag: BeautifulSoup) -> str:
        """The extract_title method extracts the title from the html tag that stores the title data. 

        Retruns:
            a str
        """
        return title_tag.find_next("tr").text.strip()

    def extract_winning_numbers(self, winning_numbers_tag: BeautifulSoup) -> Union[str, None]:
        """The extract_winning_numbers method extracts the winning numbers from the html tag that stores the winning number data.  
        
        Returns:
            a string if the winning number is found, a None otherwise
        """
        winning_numbers = winning_numbers_tag.find(class_=re.compile(r"number|number\d")) 
        if winning_numbers:
            return winning_numbers.text.strip()

    def clean_data(self) -> UniformInvoiceInfo: 
        """The clean_data method cleans the html tags.

        Returns:
            a UniformInvoiceInfo object
        """
        title_tag = self.table_tag.find("tr", class_="htitlepink")
        winning_numbers_tag = self.table_tag.find_all("tr", class_="tr")
        data = UniformInvoiceInfo(
            title=self.extract_title(title_tag), 
            winning_numbers=map(self.extract_winning_numbers, winning_numbers_tag)
        )
        return data
