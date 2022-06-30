import streamlit as st
from typing import Optional


def add_input(
    title: str, placeholder: Optional[str] = "", max_chars: Optional[int] = None
) -> str:
    """The add_input function adds a input field."""
    return st.text_input(
        title,
        placeholder=placeholder,
        max_chars=max_chars,
    )
