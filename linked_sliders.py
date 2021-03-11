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

# Convert between fahrenheit and celsius
to_celsius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

MIN_CELCIUS, MAX_CELCIUS = -100.0, 100.0

def example_with_callbacks():
    """
    - I had to reset the state in this complex way because I wasn't sure where
      else the state may have been used. :(

    - In a way, I find this example simpler to understand than the example 
      with signals, because it's more obvious how it works
      
    - One thing I don't like about this is that it feels like the state is
      "taking over" and the Streamlit dataflow style is becoming a detail.
      I feel like there's a way of marrying them more closely.

    - This example failed for me:
      ```py
      state = st.beta_session_state() 
      if 'temperature_celsius' not in dir(state):
          state.temperature_celsius = MIN_CELCIUS
      ```
      With the following message: *StreamlitAPIException: Session state
      variable has not been initialized: "temperature_celsius"*. Is this really
      what we want??
    """
    # Get and initialize the state.
    state = st.beta_session_state(temperature_celsius=MIN_CELCIUS) 

    # Callbacks if something changes
    def celsius_changed(new_celsius_temperature):
        state.temperature_celsius = new_celsius_temperature

    def fahrenheit_changed(new_fahrenheit_temperature):
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
    st.write(f"`{state.celsius}`c == `{state.fahrenheit}`f")

    # React to any changes up here
    if st.widget_changed("celsius"):
        st.error("celsius changed")
        state.fahrenheit = to_fahrenheit(state.celsius)
    elif st.widget_changed("fahrenheit"):
        st.error("fahrenheit changed")
        state.celsius = to_celsius(state.fahrenheit)
    else:
        st.success("nothing changed")

    # Now actually display the sliders
    st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, key="celsius")
    st.slider("Fahrenheit", min_fahrenheit, max_fahrenheit, key="fahrenheit")

    # Show the new state
    st.write(f"`{state.celsius}`c == `{state.fahrenheit}`f")

