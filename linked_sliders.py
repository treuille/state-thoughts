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
    Linked sliders with callbacks.
    """
    # Get and initialize the state.
    state = st.get_state()
    state.temperature_celsius = MIN_CELCIUS

    # Callbacks if something changes
    def celsius_changed(new_celsius_temperature):
        st.write("new_celsius_temperature:", new_celsius_temperature)
        state.temperature_celsius = new_celsius_temperature

    def fahrenheit_changed(new_fahrenheit_temperature):
        st.write("new_fahrenheit_temperature:", new_fahrenheit_temperature)
        state.temperature_celsius = to_celsius(new_fahrenheit_temperature)

    celsius = st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS,
            state.temperature_celsius, on_change=celsius_changed)
    fahrenheit = st.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),
            to_fahrenheit(MAX_CELCIUS), 
            to_fahrenheit(state.temperature_celsius),
            on_change=fahrenheit_changed)

    st.write(f"`{celsius}c` == `{fahrenheit}f`")


def example_with_signals():
    """
    I think this example is nice and clean, but it does **require putting the
    signal handling above the 
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
    st.write(f"`{state.celsius}`c == `{state.fahrenheit}`f")


def example_with_decorators():
    """
    Linked sliders with decorators.
    """
    # Get and initialize the state
    state = st.get_state()
    if state.celsius == None:
        state.celsius = MIN_CELCIUS

    # Display the state in some debug code
    st.write("state", type(state), state)

    # # This could be streamlit_ui.py
    # st.write(st.get_state)
    # st.write(st.session_state.init)
    # return

    @st.ui.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, state.celsius)
    def celsius_slider(new_value):
        # can use context here
        state.celsius = new_value
        
    # # @st.ui.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),s

    # answer = celsius_slider()
    # st.write("answer:", answer)
