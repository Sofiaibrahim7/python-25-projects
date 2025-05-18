import streamlit as st
import numpy as np

ROWS = 6
COLS = 7

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.current_player = 1
    st.session_state.winner = 0

# Function to drop disc
def drop_disc(col):
    if st.session_state.winner != 0:
        return

    for row in range(ROWS - 1, -1, -1):
        if st.session_state.board[row][col] == 0:
            st.session_state.board[row][col] = st.session_state.current_player
            if check_winner(row, col):
                st.session_state.winner = st.session_state.current_player
            else:
                st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1
            break

# Function to check for winner
def check_winner(row, col):
    board = st.session_state.board
    player = board[row][col]

    directions = [(0,1), (1,0), (1,1), (1,-1)]

    for dr, dc in directions:
        count = 1

        for i in range(1, 4):
            r, c = row + dr*i, col + dc*i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
            else:
                break

        for i in range(1, 4):
            r, c = row - dr*i, col - dc*i
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == player:
                count += 1
            else:
                break

        if count >= 4:
            return True

    return False

# UI Title
st.title("🔴🟡 Connect Four - Streamlit Version")

# Display player turn or winner
if st.session_state.winner:
    st.success(f"🎉 Player {'🔴' if st.session_state.winner == 1 else '🟡'} wins!")
else:
    st.info(f"Player {'🔴' if st.session_state.current_player == 1 else '🟡'}'s turn")

# Column buttons
cols = st.columns(COLS)
for i in range(COLS):
    if cols[i].button(f"⬇️", key=f"col_{i}"):
        drop_disc(i)

# Display board
symbol = {0: '⚪', 1: '🔴', 2: '🟡'}

for row in range(ROWS):
    cols = st.columns(COLS)
    for col in range(COLS):
        cols[col].markdown(f"<h1 style='text-align: center;'>{symbol[st.session_state.board[row][col]]}</h1>", unsafe_allow_html=True)

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    st.session_state.current_player = 1
    st.session_state.winner = 0
