from dataclasses import dataclass
from ..utils import UniformInvoiceCleaner, build_bulletin


@dataclass
class UniformInvoice:
    """
    The UniformInvoice objects shows the content of the uniform invoice webpage to the user, and let the user check whether he/she
    gets the rewards or not.
    """

    month: str

    def __post_init__(self) -> None:
        self.data = UniformInvoiceCleaner(self.month)
        self.invoice_year = self.data.invoice_year
        self.claiming_date = self.data.claiming_date
        self.winning_numbers = self.data.winning_numbers

    def show_content(self) -> str:
        return build_bulletin(
            invoice_year=self.invoice_year,
            month=self.month,
            claiming_date=self.claiming_date,
            winning_numbers=self.winning_numbers,
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
