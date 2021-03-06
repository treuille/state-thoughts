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
to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
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
      if 'temperature_celcius' not in dir(state):
          state.temperature_celcius = MIN_CELCIUS
      ```
      With the following message: *StreamlitAPIException: Session state
      variable has not been initialized: "temperature_celcius"*. Is this really
      what we want??
    """
    # Get and initialize the state.
    state = st.beta_session_state(temperature_celcius=MIN_CELCIUS) 

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
    - consider something like DONT_CHANGE for linked sliders

    - One thing that's kinda complicated about this example is that it's 
      kinda weird how you're juggling these two pieces of state (fahrenheit and
      celsius) in a tricky way.

    [Amanda]:
    - The idea is essentially the widget_values feature I implemented, except
      we make having a key disable widgets updating in response to changing input values.
      The key here is that by making the value explicitly copy from the previous run,
      it becomes much clearer what the value should be each time.
    - Automatically resetting in response to input changing would work here but we're
      still discussing the design of that for other situations. So this also showcases
      a possible design where widgets are assumed to retain their identity and local state
      unless and until we assign it explicitly.
    - I'm not sold on this aspect of the design, because I really like the
      declarative feel of each widget being a pure function of its arguments.
    - To lean into the obvious React analogy, each widget is a function of its props and
      local state, except we currently don't distinguish those, and so either wipe out our
      state when props change, or we lose the ability to set state from the outside.
      This seems like a very important direction to explore.
    """
    # Let's add some signal handlers here
    if st.beta_signal("Celsius"):
        c = st.beta_signal_value()
        f = to_fahrenheit(c)
    elif st.beta_signal("Fahrenheit"):
        f = st.beta_signal_value()
        c = to_celcius(f)
    else:
        # beta_widget_value doesn't return what I expected, so these are differently named to
        # empahsize that this part is imaginary
        c = st.previous_widget_value('c')
        f = st.previous_widget_value('f')

    # Now actually display the sliders
    celsius = st.slider("Celsius", MIN_CELCIUS, MAX_CELCIUS, signal="Celsius", key='c')
    celsius.value = c
    fahrenheit = st.slider("Fahrenheit", to_fahrenheit(MIN_CELCIUS),
                           to_fahrenheit(MAX_CELCIUS), signal="Fahrenheit", key='f')
    fahrenheit.value = f

    st.write(f"`{celsius}`c == `{fahrenheit}`f")

    # Note that launching the balloons resets the sliders. I think we need to
    # consider something like DONT_CHANGE for linked sliders.
    st.warning(
        "☣️ Clicking the button below will mess up the state. "
        "We need to fix this.")
    if st.beta_signal("Balloons"):
        st.balloons()
    st.button("Balloons", signal="Balloons")
