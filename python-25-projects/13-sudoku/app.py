import streamlit as st
import numpy as np

st.set_page_config(page_title="Sudoku Solver", layout="centered")

st.title("🧩 Sudoku")

# Initialize session state
if "grid" not in st.session_state:
    st.session_state.grid = [[0 for _ in range(9)] for _ in range(9)]

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def reset_board():
    st.session_state.grid = [[0 for _ in range(9)] for _ in range(9)]

# Display input grid
with st.form("sudoku_form"):
    for i in range(9):
        cols = st.columns(9)
        for j in range(9):
            cell = cols[j].text_input(
                label=f"Cell {i},{j}",
                value="" if st.session_state.grid[i][j] == 0 else str(st.session_state.grid[i][j]),
                key=f"{i}-{j}",
                max_chars=1
            )
            st.session_state.grid[i][j] = int(cell) if cell.isdigit() and 1 <= int(cell) <= 9 else 0

    submitted = st.form_submit_button("Solve Sudoku")
    reset = st.form_submit_button("Reset Grid")

if reset:
    reset_board()
    st.rerun()

if submitted:
    grid_copy = [row[:] for row in st.session_state.grid]
    if solve_sudoku(grid_copy):
        st.success("🎉 Sudoku Solved Successfully!")
        st.write(np.matrix(grid_copy))
    else:
        st.error("❌ No solution exists for the given Sudoku.")
