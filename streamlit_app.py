import streamlit as st
import st_event


def main():
    """Exection starts here."""
    st.write("""
        # Adrien's event model notes

        ## Examples

        - Two linked sliders
        - Non-trivial state initialization
    """)
    signals_example_two_linked_sliders()

def callback_example_two_linked():
    """asdfa"""
    asdfa

def signals_example_two_linked_sliders():
    """An example of two linked sliders using signals."""
    to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5.0 / 9.0
    to_fahrenheit = lambda celsius: 9.0 / 5.0 * celsius + 32

    min_celsius, max_celsius = -100.0, 100.0
    if st_event.signal("Celsius"):
        celsius = st_event.value()
        fahrenheit = to_fahrenheit(celsius)
    elif st_event.signal("Fahrenheit"):
        fahrenheit = st_event.value()
        celsius = to_celcius(fahrenheit)
    else:
        celsius, fahrenheit = None, None

    celsius = st_event.slider("Celsius", min_celsius, max_celsius, celsius)
    fahrenheit = st_event.slider("Fahrenheit", to_fahrenheit(min_celsius),
            to_fahrenheit(max_celsius), fahrenheit)


if __name__ == "__main__":
    main()

