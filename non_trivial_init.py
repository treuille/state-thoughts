"""
# Non-trivial state intialization

This is an example where we're trying to initialize the state properly
"""

import streamlit as st
import numpy as np


def example_with_callbacks():
    """
    - The use of callbacks here makes it easy to avoid off-by-one errors.
    """
    rows = st.slider("Rows", 1, 10, 5)
    cols = st.slider("Columns", 1, 10, 5)
    state = st.beta_session_state(rows=None, cols=None, data=0)
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
    state = st.beta_session_state(rows=None, cols=None, data=0)
    if st.beta_signal("Increment data"):
        state.data += 1
    elif st.beta_signal("Reset state"):
        state.rows = state.cols = None
    if rows != state.rows or cols != state.cols:
        state.rows = rows
        state.cols = cols
        state.data = np.zeros((state.rows, state.cols), np.int32)
        for i in range(rows):
            for j in range(cols):
                state.data[i, j] = (i + j) % 2
    st.write(state.data)
    st.button("Increment", signal="Increment data")
    st.button("Reset", signal="Reset state")

def example_with_beta_state():
    """
    - Mostly, my main reaction is that the dictionary notation is so ugly that
      I'm finding myself playing tricks to avoid using it. I think that given
      the keys have to be strings, we could just use Python properties to make
      this a little prettier

    - This init thing is way too verbose. What "wants" to happen is a
      unification of widgets and state into a single dictionary.

    - We could eventually have a namespace stack, but I really wonder whether
      that's P0 actually. (To me, namespaces would happen using a context
      manager.)

    - Therefore, the "key" is actually just the name for the variable
    """
    rows = st.slider("Rows", 1, 10, 5)
    cols = st.slider("Columns", 1, 10, 5)
    st.beta_state.init("rows", None)
    st.beta_state.init("cols", None)
    st.beta_state.init("data", None)
    state = st.beta_state.get()
    st.write("state", type(state), state)
    if rows != state["rows"] or cols != state["cols"]:
        state["rows"] = rows
        state["cols"] = cols
        data = np.zeros((rows, cols), np.int32)
        for i in range(rows):
            for j in range(cols):
                data[i, j] = (i + j) % 2
        state["data"] = data
    def increment_data():
        state["data"] += 1
    def reset_state():
        state["rows"] = state["cols"] = None
    st.write(st.beta_state.get("data"))
    st.button("Increment data", on_click=increment_data)
    st.button("Reset state", on_click=reset_state)
