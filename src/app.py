import asyncio
import streamlit as st
from models import init_db
from config import make_db_dir, DB_PATH
from view import create_invoice_form, create_prize_table, create_redemption


if not DB_PATH.is_file():
    make_db_dir()
    init_db()


def run_app() -> None:
    st.title("Uniform Invoice App")
    create_invoice_form()

    if "invoice_data" in st.session_state:
        create_prize_table()
        asyncio.run(create_redemption())


if __name__ == "__main__":
    run_app()
