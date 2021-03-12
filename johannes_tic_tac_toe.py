"""
# [Johannes] Not another tic tac toe
"""

import streamlit as st
import numpy as np
import functools


# From: https://stackoverflow.com/questions/39922967/python-determine-tic-tac-toe-winner
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return None


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        return board[0][len(board) - 1]
    return None


def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


def example_with_callbacks():
    """
    - [Bug] If I use `st.write` from within the callback, it prints at the top of the 
    page. This is a bit weird and breaks the coding flow of streamlit. 
    - I'm handling context here through `functools.partial`, which may be a bit tricky
    for newcomers but I feel it actually works quite nice / doesn't need the context 
    stuff. 
    """

    # Initialize state.
    state = st.beta_session_state(
        fields=np.full((3, 3), ".", dtype=str),
        next_player="X",
        done=False,
    )

    # Define callbacks to handle button clicks.
    def on_click(i, j):
        if not state.done:
            state.fields[i, j] = state.next_player
            state.next_player = "O" if state.next_player == "X" else "X"
            winner = checkWin(state.fields)
            if winner != ".":
                state.done = True
                st.write(f"{winner} won the game!")
                st.balloons()

    # Show one button for each field.
    cols = st.beta_columns(3)
    for i, row in enumerate(state.fields):
        for j, field in enumerate(row):
            cols[j].button(
                state.fields[i, j],
                key=f"{i}-{j}",
                on_click=functools.partial(on_click, i=i, j=j),
            )


def example_with_signals():
    """
    - **Adrien will write notes and observations here.**
    """
    st.write("example_with_signals")
