import streamlit as st
import random

# Set up session state for the game
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.direction = 'RIGHT'
    st.session_state.score = 0

# Move snake based on direction
def move_snake():
    head = st.session_state.snake[0]
    if st.session_state.direction == 'UP':
        new_head = (head[0], head[1] - 1)
    elif st.session_state.direction == 'DOWN':
        new_head = (head[0], head[1] + 1)
    elif st.session_state.direction == 'LEFT':
        new_head = (head[0] - 1, head[1])
    else:
        new_head = (head[0] + 1, head[1])
    
    # Check for collisions
    if new_head in st.session_state.snake or not (0 <= new_head[0] < 10 and 0 <= new_head[1] < 10):
        st.error("Game Over! Refresh to restart.")
        return
    
    st.session_state.snake = [new_head] + st.session_state.snake

    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.pop()

# Game controls
st.title("🐍 Snake Game")
st.write(f"**Score**: {st.session_state.score}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Left"):
        st.session_state.direction = 'LEFT'
with col2:
    if st.button("⬆️ Up"):
        st.session_state.direction = 'UP'
    if st.button("⬇️ Down"):
        st.session_state.direction = 'DOWN'
with col3:
    if st.button("➡️ Right"):
        st.session_state.direction = 'RIGHT'

if st.button("Move"):
    move_snake()

# Draw the grid
grid = ""
for y in range(10):
    for x in range(10):
        if (x, y) == st.session_state.food:
            grid += "🍎 "
        elif (x, y) in st.session_state.snake:
            grid += "🟩 "
        else:
            grid += "⬜ "
    grid += "\n"

st.text(grid)
