import streamlit as st
from typing import List
from .table import Table
from streamlit.delta_generator import DeltaGenerator


def create_prize_table(data: List) -> DeltaGenerator:
    claiming_date, prize_data = data
    start, end = claiming_date[0]

    st.header(f"領獎日期{start} 至 {end}")
    return st.table(Table(prize_data).create())
