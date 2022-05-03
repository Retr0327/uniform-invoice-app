import re
import pydantic
from typing import Any, Union
from bs4 import BeautifulSoup
from dataclasses import dataclass


class UniformInvoiceDataInfo(pydantic.BaseModel):
    """
    The UniformInvoiceDataInfo object keeps track of an item in inventory, including invoice_year, claiming_date, and winning_numbers.`
    """

    invoice_year: str
    claiming_date: str
    winning_numbers: Any

    @pydantic.validator("invoice_year")
    @classmethod
    def has_year(cls, value) -> str:
        """The has_year method makes sure there is `invoice_year` value definied."""
        if not value:
            raise Exception("No invoice year defined!")

        return value

    @pydantic.validator("claiming_date")
    @classmethod
    def has_claiming_date(cls, value) -> str:
        """The has_year method makes sure there is `claiming_date` value definied."""
        if not value:
            raise Exception("No claiming_date defined!")

        return value


@dataclass
class UniformInvoiceDownloader:
    """
    The UniformInvoiceData object finds the crucial data of the uniform-invoice webpage, namely title and winning numbers.
    """

    soup: BeautifulSoup

    def __post_init__(self) -> None:
        self.table_tag = self.soup.find(
            "table", class_=re.compile(r"mytable(green|pink|purple)")
        )

    def extract_claiming_date(self, title_tag: BeautifulSoup) -> str:
        """The extract_title method extracts the claiming date from the html tag that stores the claiming date data.

        Retruns:
            a str
        """
        return title_tag.find_next("tr").text.strip()

    def extract_winning_numbers(
        self, winning_numbers_tag: BeautifulSoup
    ) -> Union[str, None]:
        """The extract_winning_numbers method extracts the winning numbers from the html tag that stores the winning number data.

        Returns:
            a string if the winning number is found, a None otherwise
        """
        winning_numbers = winning_numbers_tag.find(
            class_=re.compile(r"number|number\d")
        )
        if winning_numbers:
            return winning_numbers.text.strip()

    def download(self):
        """The clean_data method cleans the html tags.

        Returns:
            a UniformInvoiceInfo object
        """
        invoice_year = self.soup.find("title").text.split(" ")[0][:4]
        claiming_date_tag = self.table_tag.find("tr", class_="htitlepink")
        winning_numbers_tag = self.table_tag.find_all("tr", class_="tr")

        data = UniformInvoiceDataInfo(
            invoice_year=invoice_year,
            claiming_date=self.extract_claiming_date(claiming_date_tag),
            winning_numbers=map(self.extract_winning_numbers, winning_numbers_tag),
        )

        return data.dict()
