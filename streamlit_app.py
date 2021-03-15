import streamlit as st
import linked_sliders
import non_trivial_init
import reacting_at_the_bottom
import inspect
import re
import textwrap
import pandas as pd

# This is the list of prototypes which we're testing, mapped to the name of
# the function in the example module which demonstrates that prototype
# on that eample. For example the the code implementing the signals prototype on
# the linked sliders example is called linked_sliders.example_with_signals().
PROTOTYPES = {
    "Callbacks": "example_with_callbacks",
    "Signals": "example_with_signals",
    "beta_state": "example_with_beta_state",
    "Decorator Style": "example_with_decorators",
}

# Each prototype is tested on a number of examples, listed here.
EXAMPLES = {
    "Linked sliders": linked_sliders,
    "Non-trivial state initialization": non_trivial_init,
    "Reacting to events at the bottom": reacting_at_the_bottom,
}

def main():
    """Exection starts here."""
    # Setup the main navigation in the sidebar
    options = ["Summary"] + list(EXAMPLES.keys())
    selected_page = st.sidebar.radio("Select an example", options)

    if selected_page == "Summary":
        display_summary()
    elif selected_page in EXAMPLES:
        display_example(EXAMPLES[selected_page])


def display_summary():
    """Display the summary information."""

    # Instructions
    st.write("# State tests")
    st.success("👈 Choose an example at left to explore implementations.")

    # Code layout
    st.write("""
    ## Code Layout
    There are two basic concepts:
    
    1. An **example** is a model use case for which we're testing different
    state models. Each example is defined in a **module**.
    2. A **prototype** is a Python API which we might publish to the community.
    Each prototype is defined in a **function**.

    For example, the function `linked_sliders.example_with_callbacks()`
    provides a snippet of code exemplifying writing two linked sliders in the
    callback style.
    """)

    # Show how to write some examples
    st.write("""
    ## How to add new examples

    1. Add a new Python module to this repo.
    2. Add that modele to the `EXAMPLES` table.
    3. Populate it with prototype functions.

    Currently supported examples:
    """)

    examples = pd.DataFrame(EXAMPLES.items(),
        columns=['example', 'module'])
    st.table(examples)

    # Show how to write prototypes
    st.write("""
    ## How to add new prototypes

    1. Add a new prototype name to the `PROTOTYPES` table.
    2. Implement the corresponding functions in whatever example modules you
       like.

    Currently supported prototypes:
    """)

    examples = pd.DataFrame(PROTOTYPES.items(),
        columns=['prototype', 'function'])
    st.table(examples)


def display_example(example):
    """Show how an example works with differnet code snippets."""
    # This is the set of prototypes which are defined in this example module
    valid_prototypes = [name for name, func_name in PROTOTYPES.items()
            if hasattr(example, func_name)]

    prototype_name = st.sidebar.radio("Example a prototype", valid_prototypes)
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
