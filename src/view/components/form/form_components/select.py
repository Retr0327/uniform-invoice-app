import streamlit as st
from typing import Optional, Union


def add_select(title: str, options: tuple, index: Optional[int] = 0) -> Union[str, int]:
    """The add_select function adds a select field."""
    return st.selectbox(title, options, index=index)
