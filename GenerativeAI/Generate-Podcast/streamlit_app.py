import streamlit as st
import wikipedia
import tiktoken
import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

st.title('AI Generated Podcast')


def split_text(input_text):
    split_texts = sent_tokenize(input_text)
    return split_texts


def create_chunks(split_sents, max_token_len=2500):
    current_token_len = 0
    input_chunks = []
    current_chunk = ""
    for sents in split_sents:
        sent_token_len = len(enc.encode(sents))
        if (current_token_len + sent_token_len) > max_token_len:
            input_chunks.append(current_chunk)
            current_chunk = ""
            current_token_len = 0
        current_chunk = current_chunk + sents
        current_token_len = current_token_len + sent_token_len
    if current_chunk != "":
        input_chunks.append(current_chunk)
    return input_chunks


input_text = st.text_input("Enter Wikipedia URL")

if not input_text:
    st.error("Valid Wikipedia URL needs to be provided")
else:
    wikipedia_id = input_text.rsplit('/', 1)[-1]

if input_text:
    if not wikipedia_id:
        st.error("Valid Wikipedia URL needs to be provided")

    openai_key = st.text_input("Enter OpenAI Key")
    if not openai_key:
        st.error("OpenAI key needs to be provided!")

    if wikipedia_id:
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
        input = wikipedia.page(wikipedia_id, auto_suggest=False)
        wiki_input = input.content
        split_sents = split_text(wiki_input)
        input_chunks = create_chunks(split_sents, max_token_len=2000)
        print(len(input_chunks))
