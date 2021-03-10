"""
# 🧑‍💻 Johannes' TODO list

This is a simple TODO list which stores the TODO items in session state (each item is 
one `dict`). 
"""

import streamlit as st


def example_naive():
    """
    **:warning: This doesn't work – it's just for my understanding of the problem.**

    Naive way to add a new item: just use the return value from the text input.

    At each script execution (e.g. when a checkbox is checked), the new item is added
    again. We need to either

    1. Clear the value of the textfield OR
    2. Have a way to add the new item only when the input to the textfield changed
       (-> on_change or signal)
    """
    # Define initial state with some dummy todos.
    state = st.beta_session_state(
        todos=[
            {"description": "Join streamlit", "author": "Johannes", "done": True},
            {"description": "Test state", "author": "Johannes", "done": False},
        ],
    )

    new_todo = st.text_input("What should Johannes do?")
    if new_todo:
        state.todos.append(
            {"description": new_todo, "author": "Johannes", "done": False}
        )

    write_todo_list(state.todos)


def example_with_callbacks():
    """
    - **Adrien will write notes and observations here.**
    """
    st.write("example_with_callbacks")

    state = st.beta_session_state(
        # new_todo="",
        todos=[
            {"description": "Join streamlit", "author": "Johannes", "done": True},
            {
                "description": "Test state prototypes",
                "author": "Johannes",
                "done": False,
            },
        ],
    )

    new_todo = st.text_input("What should Johannes do?")
    if new_todo:
        state.todos.append(
            {"description": new_todo, "author": "Johannes", "done": False}
        )

    write_todo_list(state.todos)


def example_with_signals():
    """
    - **Adrien will write notes and observations here.**
    """
    st.write("example_with_signals")


def write_todo_list(todos):
    "Display the todo list (mostly layout stuff, no state)."
    st.write("---")
    col1, col2, col3 = st.beta_columns([0.1, 0.7, 0.2])
    col1.write("*Done?*")
    col2.write("*Description*")
    col3.write("*Created by*")
    for i, todo in enumerate(todos):
        done = col1.checkbox("", todo["done"], key=str(i))
        if done:
            format_str = (
                '<span style="color: grey; text-decoration: line-through;">{}</span>'
            )
        else:
            format_str = "{}"
        col2.markdown(
            format_str.format(todo["description"]),
            unsafe_allow_html=True,
        )
        col3.markdown(format_str.format(todo["author"]), unsafe_allow_html=True)
