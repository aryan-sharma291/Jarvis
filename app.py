# streamlit run app.py
import openai

import importlib

client = openai.OpenAI(
    api_key="Your Api Key"

)
import pyttsx3
import streamlit as st
import random
import time



user_text = ""
st.set_page_config(page_title="Jarvis", page_icon="🤖")
st.title("Jarvis")

# afplay

import datetime

import speech_recognition as sr

chat_container = st.container()
if "messages" not in st.session_state:
    st.session_state.messages = []

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        hi = st.warning("Listening, sir...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            hi.empty()
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            st.warning("Sorry, could not recognize your voice")


def speak(audio, user_input_text, ai_response_text):
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()

    # 1. Talk first (This usually works fine alone)
    engine.say(audio)
    engine.runAndWait()

    # 2. Re-initialize for the Save action (This "resets" the driver)
    importlib.reload(pyttsx3)
    engine = pyttsx3.init()
    date = datetime.datetime.now()


    # 3. Save to file separately
    engine.save_to_file(f"{ai_response_text}", f"{user_input_text.replace(' ', '_')}_{date.strftime('%m-%d-%Y_%H-%M-%S')}.wav")
    engine.runAndWait()


with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
st.write("---")
col1, col2, col3, col4, col5 = st.columns(8)

with col3:
    if st.button("Jarvis"):
        user_text = listen()

if user_text != "":
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= [{"role": "system", "content": "Speak like Jarvis."},
                      {"role": "user", "content": user_text}],
        max_tokens=100
    )
    final_rely = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": final_rely})
    with st.chat_message("assistant"):
        st.markdown(final_rely)
    speak(final_rely, user_text, response.choices[0].message.content)

    st.rerun()

