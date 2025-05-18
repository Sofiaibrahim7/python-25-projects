import streamlit as st
import random
import copy

st.set_page_config(page_title="Tic Tac Toe AI", layout="centered")
st.title("🤖 Tic Tac Toe vs AI")

# Initialize board and game state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.game_over = False
    st.session_state.winner = None

# Check winner
def check_winner(board):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Minimax algorithm for AI
def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Draw":
        return 0

    if is_max:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

# Get AI move
def get_best_move(board):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

# Display board and handle clicks
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.session_state.board[i] == "" and not st.session_state.game_over:
            if st.button(" ", key=i):
                st.session_state.board[i] = "X"
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.game_over = True
                    st.session_state.winner = winner
                else:
                    ai_move = get_best_move(st.session_state.board)
                    if ai_move is not None:
                        st.session_state.board[ai_move] = "O"
                    winner = check_winner(st.session_state.board)
                    if winner:
                        st.session_state.game_over = True
                        st.session_state.winner = winner
        else:
            st.markdown(f"<div style='height:45px; text-align:center; font-size:24px;'>{st.session_state.board[i]}</div>", unsafe_allow_html=True)

# Show result
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.info("It's a Draw 🤝")
    elif st.session_state.winner == "X":
        st.success("You Win! 🎉")
    else:
        st.error("AI Wins! 🤖")

# Restart
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.game_over = False
    st.session_state.winner = None
 