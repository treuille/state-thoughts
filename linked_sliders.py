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

MIN_CELCIUS, MAX_CELCIUS = -100.0, 100.0

def example_with_callbacks():
    """
    ## Notes on the callback example

    - I had to reset the state in this complex way because I wasn't sure where
      else the state may have been used. :(

    - In a way, I find this example simpler to understand than the example 
      with signals, because it's more obvious how it works
      
    - One thing I don't like about this is that it feels like the state is
      "taking over" and the Streamlit dataflow style is becoming a detail.
      I feel like there's a way of marrying them more closely.
    """
    # Get and initialize the state.
    state = st.beta_session_state() 
    if 'temperature_celcius' not in dir(state):
        state.temperature_celcius = MIN_CELCIUS

    # Callbacks if something changes
    def celcius_changed(new_celcius_temperature):
        state.temperature_celcius = new_celcius_temperature

    def fahrenheit_changed(new_fahrenheit_temperature):
        state.temperature_celcius = to_celcius(new_fahrenheit_temperature)

    celsius = st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS,
            state.temperature_celcius, on_change=celcius_changed)
    fahrenheit = st.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),
            to_fahrenheit(MAX_CELCIUS), 
            to_fahrenheit(state.temperature_celcius),
            on_change=fahrenheit_changed)
    st.write(f"`{celsius}c` == `{fahrenheit}f`")
        

def example_with_signals():
    """
    # Notes on the signals example

    - Note that launching the balloons resets the sliders. I think we need to
      consider something like DONT_CHANGE for linked sliders.

    - One thing that's kinda complicated about this example is that it's 
      kinda weird how you're juggling these two pieces of state (fahrenheit and
      celsius) in a tricky way.
    """
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
    celsius = st_event.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, celsius)
    fahrenheit = st_event.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),
            to_fahrenheit(MAX_CELCIUS), fahrenheit)

    st.write(f"`{celsius}c` == `{fahrenheit}f`")

    # Note that launching the balloons resets the sliders. I think we need to
    # consider something like DONT_CHANGE for linked sliders.
    if st_event.signal("Balloons"):
        st.balloons()
    st_event.button("Balloons")
