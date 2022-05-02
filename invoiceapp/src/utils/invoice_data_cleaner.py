import re
from typing import Union
from urllib.parse import urljoin
from dataclasses import dataclass
from .html_downloader import download_html
from .invoice_data_downloader import UniformInvoiceDownloader


BASE_URL = "https://invoices.com.tw/"


@dataclass
class UniformInvoiceCleaner:
    """
    The UniformInvoiceCleaner objects downloads the data regarding the uniform invoice from the url.
    """

    month: str

    def __post_init__(self) -> None:
        self.url = urljoin(BASE_URL, f"{self.month}.html")
        self.bsObj = download_html(self.url)

    def download_data(self, name: str) -> Union[str, list[str]]:
        """The download_data method downloads the data via the object UniformInvoiceReward and UniformInvoiceTitle, and stores the data
           in a dictionary.

        Returns:
            a string if the `name` refers to `invoice_year` or `date`, a map object if the `name` refers to `rewards`
        """
        invoice_data = UniformInvoiceDownloader(self.bsObj).download()
        factories = {
            "invoice_year": invoice_data["invoice_year"],
            "date": invoice_data["claiming_date"],
            "rewards": invoice_data["winning_numbers"],
        }
        return factories[name]

    @property
    def invoice_year(self) -> list[str]:
        return self.download_data("invoice_year")

    @property
    def claiming_date(self) -> list[str]:
        date = self.download_data("date")
        claiming_date = re.findall(r"\d+\-\d+\-\d+", date)
        return claiming_date

    @property
    def winning_numbers(self) -> dict[str, Union[str, list]]:
        rewards = list(self.download_data("rewards"))
        numbers = {
            "special": rewards[0],
            "grand": rewards[1],
            "first": [value.strip() for value in rewards[2].split("\n")],
            "sixth": rewards[3],
        }
        return numbers
