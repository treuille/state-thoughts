"""
# Reacting to events at the bottom of a script

One of the main problems with events I noticed is that you have to react to them
at the very beginning of a script. The good thing aboutt this is that it avoids
off-by-one errors in changing the state, but I think it can also be too
restrictive. This is a contrived example which shows what I mean.

## Notes

- This is the main reason why I started thinking about this signals model. It
  makes this exact case a lot easier.
- Of course, this is a contrived example, but this actually came up for me when
  I was writing my battleship game!
- I also think that this agrees with two other Streamlit-y principals:
    1. That the entire script sort of be a giant callback
    2. That we prefer imperative over functional styles
"""

import streamlit as st

def example_with_callbacks():
    """
    - Note that the callbacks version is much longer here.
    """
    state = st.beta_session_state(color=None)
    def set_color(color):
        def callback():
            state.color = color
        return callback
    st.button("Blue", on_click=set_color("Blue"))
    st.button("Yellow", on_click=set_color("Yellow"))
    if state.color == "Blue":
        st.info("Blue")
    if state.color == "Yellow":
        st.warning("Yellow")


def example_with_signals():
    """
    - Note that the signals version is much shorter here.
    """
    st.button("Blue", signal="Blue")
    st.button("Yellow", signal="Yellow")
    if st.signal("Blue"):
        st.info("Blue")
    elif st.signal("Yellow"):
        st.warning("Yellow")
