import streamlit as st
from transformers import pipeline

st.title('Summarize text')
context = st.text_input('input text or paragraph')
max = st.number_input('maximum words')
min = st.number_input('minimum words')


if st.button('submit'):
    summarizer = pipeline("summarization")
    st.write(summarizer(context, min_length=int(min), max_length=int(max)))

