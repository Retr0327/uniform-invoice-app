from string import Template

CONTENT = Template(
    "$year$first_month、$second_month月發票\n"
    "領獎時間： $claiming_date_start 至 $claiming_date_end\n"
    "1. 特別：$special\n"
    "2. 特獎：$grand\n"
    "3. 頭獎：$first\n"
    "4. 增開：$sixth"
)


def build_bulletin(
    invoice_year: str, month: str, claiming_date: list, winning_numbers: dict
) -> str:

    first_month = month[:2]
    second_month = month[2:]
    claiming_date_start = claiming_date[0]
    claiming_date_end = claiming_date[-1]
    special_prize = winning_numbers["special"]
    grand_prize = winning_numbers["grand"]
    first_prize = " / ".join(winning_numbers["first"])
    sixth_prize = winning_numbers["sixth"]

    return CONTENT.substitute(
        year=invoice_year,
        first_month=first_month,
        second_month=second_month,
        claiming_date_start=claiming_date_start,
        claiming_date_end=claiming_date_end,
        special=special_prize,
        grand=grand_prize,
        first=first_prize,
        sixth=sixth_prize,
    )
