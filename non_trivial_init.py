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


def example_with_decorators():
    """
    - Non-trivial state initialization using Ken's decorator style
    - I wish I could write multiple dimension sliders, but they keys the keys
      need to be set indepdentently, which isn't currently supported.
    """
    # Setup the state properly
    state = st.get_state()
    if state.dim is None:
        state.dim = 5

    # Initialize the state
    intended_shape = (state.dim, state.dim)
    if state.data is None or state.data.shape != intended_shape:
        state.data = np.zeros(intended_shape, np.int32)
        for i in range(state.dim):
            for j in range(state.dim):
                state.data[i, j] = (i + j) % 2
    
    @st.ui.slider("Dimension", 1, 10)
    def dimension_slider(value):
        st.warning(f"dimension_slider: `{value}`")
        state.dim = value
    dimension_slider()

    st.write(state.data)

    @st.ui.button("Increment")
    def increment():
        state.data += 1
    increment()

    @st.ui.button("Reset")
    def reset():
        state.data = None
    reset()
