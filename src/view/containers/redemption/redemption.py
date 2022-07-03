import asyncio
import streamlit as st
from .prize_search import binary_search
from ...components import form_controller

PRIZE_TYPES = {
    1: ["特別獎", "1000 萬"],
    2: ["特獎", "200 萬"],
    3: ["頭獎", "20 萬"],
    4: ["二獎", "4 萬"],
    5: ["三獎", "1 萬"],
    6: ["四獎", "4000 "],
    7: ["五獎", "1000 "],
    8: ["六獎", "200 "],
    9: ["增開", "200 "],
}


def clear_number():
    st.session_state["number"] = ""


async def handle_prize_search(input: str):
    prize_data = st.session_state["invoice_data"][1]
    try:
        result = await asyncio.gather(
            *[binary_search(prize_data.copy(), input[item:]) for item in range(6)]
        )

        filtered_result = list(filter(lambda value: value, result))

        if not filtered_result:
            return st.info("沒有中獎！")

        index = min(filtered_result)
        return st.success(f"恭喜中 {PRIZE_TYPES[index][0]} {PRIZE_TYPES[index][1]}元")

    except ValueError:
        st.error("請輸入正確發票數字")


async def create_redemption() -> None:
    input = form_controller("input", title="請輸入發票號碼", key="number", max_chars=8)
    st.button("clear number", on_click=clear_number)

    if input:
        await handle_prize_search(input)
