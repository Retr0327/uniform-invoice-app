import pandas as pd
from typing import List
from dataclasses import dataclass

TABLE_INDEX = ["特別獎", "特獎", "頭獎", "增開獎"]


@dataclass
class Table:
    prize_data: List

    def create_prize_list(self, data: List):
        result = []
        first_prize = []
        for item in data:
            if item[0] == 3:
                first_prize.append(item[1])

            if item[0] == 1 or item[0] == 2 or item[0] == 9:
                result.append(item[1])

        result.insert(2, " / ".join(first_prize))
        return result

    def create(self):
        prize_list = self.create_prize_list(self.prize_data)
        table = pd.DataFrame({"獎項": TABLE_INDEX, "號碼": prize_list})
        
        return table.set_index("獎項")
