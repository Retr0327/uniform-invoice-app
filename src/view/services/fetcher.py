import streamlit as st
from typing import Literal, Union
from controllers import handle_create_invoice

TEN_MINUTES = 60 * 10


@st.cache(ttl=TEN_MINUTES)
def fetch(method: Literal["get_data"], month: str, year: int) -> Union[str, tuple]:
    """The fetch function fetch the data in the database based on the `method`."""
    methods = {"create_data": handle_create_invoice(month, str(year - 1911))}

    return methods[method]
