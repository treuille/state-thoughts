"""
# [Johannes] Not another tic tac toe
"""

import streamlit as st


def example_with_callbacks():
    """
    - **Adrien will write notes and observations here.**
    """
    state = st.beta_session_state(
        fields=[[None, None, None], [None, None, None], [None, None, None]]
    )

    cols = st.beta_columns(3)
    for i, row in enumerate(state.fields):
        for j, field in enumerate(row):
            cols[j].button(".", key=f"{i}-{j}")


def example_with_signals():
    """
    - **Adrien will write notes and observations here.**
    """
    st.write("example_with_signals")
