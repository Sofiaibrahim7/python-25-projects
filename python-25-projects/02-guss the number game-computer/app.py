import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game", page_icon="🎯")

st.title("🎯 Guess the Number Game")
st.subheader("I have selected a number between 1 and 100. Can you guess it?")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.message = ""

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Guess"):
    st.session_state.tries += 1
    if guess < st.session_state.number:
        st.session_state.message = "🔻 Too low! Try a higher number."
    elif guess > st.session_state.number:
        st.session_state.message = "🔺 Too high! Try a lower number."
    else:
        st.success(f"🎉 Correct! You guessed the number {st.session_state.number} in {st.session_state.tries} tries.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.tries = 0
            st.session_state.message = ""

# Show feedback
st.write(st.session_state.message)
