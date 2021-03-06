import streamlit as st
import linked_sliders
import non_trivial_init
import reacting_at_the_bottom
import inspect
import re
import textwrap

# This is the list of prototypes which we're testing, mapped to the name of
# the function in the example module which demonstrates that prototype
# on that eample. For example the the code implementing the signals prototype on
# the linked sliders example is called linked_sliders.example_with_signals().
PROTOTYPES = {
    "Callbacks": "example_with_callbacks",
    "Signals": "example_with_signals",
    "beta_state": "example_with_beta_state",
}

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

    # Also writ the beta_state.init function
    st.write("### `beta_state.init`", st.beta_state.init)


def display_example(example):
    """Show how an example works with differnet code snippets."""
    # This is the set of prototypes which are defined in this example module
    valid_prototypes = [name for name, func_name in PROTOTYPES.items()
            if hasattr(example, func_name)]

    prototype_name = st.sidebar.radio("Example type", valid_prototypes)
    func = getattr(example, PROTOTYPES[prototype_name])

    # Display the title
    example.__doc__

    # Display the code
    st.write(f"# Example with {prototype_name}")
    st.write("## Code")
    display_function_code(func)

    # Display the live demo
    "## Live demo"
    func()

    # Display the notes
    f"## {prototype_name} Notes"
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
