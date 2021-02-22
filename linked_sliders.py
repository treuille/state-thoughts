"""
# Linked Sliders

Here we are trying to get two sliders to be linked together.

## Notes

- I think it's important to prefer state in the widget than in the state
  object, and to avoid duplicating the state between the wiget and the
  state object.

- It's a little bit awkward how the handling of the signals is happening
  above the definition of the GUI events

- This live reloading thing with state is just absolutely amazing from 
  a workflow perspective.

- Note that launching the balloons resets the sliders. I think we need to
  consider something like DONT_CHANGE for linked sliders.
"""

import streamlit as st
import st_event

# Convert between fahrenheit and celsius
to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

min_celsius, max_celsius = -100.0, 100.0

def example_with_callbacks():
    """An example of two linked sliders using callbacks."""
    state = st.beta_session_state() 
    

def example_with_signals():
    """An example of two linked sliders using signals."""
    # Let's add some signal handlers here
    if st_event.signal("Celsius"):
        celsius = st_event.value()
        fahrenheit = to_fahrenheit(celsius)
    elif st_event.signal("Fahrenheit"):
        fahrenheit = st_event.value()
        celsius = to_celcius(fahrenheit)
    else:
        celsius, fahrenheit = None, None

    # Now actually display the sliders
    celsius = st_event.slider("Celsius", min_celsius, max_celsius, celsius)
    fahrenheit = st_event.slider("Fahrenheit", to_fahrenheit(min_celsius),
            to_fahrenheit(max_celsius), fahrenheit)

    # To test the effect of a separate signal, let's add one here.
    if st_event.signal("Balloons"):
        st.balloons()
    st_event.button("Balloons")
