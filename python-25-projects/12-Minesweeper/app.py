import streamlit as st
import random

# Helper function to initialize board in session state
def initialize_board(dim_size, num_bombs):
    board = [[None for _ in range(dim_size)] for _ in range(dim_size)]
    bombs = set()
    while len(bombs) < num_bombs:
        loc = random.randint(0, dim_size**2 - 1)
        row, col = divmod(loc, dim_size)
        if (row, col) in bombs:
            continue
        bombs.add((row, col))
        board[row][col] = '*'
    # Assign values
    for r in range(dim_size):
        for c in range(dim_size):
            if board[r][c] == '*':
                continue
            board[r][c] = sum(
                1 for rr in range(max(0, r-1), min(dim_size, r+2))
                for cc in range(max(0, c-1), min(dim_size, c+2))
                if (rr != r or cc != c) and board[rr][cc] == '*'
            )
    return board, bombs

# Initial state setup
if 'board' not in st.session_state:
    st.session_state.dim = 5
    st.session_state.bombs = 5
    st.session_state.board, st.session_state.bomb_set = initialize_board(st.session_state.dim, st.session_state.bombs)
    st.session_state.dug = set()
    st.session_state.game_over = False
    st.session_state.victory = False

st.title("💣 Minesweeper Game ")
st.write("Click cells to reveal. Avoid the bombs!")

# Input for cell selection
row = st.number_input("Row", min_value=0, max_value=st.session_state.dim-1, step=1)
col = st.number_input("Col", min_value=0, max_value=st.session_state.dim-1, step=1)

# Dig button
if st.button("Dig"):
    if (row, col) in st.session_state.dug:
        st.warning("Already dug here!")
    elif (row, col) in st.session_state.bomb_set:
        st.session_state.dug.add((row, col))
        st.session_state.game_over = True
    else:
        def dig(r, c):
            if (r, c) in st.session_state.dug:
                return
            st.session_state.dug.add((r, c))
            if st.session_state.board[r][c] == 0:
                for rr in range(max(0, r-1), min(st.session_state.dim, r+2)):
                    for cc in range(max(0, c-1), min(st.session_state.dim, c+2)):
                        if (rr, cc) != (r, c):
                            dig(rr, cc)
        dig(row, col)
        if len(st.session_state.dug) >= st.session_state.dim**2 - st.session_state.bombs:
            st.session_state.victory = True

# Display board
for r in range(st.session_state.dim):
    cols = st.columns(st.session_state.dim)
    for c in range(st.session_state.dim):
        cell = " "
        if (r, c) in st.session_state.dug:
            val = st.session_state.board[r][c]
            cell = "💣" if val == '*' else str(val)
        elif st.session_state.game_over and (r, c) in st.session_state.bomb_set:
            cell = "💣"
        cols[c].button(cell, key=f"{r}-{c}")

# Messages
if st.session_state.game_over:
    st.error("💥 Game Over!")
elif st.session_state.victory:
    st.success("🎉 You Win!")

# Reset button
if st.button("Restart"):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

   