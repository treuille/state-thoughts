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
    - consider something like DONT_CHANGE for linked sliders

    - One thing that's kinda complicated about this example is that it's 
      kinda weird how you're juggling these two pieces of state (fahrenheit and
      celsius) in a tricky way.
    """
    # Get the state
    state = st.get_state()

    # Convert the range bounds to fahrenheit.
    min_fahrenheit = to_fahrenheit(MIN_CELCIUS)
    max_fahrenheit = to_fahrenheit(MAX_CELCIUS)

    # Show the old state
    st.write("**Before signals**")
    st.write(f"celcius: `{state.celsius}`c")
    st.write(f"fahrenheit: `{state.fahrenheit}`f")

    # React to any changes up here
    if st.widget_changed("celsius"):
        st.error("celsius changed")
        state.fahrenheit = to_fahrenheit(state.celsius)
    elif st.widget_changed("fahrenheit"):
        st.error("fahrenheit changed")
        state.celsius = to_celsius(state.fahrenheit)
    else:
        st.success("nothing changed")

    st.write("**After signals**")
    st.write(f"celcius: `{state.celsius}`c")
    st.write(f"fahrenheit: `{state.fahrenheit}`f")

    # Now actually display the sliders
    st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, key="celsius")
    st.slider("Fahrenheit", min_fahrenheit, max_fahrenheit, key="fahrenheit")

    # Show the new state
    st.write("**After signals**")
    st.write(f"celcius: `{state.celsius}`c")
    st.write(f"fahrenheit: `{state.fahrenheit}`f")

def example_with_decorators():
    """
    Linked sliders with decorators.
    """
    # This could be streamlit_ui.py
    st.beta_state.init("celsius", MIN_CELCIUS)

    @st.ui.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, st.state.celsius)
    def celsius_slider(new_value):
        # can use context here
        st.beta_state.set("celsius", new_value)
        
    # @st.ui.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),s

    answer = celsius_slider()
    st.write("answer:", answer)
