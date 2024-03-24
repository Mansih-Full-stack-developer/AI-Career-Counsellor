import cohere

import numpy as np
import streamlit as st

client = cohere.Client(api_key=st.secrets["API_KEY"])




# Function to add last two items of one array to another array
def add_last_two_items(source_array):
    if len(source_array) >= 2:
        last_two_items = source_array[-2:]
        role = last_two_items[0].role
        message = last_two_items[0].message
        st.session_state.chatHistory.append({"role":role, "message":message})
 

st.title("AI Career Counsellor")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("Tell me about your child or Ask me about your child"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        stream = client.chat(
            chat_history= st.session_state.chatHistory,
            message= prompt
               
        )
        
        add_last_two_items(stream.chat_history)


        response = st.write(stream.text)
    st.session_state.messages.append({"role": "assistant", "content": response})