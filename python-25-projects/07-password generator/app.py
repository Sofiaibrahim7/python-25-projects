import streamlit as st
import random
import string

# Page config
st.set_page_config(page_title="🔐 Password Generator", page_icon="🔒")

st.title("🔐 Secure Password Generator")
st.write("Generate a strong password with custom options.")

# Sidebar options
st.sidebar.header("🔧 Customize your password")

length = st.sidebar.slider("Password length", 6, 40, 12)
use_upper = st.sidebar.checkbox("Include Uppercase Letters (A-Z)", value=True)
use_lower = st.sidebar.checkbox("Include Lowercase Letters (a-z)", value=True)
use_digits = st.sidebar.checkbox("Include Numbers (0-9)", value=True)
use_special = st.sidebar.checkbox("Include Symbols (!@#$...)", value=True)

# Password generation function
def generate_password(length, upper, lower, digits, special):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        return "❌ Please select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))

# Button to generate
if st.button("Generate Password"):
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    st.success("✅ Here is your secure password:")
    st.code(password, language="text")