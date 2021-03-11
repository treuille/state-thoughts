"""
# Tic Tac Toe Game
"""

import streamlit as st


def example_with_callbacks():
    """
    Tic Tac Toe with callbacks
    """
    state = st.beta_session_state(
        board=["#"] * 9,
        players=["X", "O"],
        current_player=0
    )


    def place_marker(position):
        players = state.players
        current_player = state.current_player
        board = state.board
        board[position] = players[current_player]
        if current_player == 0:
            set_current_player(1)
        else:
            set_current_player(0)


    def col_button(col, index):
        col.button(label=state.board[index], key=str(index), on_click=lambda: place_marker(index))


    def set_board(board):
        state.board = board


    def set_players(players):
        state.players = players


    def set_current_player(player):
        state.current_player = player


    st.markdown("# Streamlit Tic Tac Toe")

    player1 = st.selectbox(label="""Please pick a marker 'X' or 'O' """, options=["X", "O"])
    if player1.upper() == "X":
        player2 = "O"
        st.write("You have chosen " + player1 + ". Player 2 will be " + player2)
        set_players(["X", "O"])
    elif player1.upper() == "O":
        player2 = "X"
        st.write("You have chosen " + player1 + ". Player 2 will be " + player2)
        set_players(["O", "X"])

    cols = st.beta_columns(3)
    index = 0

    for row in range(3):
        for col in cols:
            col_button(col, index)
            index += 1


    def full_board_check():
        board = state.board
        return len([x for x in board if x == "#"]) == 0


    def win_check():
        board = state.board
        current_player = state.current_player
        players = state.players

        if current_player == 0:
            mark = players[1]
        else:
            mark = players[0]

        if board[0] == board[1] == board[2] == mark:
            return True
        if board[3] == board[4] == board[5] == mark:
            return True
        if board[6] == board[7] == board[8] == mark:
            return True
        if board[0] == board[3] == board[6] == mark:
            return True
        if board[1] == board[4] == board[7] == mark:
            return True
        if board[2] == board[5] == board[8] == mark:
            return True
        if board[0] == board[4] == board[8] == mark:
            return True
        if board[2] == board[4] == board[6] == mark:
            return True
        return False


    board = state.board
    game_finished = full_board_check()
    win = win_check()


    def reset():
        set_board(["#"] * 9)
        set_players(["X", "O"])
        set_current_player(0)


    if win:
        st.markdown('## Game Over!')
        st.write("Do you want to play again?")
        play_again = st.button(label="Yes", on_click=reset)

    if game_finished:
        st.write("Do you want to play again?")
        play_again = st.button(label="Yes", on_click=reset)


def example_with_signals():
    """
    Tic Tac Toe with signals
    """
    state = st.beta_session_state(
        board=["#"] * 9,
        players=["X", "O"],
        current_player=0
    )

    RESET = 'reset'
    MARK = 'mark'

    def set_board(board):
        state.board = board

    def set_players(players):
        state.players = players

    def set_current_player(player):
        state.current_player = player

    if st.signal(MARK):
        position = st.beta_signal_context()
        players = state.players
        current_player = state.current_player
        board = state.board
        board[position] = players[current_player]
        if current_player == 0:
            set_current_player(1)
        else:
            set_current_player(0)

    if st.signal(RESET):
        set_board(["#"] * 9)
        set_players(["X", "O"])
        set_current_player(0)

    st.markdown("# Streamlit Tic Tac Toe")

    player1 = st.selectbox(label="""Please pick a marker 'X' or 'O' """, options=["X", "O"])
    if player1.upper() == "X":
        player2 = "O"
        st.write("You have chosen " + player1 + ". Player 2 will be " + player2)
        set_players(["X", "O"])
    elif player1.upper() == "O":
        player2 = "X"
        st.write("You have chosen " + player1 + ". Player 2 will be " + player2)
        set_players(["O", "X"])

    cols = st.beta_columns(3)
    index = 0

    for row in range(3):
        for col in cols:
            col.button(label=state.board[index], key=str(index), signal=MARK, context=index)
            index += 1

    def full_board_check():
        board = state.board
        return len([x for x in board if x == "#"]) == 0

    def win_check():
        board = state.board
        current_player = state.current_player
        players = state.players

        if current_player == 0:
            mark = players[1]
        else:
            mark = players[0]

        if board[0] == board[1] == board[2] == mark:
            return True
        if board[3] == board[4] == board[5] == mark:
            return True
        if board[6] == board[7] == board[8] == mark:
            return True
        if board[0] == board[3] == board[6] == mark:
            return True
        if board[1] == board[4] == board[7] == mark:
            return True
        if board[2] == board[5] == board[8] == mark:
            return True
        if board[0] == board[4] == board[8] == mark:
            return True
        if board[2] == board[4] == board[6] == mark:
            return True
        return False

    board = state.board
    game_finished = full_board_check()
    win = win_check()

    if win:
        st.markdown('## Game Over!')
        st.write("Do you want to play again?")
        st.button(label="Yes", signal=RESET)

    if game_finished:
        st.write("Do you want to play again?")
        st.button(label="Yes", signal=RESET)