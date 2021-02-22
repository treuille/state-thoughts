import streamlit as st
import st_event
import linked_sliders

EVENT_MODEL_NOTES = """
# Adrien's event model notes

"""


def main():
    """Exection starts here."""
    st.write(EVENT_MODEL_NOTES)
    linked_sliders.example_with_callbacks()

if __name__ == "__main__":
    main()

