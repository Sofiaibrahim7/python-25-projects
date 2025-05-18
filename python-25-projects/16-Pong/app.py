import streamlit as st
import time
import random

# Set page config
st.set_page_config(page_title="🏓 Pong Game", layout="centered")

st.title("🏓 Simple Pong Game ")

# Initialize session state
if 'ball_x' not in st.session_state:
    st.session_state.ball_x = 5
    st.session_state.ball_y = 0
    st.session_state.ball_dir = 1  # 1 = right, -1 = left
    st.session_state.score = 0
    st.session_state.paddle_x = 5

# Draw field
def draw_field():
    field = [[" " for _ in range(11)] for _ in range(6)]
    bx, by = st.session_state.ball_x, st.session_state.ball_y
    px = st.session_state.paddle_x

    # Ball
    if 0 <= by < 6 and 0 <= bx < 11:
        field[by][bx] = "🔴"

    # Paddle
    for i in range(-1, 2):
        if 0 <= px + i < 11:
            field[5][px + i] = "🟩"

    # Render
    for row in field:
        st.markdown("".join(row))

# Move ball
def move_ball():
    st.session_state.ball_y += 1
    st.session_state.ball_x += st.session_state.ball_dir

    # Bounce from walls
    if st.session_state.ball_x <= 0 or st.session_state.ball_x >= 10:
        st.session_state.ball_dir *= -1

    # Check for paddle hit
    if st.session_state.ball_y == 5:
        px = st.session_state.paddle_x
        if px - 1 <= st.session_state.ball_x <= px + 1:
            st.session_state.score += 1
            st.session_state.ball_y = 0
            st.session_state.ball_x = random.randint(0, 10)
        else:
            st.warning("❌ Game Over!")
            st.session_state.ball_y = 0
            st.session_state.ball_x = 5
            st.session_state.score = 0

# Game controls
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Move Left"):
        if st.session_state.paddle_x > 1:
            st.session_state.paddle_x -= 1

with col3:
    if st.button("➡️ Move Right"):
        if st.session_state.paddle_x < 9:
            st.session_state.paddle_x += 1

# Move ball
move_ball()

# Draw game field
draw_field()

# Show score
st.success(f"🏆 Score: {st.session_state.score}")
