import datetime

current_year = datetime.datetime.now().year
years_options = (current_year - 1, current_year)
month_options = ("0102", "0304", "0506", "0708", "0910", "1112")


def get_month_index():
    container = [3, 7, 11, 15, 19, -1]
    current_month = datetime.datetime.now().month
    values = {"0": current_month * 2 - 5, "1": current_month * 2 - 3}
    key = str(current_month % 2)
    return container.index(values[key])
