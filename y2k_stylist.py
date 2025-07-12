import streamlit as st 
from transformers import pipeline 

st.write("Loading AI personal stylist...")
generator = pipeline("text-generation", model="gpt2")

st.title("💖 Y2K fashion stylist chatbot 💖")
st.write("Hi i'm Cherry your AI fashion stylist. Type your fashion dilemmas and let Cherry fix it")

if "chat" not in st.session_state:
    st.session_state.chat = []  # empty list to store message

user_imput = st.text_input("You:", "")

if user_imput:
    prompt = f"You are a fashion stylist specialising in Y2K looks. Answer this style request: {user_imput}"
    response = generator(prompt, max_length=100, do_sample=True, temperature=0.9) [0] ["generated_text"]

    st.session_state.chat.append(("You", user_imput))
    st.session_state.chat.append(("Stylist", response[len(prompt):]))

for speaker, msg in st.session_state.chat:
    st.markdown(f"**{speaker}:** {msg.strip()}")