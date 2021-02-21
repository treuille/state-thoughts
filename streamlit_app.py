import streamlit as st
import st_event
import linked_sliders

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

## Notes

- I wonder if there's a way we can do signal handling at the bottom of the 
  script? (Without getting off-by-one errors?)
  
- Two similar concepts are (1) global variables in imported packages, and (2)
  state. They have similar enough semantics (aka they stay around between runs)
  that you might use them intergchangeably. (I did in st_event.py.) But they
  don't reset at the same time, which can be the source of subtle bugs.
"""


def main():
    """Exection starts here."""
    st.write(EVENT_MODEL_NOTES)
    linked_sliders.example_with_signals()

if __name__ == "__main__":
    main()

