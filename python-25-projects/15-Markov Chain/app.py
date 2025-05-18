import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Markov Chain Simulator", layout="centered")

st.title("🎲 Markov Chain Simulator ")
st.write("Ek simple Markov Chain simulator jo transition matrix use karta hai states predict karne ke liye.")

# --- Step 1: Define States ---
states = st.text_input("Enter states separated by comma (e.g., Sunny,Rainy,Cloudy)", "Sunny,Rainy,Cloudy")
states = [state.strip() for state in states.split(",")]

# --- Step 2: Create Transition Matrix ---
st.subheader("🔁 Enter Transition Matrix")
matrix_input = []
for i, state_from in enumerate(states):
    row = st.text_input(f"Probabilities from '{state_from}' to all states (comma-separated)", "0.3,0.4,0.3")
    try:
        row_vals = [float(val) for val in row.split(",")]
        if len(row_vals) != len(states):
            st.warning(f"Row {i+1} should have {len(states)} values.")
        matrix_input.append(row_vals)
    except:
        st.error("Please enter valid numbers.")

# --- Step 3: Show Matrix ---
if len(matrix_input) == len(states):
    matrix = np.array(matrix_input)
    st.write("📊 Transition Matrix:")
    st.dataframe(matrix)

    # --- Step 4: Select Initial State and Steps ---
    st.subheader("⚙️ Simulation Settings")
    initial_state = st.selectbox("Choose initial state", states)
    steps = st.slider("Number of steps to simulate", 1, 20, 5)

    # --- Step 5: Simulate Markov Chain ---
    def simulate_markov_chain(matrix, states, start_state, steps):
        state_sequence = [start_state]
        current_state = states.index(start_state)

        for _ in range(steps):
            next_state = np.random.choice(
                range(len(states)), p=matrix[current_state]
            )
            state_sequence.append(states[next_state])
            current_state = next_state

        return state_sequence

    if st.button("🔁 Run Simulation"):
        sequence = simulate_markov_chain(matrix, states, initial_state, steps)
        st.success("✅ Simulation Complete!")
        st.write("➡️ State Sequence:")
        st.write(" → ".join(sequence))
