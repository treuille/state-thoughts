import streamlit as st
import st_event

EVENT_MODEL_NOTES = """
# Adrien's event model notes

## Examples

- Two linked sliders
- Non-trivial state initialization
- Errors before and after 
- closures
- sliders that re-initialize the state

## Questions

- Can state be instantiated with two separate places?

## Random Thoughts

- I wonder if there's a way we can do signal handling at the bottom of the 
  script? (Without getting off-by-one errors?)
"""

# Convert between fahrenheit and celsius
to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

def main():
    """Exection starts here."""
    st.write(EVENT_MODEL_NOTES)
    two_linked_sliders_with_signals()

def two_linked_sliders_with_callbacks():
    """An example of two linked sliders using callbacks."""
    state = st.beta_session_state() 
    

def two_linked_sliders_with_signals():
    """An example of two linked sliders using signals."""
    # Let's add some signal handlers here
    min_celsius, max_celsius = -100.0, 100.0
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

if __name__ == "__main__":
    main()

