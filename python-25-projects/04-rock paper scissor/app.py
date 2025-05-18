import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="✊ Rock, Paper, Scissors", page_icon="✌️", layout="centered")

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>✊ Rock, Paper, Scissors ✋</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Play against the computer and test your luck!</p>", unsafe_allow_html=True)

# Choices and emojis
choices = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

user_choice = st.selectbox("Choose your move:", list(choices.keys()))

# Play button
if st.button("Play"):
    comp_choice = random.choice(list(choices.keys()))

    # Show choices
    st.markdown(f"### 🙋 You chose: {choices[user_choice]} {user_choice}")
    st.markdown(f"### 💻 Computer chose: {choices[comp_choice]} {comp_choice}")

    # Game logic
    if user_choice == comp_choice:
        result = "😐 It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "🎉 You win!"
    else:
        result = "😞 You lose!"

    # Display result
    st.markdown(f"<h3 style='text-align: center; color: green;'>{result}</h3>", unsafe_allow_html=True)