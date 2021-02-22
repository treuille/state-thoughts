import streamlit as st
import st_event
import linked_sliders
import inspect
import re
import textwrap

def main():
    """Exection starts here."""
    # Setup the main navigation in the sidebar
    examples = {
        "Linked sliders example": linked_sliders,
    }
    options = ["Summary"] + list(examples.keys())
    selected_page = st.sidebar.radio("Select page", options)

    if selected_page in examples:
        display_example(examples[selected_page])

def display_example(example):
    """Show how an example works with differnet code snippets."""
    example_with_callbacks = getattr(example, "example_with_callbacks")
    """
    # Example with callbacks
    ## Code
    """
    display_function_code(example_with_callbacks)
    "## Results"
    example_with_callbacks()

def display_function_code(func):
    """Displays the code of a function, stripping out the defintion and
    docstring."""
    # Get the functio sourc
    source = inspect.getsource(func)

    # Strip out the function definition and docstring.
    def_and_docs = re.match(r'def.*:\n\s*"""(.*\n)*\s*"""',
        source, re.MULTILINE)
    source = textwrap.dedent(source[def_and_docs.end() + 1:])

    # Display it
    st.code(source)

if __name__ == "__main__":
    main()

