from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class UniformInvoiceDownloader:
    """The UniformInvoiceDownloader object downloads the invoice data."""

    soup: BeautifulSoup

    def __post_init__(self) -> None:
        self.table_tags = self.soup.find("table").find_all("tr")

    def clean_tag(self, table_tag: BeautifulSoup) -> str:
        return table_tag.text.strip().replace("\n", "")

    def download(self) -> map:
        target_tags = [
            tag.find("td", {"class": "this_bg"})
            for tag in self.table_tags
            if tag.find("td", {"class": "this_bg"}) is not None
        ][1:]

        return map(self.clean_tag, target_tags)
