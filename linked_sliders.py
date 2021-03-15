"""
# Linked Sliders

Here we are trying to get two sliders to be linked together.
"""

import streamlit as st

# Convert between fahrenheit and celsius
to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

MIN_CELCIUS, MAX_CELCIUS = -100.0, 100.0

def example_with_callbacks():
    """
    - Linked sliders with callbacks.
    - Only a single state value.
    - Setting the slider values by passing in the `value` parameter.
    """
    # Get and initialize the state.
    state = st.get_state()
    if state.celsius == None:
        state.celsius = MIN_CELCIUS

    # Callbacks if something changes
    def celsius_changed(new_celsius_temperature):
        state.celsius = new_celsius_temperature

    def fahrenheit_changed(new_fahrenheit_temperature):
        state.celsius = to_celsius(new_fahrenheit_temperature)

    # Display the sliders.
    st.slider("Celsius",
            min_value=MIN_CELCIUS,
            max_value=MAX_CELCIUS,
            value=state.celsius,
            on_change=celsius_changed)
    st.slider("Fahrenheit",
            min_value=to_fahrenheit(MIN_CELCIUS),
            max_value=to_fahrenheit(MAX_CELCIUS), 
            value=to_fahrenheit(state.celsius),
            on_change=fahrenheit_changed)

    # Display the state.
    st.success(f"`{state.celsius}c` == `{to_fahrenheit(state.celsius)}f`")


def example_with_signals():
    """
    - Linked sliders with signals.
    - We have two state variables here, `fahrenheit` and `celsius`.
    """
    # Get the state
    state = st.get_state()

    # Convert the range bounds to fahrenheit.
    min_fahrenheit = to_fahrenheit(MIN_CELCIUS)
    max_fahrenheit = to_fahrenheit(MAX_CELCIUS)

    # React to any changes up here
    if st.widget_changed("celsius"):
        state.fahrenheit = to_fahrenheit(state.celsius)
    elif st.widget_changed("fahrenheit"):
        state.celsius = to_celsius(state.fahrenheit)

    # Now actually display the sliders
    st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, key="celsius")
    st.slider("Fahrenheit", min_fahrenheit, max_fahrenheit, key="fahrenheit")

    # Show the result
    st.success(f"`{state.celsius}`c == `{state.fahrenheit}`f")


def example_with_decorators():
    """
    Linked sliders with decorators.
    """
    # Get and initialize the state
    state = st.get_state()
    if state.celsius == None:
        state.celsius = MIN_CELCIUS

    # Convert the range bounds to fahrenheit.
    min_fahrenheit = to_fahrenheit(MIN_CELCIUS)
    max_fahrenheit = to_fahrenheit(MAX_CELCIUS)

    # Display the state in some debug code
    st.write("state", type(state), state)

    @st.ui.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, state.celsius)
    def celsius_slider(celsius):
        st.warning("celsius_slider callback")
        state.celsius = celsius
        state.fahrenheit = to_fahrenheit(celsius)
        
    @st.ui.slider("Fahrenheit", min_fahrenheit, max_fahrenheit, state.fahrenheit)
    def fahrenheit_slider(fahrenheit):
        st.warning("fahrenheit_slider callback")
        state.fahrenheit = fahrenheit
        state.celsius = to_celsius(fahrenheit)
        
    celsius_slider()
    fahrenheit_slider()

    # Show the result
    st.success(f"`{state.celsius}` c == `{state.fahrenheit}` f")

def _fancy_slider(label, **slider_kwargs):
    def decorator(callback):
        st.write(callback)

def example_with_decorators_2():
    """
    - This is an alternate decorator style
    """  
