import streamlit as st

def count_letters(text):
    upper_count= sum(1 for char in text if char.isupper())
    lower_count= sum(1 for char in text if char.islower())
    total_count=upper_count+lower_count
    return upper_count, lower_count, total_count

def count_specific_letter(text, letter):
    return text.count(letter)

def count_words(text):
    words=text.split()
    return len(words)    

st.title('Case-Sensitive Word Counter')

input_text= st.text_area('Enter your text here:', height=200)

if input_text:
    st.write('**Analysis Results**')
    
    upper_count, lower_count, total_count=count_letters(input_text)
    st.write(f'Total number of letters: {total_count}')

    letter_to_count=st.text_input('Enter a letter to count:')
    
    if letter_to_count:
        times=count_specific_letter(input_text, letter_to_count)
        st.write(f'Number of times"{letter_to_count}" is: {times}')
    
    
    