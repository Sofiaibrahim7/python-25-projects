import streamlit as st
import random

# List of possible words
words = ['python', 'streamlit', 'developer', 'hangman', 'computer', 'keyboard']

# Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words).lower()
    st.session_state.guessed = ['_'] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []

# Display game information
st.title("🎯 Hangman Game")
st.write(f"Guess the word! You have {st.session_state.attempts} attempts left.")
st.write(" ".join(st.session_state.guessed))

# User input: Guess a letter
guess = st.text_input("Enter a letter:", max_chars=1).lower()

if guess:
    # Check if input is a valid letter
    if not guess.isalpha() or len(guess) != 1:
        st.warning("❌ Please enter a single letter.")
    elif guess in st.session_state.guessed_letters:
        st.warning("⚠️ You already guessed that letter.")
    else:
        # Update guessed letters
        st.session_state.guessed_letters.append(guess)

        # Check if letter is in the word
        if guess in st.session_state.word:
            for i in range(len(st.session_state.word)):
                if st.session_state.word[i] == guess:
                    st.session_state.guessed[i] = guess
            st.success(f"✅ Good guess! The word contains '{guess}'.")
        else:
            st.session_state.attempts -= 1
            st.error(f"❌ Wrong guess! You have {st.session_state.attempts} attempts left.")

        # Check if the word is guessed
        if "_" not in st.session_state.guessed:
            st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
            if st.button("Play Again"):
                st.session_state.word = random.choice(words).lower()
                st.session_state.guessed = ['_'] * len(st.session_state.word)
                st.session_state.attempts = 6
                st.session_state.guessed_letters = []

        elif st.session_state.attempts == 0:
            st.error(f"💀 Game Over! The word was: {st.session_state.word}")
            if st.button("Play Again"):
                st.session_state.word = random.choice(words).lower()
                st.session_state.guessed = ['_'] * len(st.session_state.word)
                st.session_state.attempts = 6
                st.session_state.guessed_letters = []

