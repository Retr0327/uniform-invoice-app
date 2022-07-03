from services import get_invoice, get_claiming_date


def check_has_invoice(func):
    """The check_has_invoice function checks whether the database has the invoice data."""

    def wrapper(month: str, year: str):
        invoice_query = (month, year)
        result = get_invoice(invoice_query)

        if result:
            claiming_date = get_claiming_date(invoice_query)
            return (claiming_date, result)

        return func(month, year)

    return wrapper
