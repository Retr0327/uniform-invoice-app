import asyncio
import streamlit as st
from view import create_invoice_form, create_prize_table, create_redemption


def run_app() -> None:
    st.title("Uniform Invoice App")
    create_invoice_form()

    if "invoice_data" in st.session_state:
        create_prize_table()
        asyncio.run(create_redemption())


if __name__ == "__main__":
    run_app()