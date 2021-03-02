"""
# Non-trivial state intialization

This is an example where we're trying to initialize the state properly
"""

import streamlit as st
import st_event
import numpy as np

def example_with_callbacks():
    """
    - The use of callbacks here makes it easy to avoid off-by-one errors.
    """
    rows = st.slider("Rows", 1, 10, 5)
    cols = st.slider("Columns", 1, 10, 5)
    state = st.beta_session_state(rows=None, cols=None)
    if rows != state.rows or cols != state.cols:
        state.rows = rows
        state.cols = cols
        state.data = np.zeros((state.rows, state.cols), np.int32)
        for i in range(rows):
            for j in range(cols):
                state.data[i, j] = (i + j) % 2
    def increment_data():
        state.data += 1
    def reset_state():
        state.rows = state.cols = None
    st.write(state.data)
    st.button("Increment data", on_click=increment_data)
    st.button("Reset state", on_click=reset_state)


def example_with_signals():
    """
    - Unlike the signals example, in this case we needed to put the if
      statements a bit earlier in the code logic. **So order of operations
      became more important.**
    """
    rows = st.slider("Rows", 1, 10, 5)
    cols = st.slider("Columns", 1, 10, 5)
    state = st.beta_session_state(rows=None, cols=None)
    if st_event.signal("Increment data"):
        state.data += 1
    elif st_event.signal("Reset state"):
        state.rows = state.cols = None
    if rows != state.rows or cols != state.cols:
        state.rows = rows
        state.cols = cols
        state.data = np.zeros((state.rows, state.cols), np.int32)
        for i in range(rows):
            for j in range(cols):
                state.data[i, j] = (i + j) % 2
    st.write(state.data)
    st_event.button("Increment data")
    st_event.button("Reset state")
