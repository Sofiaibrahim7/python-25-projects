import streamlit as st
import time

# Page config
st.set_page_config(page_title="⏳ Countdown Timer", page_icon="⏰")

st.title("⏳ Countdown Timer")
st.write("Set your timer and watch it countdown live!")

# User input
col1, col2 = st.columns(2)
with col1:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, value=0)
with col2:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, value=10)

if st.button("Start Timer"):
    total_seconds = int(minutes * 60 + seconds)
    if total_seconds == 0:
        st.warning("Please set a time greater than 0 seconds.")
    else:
        st.success(f"⏰ Countdown started for {minutes} minutes and {seconds} seconds.")
        placeholder = st.empty()

        for remaining in range(total_seconds, -1, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"⏱️ {mins:02d}:{secs:02d}"
            placeholder.markdown(f"<h1 style='text-align:center;'>{timer_display}</h1>", unsafe_allow_html=True)
            time.sleep(1)

        st.balloons()
        st.success("⏳ Time's up!")
