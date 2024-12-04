import streamlit as st

# Sample dictionary data
dictionary = {
    "apple": "You are the apple of my eye!.",
    "banana": "موز یا کیله.",
    "orange": "نارنج.",
    "grape": "انگور.",
    "watermelon": "هندوانه.",
    "peach": "هلو.",
    "pear": "گلابی."
}

# Title of the app
st.title("Khudai_Dad__'s Online Dictionary")

# Input field for user to enter a word
word = st.text_input("لطفا لغت مورد نظر خود را وارد کنید:")

# Check if the word is in the dictionary
if word:
    # Normalize the input by converting it to lowercase
    definition = dictionary.get(word.lower(), "این لغت در دیکشنری موجود نیست.")
    st.write(f"تعریف   :  {definition}")
