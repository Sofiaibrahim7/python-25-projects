import streamlit as st

st.set_page_config(page_title="Computer Guesses Your Number", page_icon="🧠")

st.title("🤖 Computer Guesses Your Number!")
st.subheader("Think of a number between 1 and 100, and I'll try to guess it!")

# Initialize session state
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if "done" not in st.session_state:
    st.session_state.done = False

# Show current guess
if not st.session_state.done:
    st.write(f"My guess is: **{st.session_state.guess}**")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔼 Too Low"):
            st.session_state.low = st.session_state.guess + 1
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    with col2:
        if st.button("🔽 Too High"):
            st.session_state.high = st.session_state.guess - 1
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    with col3:
        if st.button("✅ Correct!"):
            st.success(f"I guessed it! Your number is {st.session_state.guess} 🎉")
            st.session_state.done = True
else:
    if st.button("🔄 Play Again"):
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.guess = 50
        st.session_state.done = False
