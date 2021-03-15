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
    # Setup the state properly
    state = st.get_state()
    if state.rows is None or state.cols is None:
        state.rows = state.cols = 5

    # Display the sliders
    st.slider("Rows", 1, 10, key="rows")
    st.slider("Columns", 1, 10, key="cols")

    # Reintialize the staste if necessary
    if state.data is None or state.data.shape != (state.rows, state.cols):
        state.data = np.zeros((state.rows, state.cols), np.int32)
        for i in range(state.rows):
            for j in range(state.cols):
                state.data[i, j] = (i + j) % 2

    # Callbacks
    def increment_data():
        state.data += 1
    def reset_state():
        state.data = None

    # Display the ui
    st.write(state.data)
    st.button("Increment data", on_click=increment_data)
    st.button("Reset state", on_click=reset_state)


def example_with_signals():
    """
    - Unlike the signals example, in this case we needed to put the if
      statements a bit earlier in the code logic. **So order of operations
      became more important.**
    """
    # Setup the state properly
    state = st.get_state()
    if state.rows is None or state.cols is None:
        state.rows = state.cols = 5

    # Display the sliders
    st.slider("Rows", 1, 10, key="rows")
    st.slider("Columns", 1, 10, key="cols")

    # Change handling
    if st.widget_changed("increment_data"):
        state.data += 1
    elif st.widget_changed("reset_state"):
        state.data = None

    # Reintialize the staste if necessary
    if state.data is None or state.data.shape != (state.rows, state.cols):
        state.data = np.zeros((state.rows, state.cols), np.int32)
        for i in range(state.rows):
            for j in range(state.cols):
                state.data[i, j] = (i + j) % 2

    st.write(state.data)
    st.button("Increment", key="increment_data")
    st.button("Reset", key="reset_state")


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
