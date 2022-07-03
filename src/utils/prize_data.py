import asyncio
from audioop import add
from typing import Dict, List
from dataclasses import dataclass

SUB_PRIZE = {
    "0": "first",
    "1": "second",
    "2": "third",
    "3": "fourth",
    "4": "fifth",
    "5": "sixth",
}


async def form_dict(type: str, prize_value: str) -> Dict[str, str]:
    """The form_dict function forms a dictionary based on `type` and `prize_value`.

    Args:
        type (str): the prize type
        prize_value (str): the claiming number

    Returns:
        a dict
    """
    return {"type": type, "prize": prize_value}


@dataclass
class PrizeData:
    """The PrizeData object generates a list of dictionaries related to the invoice claiming numbers"""

    prize_list: List[str]

    def generate_first_prize(self, first_prize: str) -> List[str]:
        """The generate_first_prize method cleans the `first_prize` data.

        Args:
            first_prize (str): the first prize numbers (e.g. 165253862846717927854976)

        Reutunrs:
            a list: ['16525386', '28467179', '27854976']
        """
        if len(first_prize) == 8:
            return [first_prize]

        container = []
        prize = first_prize[:8]
        first_prize = first_prize[8:]
        container.append(prize)
        return container + self.generate_first_prize(first_prize)

    async def generate_sub_prize(
        self, index: int, first_prize: List[str]
    ) -> asyncio.Future[tuple[Dict[str, str]]]:
        """The generate_sub_prize mehtod generates a list of sub prizes numbers."""
        sub_prize_list = map(
            lambda value: form_dict(SUB_PRIZE[str(index)], value[index:]),
            first_prize,
        )

        return await asyncio.gather(*sub_prize_list)

    def generate_additional(self, value):
        if value == "無":
            return 0
        return value

    async def generate(self) -> asyncio.Future[List[Dict[str, str]]]:
        special, grand, first, additional = self.prize_list
        cleand_first = self.generate_first_prize(first)

        return await asyncio.gather(
            form_dict("special", special),
            form_dict("grand", grand),
            *(self.generate_sub_prize(num, cleand_first) for num in range(6)),
            form_dict("additional", self.generate_additional(additional)),
        )
