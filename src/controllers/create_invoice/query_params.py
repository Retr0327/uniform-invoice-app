from typing import Dict, List
from dataclasses import dataclass


@dataclass
class QueryParams:
    """The QueryParams object creates the data which will be inserted to the database."""

    month: str
    year: str
    data: List

    def __post_init__(self) -> None:
        self.prize_data, self.claiming_data = self.data

    def update_prize_key(self, value: Dict[str, str]) -> Dict[str, str]:
        """The update_prize_key method adds two new keys, `month` and `year`.

        Args:
            value: one of the items in `self.prize_data`

        Returns:
            a dict: {
                'type': 'first',
                'prize': '16525386',
                'month': '3',
                'year': 111
            }
        """
        value["month"] = self.month
        value["year"] = self.year
        return value

    def build_invoice(self):
        return (self.month, self.year, *self.claiming_data)

    def build_prize(self):
        flatted_list = [
            dct
            for value in self.prize_data
            for dct in (value if isinstance(value, list) else (value,))
        ]
        return list(map(self.update_prize_key, flatted_list))
