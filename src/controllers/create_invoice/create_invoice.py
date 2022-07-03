import asyncio
from utils import UniformInvoiceData
from .query_params import QueryParams
from middlewares import check_has_invoice
from services import create_invoice, create_prize, get_invoice, get_claiming_date


@check_has_invoice
def handle_create_invoice(month: str, year: str):
    result = asyncio.run(UniformInvoiceData(year, month).build())

    if isinstance(result, str):
        return result

    invoice_query = (month, year)
    builder = QueryParams(month, year, result)
    invoice_param = builder.build_invoice()
    prize_param = builder.build_prize()

    create_invoice(invoice_param)
    create_prize(prize_param)

    prize_result = get_invoice(invoice_query)
    claiming_date = get_claiming_date(invoice_query)

    return (claiming_date, prize_result)
