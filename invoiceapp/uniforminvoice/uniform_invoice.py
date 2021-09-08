import re
import datetime
import requests
from typing import List, Union
from bs4 import BeautifulSoup
from string import Template
from urllib.parse import urljoin
from dataclasses import dataclass
from .uniform_invoice_data import UniformInvoiceData


CURRENT_YEAR = datetime.datetime.now().year
BASE_URL = "https://invoices.com.tw/"


# --------------------------------------------------------------------
# helper functions


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


# --------------------------------------------------------------------
# public interface


@dataclass
class UniformInvoiceDataDownloader:
    """
    The UniformInvoiceDataDownloader objects downloads the data regarding the uniform invoice from the url.
    """
    month: str

    def __post_init__(self) -> None:
        self.url = urljoin(BASE_URL, f"{self.month}.html")
        self.bsObj = download_html(self.url)

    def download_data(self, name: str) -> Union[str, List[str]]:
        """The download_data method downloads the data via the object UniformInvoiceReward and UniformInvoiceTitle, and stores the data
           in a dictionary.
        
        Returns:
            a string if the `name` refers to `title` or a map object if the `name` refers to `rewards`
        """
        invoice_data = UniformInvoiceData(self.bsObj).clean_data()
        factories = {
            "title": invoice_data.title,
            "rewards": invoice_data.winning_numbers,
        }
        return factories[name]

    @property
    def claiming_date(self) -> List[str]:
        title = self.download_data("title")
        dates = re.findall(r"\d+\-\d\-\d", title)
        return dates

    @property
    def winning_numbers(self) -> dict[str, Union[str, list]:
        rewards = list(self.download_data("rewards"))
        numbers = {
            "special": rewards[0],
            "grand": rewards[1],
            "first": rewards[2].split("\n "),
            "sixth": rewards[3],
        }
        return numbers


@dataclass
class UniformInvoice:
    """
    The UniformInvoice objects shows the content of the uniform invoice webpage to the user, and let the user check whether he/she
    gets the rewards or not.
    """
    month: str

    def __post_init__(self) -> None:
        self.data = UniformInvoiceDataDownloader(self.month)
        self.claiming_date = self.data.claiming_date
        self.winning_numbers = self.data.winning_numbers

    def show_content(self) -> str:
        """The show_content method organizes and shows the content of the uniform invoice webpage.

        Returns:
            a string
        """
        content = Template(
            "$year年$first_month、$second_month月發票\n"
            "領獎時間： $claiming_date_start 至 $claiming_date_end\n"
            "1. 特別：$special\n"
            "2. 特獎：$grand\n"
            "3. 頭獎：$first\n"
            "4. 增開：$sixth"
        )

        return content.substitute(
            year=CURRENT_YEAR,
            first_month=self.month[:2],
            second_month=self.month[2:],
            claiming_date_start=self.claiming_date[0],
            claiming_date_end=self.claiming_date[-1],
            special=self.winning_numbers["special"],
            grand=self.winning_numbers["grand"],
            first=" / ".join(self.winning_numbers["first"]),
            sixth=self.winning_numbers["sixth"],
        )
 
    def check(self, number) -> str:
        """The check method checks the parameter number is the same as the winning numbers.

        Args:
            number (int): the number that the user types

        Returns:
            a string
        """
        number = str(number).strip()
        if number == self.winning_numbers["special"]:
            return "中特別獎1,000萬元"
        elif number == self.winning_numbers["grand"]:
            return "中特獎2,00萬元"
        elif number in self.winning_numbers["first"]:
            return "中頭獎20萬元"
        elif number[-3:] == self.winning_numbers["sixth"]:
            return "中增開六獎200元"
        elif number[1:] in list(map(lambda i: i[1:], self.winning_numbers["first"])):
            return "中二獎4萬元"
        elif number[2:] in list(map(lambda i: i[2:], self.winning_numbers["first"])):
            return "中三獎1萬元"
        elif number[3:] in list(map(lambda i: i[3:], self.winning_numbers["first"])):
            return "中四獎4千元"
        elif number[4:] in list(map(lambda i: i[4:], self.winning_numbers["first"])):
            return "中五獎1千元"
        elif number[5:] in list(map(lambda i: i[5:], self.winning_numbers["first"])):
            return "中六獎200元"
        return "沒有中獎"
