import streamlit as st
import linked_sliders
import non_trivial_init
import reacting_at_the_bottom
import inspect
import re
import textwrap


def main():
    """Exection starts here."""
    # Setup the main navigation in the sidebar
    examples = {
        "Linked sliders": linked_sliders,
        "Non-trivial state initialization": non_trivial_init,
        "Reacting to events at the bottom": reacting_at_the_bottom,
    }
    options = ["Summary"] + list(examples.keys())
    selected_page = st.sidebar.radio("Select page", options)

    if selected_page == "Summary":
        display_summary()
    elif selected_page in examples:
        display_example(examples[selected_page])


def display_summary():
    """Display the summary information."""

    # These are the new functions that have been added to this wheel
    new_funcs = [
        "beta_widget_value",
        "beta_widget_value",
        "beta_signal",
        "beta_signal_value",
        "beta_signal_context",
    ]

    """
    # State Tests
    Here are the new functions that are defined in this module
    """
    for func in new_funcs:
        st.write(f"### `{func}`", getattr(st, func))


def display_example(example):
    """Show how an example works with differnet code snippets."""
    # Let the user select the example type
    example_types = {
        "Callbacks": "example_with_callbacks",
        "Signals": "example_with_signals",
    }
    example_name, func_attr = st.sidebar.radio(
        "Example type", list(example_types.items()), format_func=lambda item: item[0]
    )
    func = getattr(example, func_attr)

    # Display the title
    example.__doc__

    # Display the code
    st.write(f"# Example with {example_name}")
    st.write("## Code")
    display_function_code(func)

    # Display the live demo
    "## Live demo"
    func()

    # Display the notes
    f"## {example_name} Notes"
    func.__doc__


def display_function_code(func):
    """Displays the code of a function, stripping out the defintion and
    docstring."""
    # Get the functio sourc
    source = inspect.getsource(func)

    # Strip out the function definition and docstring.
    def_and_docs = re.match(r'def.*:\n\s*"""(.*\n)*\s*"""', source, re.MULTILINE)
    source = textwrap.dedent(source[def_and_docs.end() + 1 :])

    # Display it
    st.code(source)


if __name__ == "__main__":
    main()
