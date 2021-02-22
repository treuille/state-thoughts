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
    # Let the user select the example type
    example_types = {
        "Callbacks": ("example_with_callbacks", "notes_on_callbacks"),
        "Signals": ("example_with_signals", "notes_on_signals"),
    }
    example_name, (func_attr, notes_attr) = st.sidebar.radio("Example type",
        list(example_types.items()), format_func=lambda item: item[0])
    func = getattr(example, func_attr)

    # Display the title
    st.write(f"# Example with {example_name}")

    # Display the code
    st.write("## Code")
    display_function_code(func)

    # Display the live demo
    "## Live demo"
    func()

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

