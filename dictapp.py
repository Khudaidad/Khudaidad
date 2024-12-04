import streamlit as st

# Sample dictionary data
dictionary = {
    "apple": "سیب.",
    "banana": "موز یا کیله.",
    "orange": "نارنج.",
    "grape": "انگور."
}

# Title of the app
st.title("Khudai_dad__'S Online Dictionary")

# Input field for user to enter a word
word = st.text_input("                        لغت مورد نظر خود را وارد کنید :")

# Check if the word is in the dictionary
if word:
    definition = dictionary.get(word.lower(), "Word not found in the dictionary.")
    st.write(f"Definition: {definition}")
    
    