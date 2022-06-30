import streamlit as st


def add_select(title: str, options: tuple) -> str:
    return st.selectbox(title, options)
