import streamlit as st
from typing import List, Literal
from controllers import handle_create_invoice

TEN_MINUTES = 60 * 10


@st.cache(ttl=TEN_MINUTES)
def fetch(method: Literal["get_data"], month: str, year: str) -> List:
    methods = {"get_data": handle_create_invoice(month, year - 1911)}

    return methods[method]
