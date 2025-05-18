import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", layout="centered")
st.title("🎮 Tic Tac Toe Game")

# Initialize board state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Game logic
def check_winner(board):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Show grid
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.session_state.board[i] == "" and st.session_state.winner is None:
            if st.button(" ", key=i):
                st.session_state.board[i] = st.session_state.current_player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
        else:
            st.markdown(f"<div style='height:45px; text-align:center; font-size:24px;'>{st.session_state.board[i]}</div>", unsafe_allow_html=True)

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a draw! 🤝")
    else:
        st.success(f"Player {st.session_state.winner} wins! 🎉")

# Restart button
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
