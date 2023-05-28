import streamlit as st
import wikipedia
import tiktoken
import nltk
import openai
from PIL import Image

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

st.title('AI Generated Podcast')
htp = "https://github.com/sumanentc/Machine-Learning-with-Python/blob/main/GenerativeAI/Generate-Podcast/ai-podcast.jpg"
st.image(htp, caption='logo', width=350)


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


def get_instruct_prompt(topic):
    return f"""
    You are a {topic} enthusiast who is doing a research for a podcast. Your task is to extract relevant information from the Result delimited by triple quotes. 
    Please identify 2 interesting questions and answers which can be used for a podcast discussion.
    The identified discussions should be returned in thr following format.
    - Highlight 1 from the text
    - Highlight 2 from the text
    """


def get_chat_outputs(requestMessages):
    chatOutputs = []
    for request in requestMessages:
        chatOutput = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                  messages=[
                                                      {"role": "system", "content": "You are a helpful assistant."},
                                                      {"role": "user", "content": request}
                                                  ]
                                                  )
        chatOutputs.append(chatOutput)
    return chatOutputs


def get_podcast_facts(chatOutputs):
    podcastFacts = ""
    for chats in chatOutputs:
        podcastFacts = podcastFacts + chats.choices[0].message.content
    return podcastFacts


input_text = st.text_input(label="Enter Wikipedia URL", value="https://en.wikipedia.org/wiki/Lionel_Messi")

if not input_text:
    st.error("Valid Wikipedia URL needs to be provided")
else:
    wikipedia_id = input_text.rsplit('/', 1)[-1]

if input_text:
    if not wikipedia_id:
        st.error("Valid Wikipedia URL needs to be provided")

    openai_key = st.text_input(label="Enter OpenAI Key", type="password")

    if wikipedia_id:
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
        input = wikipedia.page(wikipedia_id, auto_suggest=False)
        wiki_input = input.content
        split_sents = split_text(wiki_input)
        input_chunks = create_chunks(split_sents, max_token_len=2000)

    if not openai_key:
        st.error("OpenAI key needs to be provided!")
    else:
        openai.api_key = openai_key
        topic_name = st.text_input(label="Enter Podcast Topic Name", value="Sports")
        instructPrompt = get_instruct_prompt(topic_name)
        requestMessages = []
        for text in input_chunks:
            requestMessage = instructPrompt + f"Result: ```{text}```"
            requestMessages.append(requestMessage)
        try:
            chatOutputs = get_chat_outputs(requestMessages)
            podcast_facts = get_podcast_facts(chatOutputs)
        except ex:
            st.error(f"Exception occurred while interacting with OpenAI {ex}")
        st.text_area(label="", value=podcast_facts, height=200)
