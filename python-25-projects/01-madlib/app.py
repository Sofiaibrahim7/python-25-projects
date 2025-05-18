import streamlit as st

st.set_page_config(page_title="Madlib Generator", page_icon="📝")

st.title("📝 Madlib Story Generator")
st.subheader("Fill in the blanks and enjoy your custom story!")

# Input fields
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
adjective = st.text_input("Enter an adjective:")
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")

# Generate button
if st.button("Generate Story 🎉"):
    if name and place and adjective and noun and verb:
        st.success("Here's your Madlib story:")
        story = f"""
        Once upon a time, there was a person named {name}.
        {name} lived in a {adjective} place called {place}.
        One day, they found a magical {noun} hidden under a tree.
        Excited and curious, {name} decided to {verb} with it.
        It turned out to be the most unforgettable adventure ever!
        """
        st.write(story)
    else:
        st.warning("Please fill in all the fields to generate the story.")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")
