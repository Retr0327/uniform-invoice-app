from dataclasses import dataclass
from .prize_data import PrizeData
from typing import Dict, List, Tuple
from .html_downloader import download_html
from .invoice_data_downloader import UniformInvoiceDownloader


@dataclass
class UniformInvoiceData:

    year: str
    month: str

    def __post_init__(self) -> None:
        self.url = f"https://bluezz.com.tw/number_pc_in.php?d={self.year}-{self.month}"

    def download_data(self) -> map:
        bsObj = download_html(self.url)
        return UniformInvoiceDownloader(bsObj).download()

    def clean_date(self, claiming_date: str) -> Tuple[str, str]:
        date_list = claiming_date.split(" ~ ")
        return tuple(date for date in date_list)

    async def build(self) -> List:
        data = list(self.download_data())
        if "" in data:
            return "尚未開獎"
        *prize_list, claiming_date = data
        prize_data = await PrizeData(prize_list).generate()
        return [prize_data, self.clean_date(claiming_date)]
