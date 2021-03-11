"""
# 👀 [Johannes] Minimal Analytics

This is a minimal version of my [streamlit-analytics](https://github.com/jrieke/streamlit-analytics)
package, which uses the [old session state hack from Thiago](https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92). 
It tracks and records the inputs to all widgets. Note that unlike my original package,
this stores the results in session state rather than global state.
"""

import functools
import streamlit as st


def example_with_callbacks():
    """
    **Only button works so far and this is still a WIP!!**
    """
    # Initialize state to track widget inputs.
    state = st.beta_session_state(widget_inputs={})

    # tracked_button = functools.partial(st.button, on_click=track_click)
    def tracked_button(label, *args, on_click=None, **kwargs):
        def track_click(orig_on_click):
            if label not in state.widget_inputs:
                state.widget_inputs[label] = 0
            state.widget_inputs[label] += 1

            if orig_on_click is not None:
                return orig_on_click()

        clicked = st.button(
            label, *args, on_click=functools.partial(track_click, on_click), **kwargs
        )

        return clicked

    st.write("Use these widgets and your inputs will be tracked below:")
    tracked_button("Click me")
    st.slider("Slide me")

    st.write("Tracked inputs:")
    st.write(state.widget_inputs)


def example_with_signals():
    """
    Add notes here
    """
    st.write("example_with_signals")
