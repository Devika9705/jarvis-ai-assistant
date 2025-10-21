import streamlit as st
from Jarvis_Logic import takeCommand, say, ask_chatgpt  # your main file renamed to jarvis.py
import os
import webbrowser
import datetime

st.set_page_config(page_title="Jarvis Dashboard", layout="centered")

# 💠 Title and Info
st.markdown("<h1 style='text-align: center; color: cyan;'>🤖 Jarvis AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("###### 🎙 Speak or type your query below", unsafe_allow_html=True)

# 🎧 Voice Command Button
if st.button("🎧 Start Listening"):
    with st.spinner("Listening..."):
        query = takeCommand()
        if query:
            st.success(f"🗣 You said: `{query}`")

            # Mini-logic for demo (or call handle_command())
            if "search" in query:
                say("Searching Google")
                webbrowser.open(f"https://www.google.com/search?q={query.replace('search','')}")
                st.info("🔍 Google search opened.")

            elif "time" in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                say(f"The time is {current_time}")
                st.info(f"⏰ Time: {current_time}")

            elif "chat" in query or "question" in query:
                say("What's your question?")
                follow_up = takeCommand()
                if follow_up:
                    say("Thinking...")
                    answer = ask_chatgpt(follow_up)
                    st.success(f"🤖 Jarvis: {answer}")
                    say(answer)

            elif "open youtube" in query:
                webbrowser.open("https://youtube.com")
                say("Opening YouTube")
                st.info("▶️ YouTube opened.")

            elif "bye" in query:
                say("Goodbye madam.")
                st.warning("👋 Jarvis session ended.")

            else:
                say("Sorry, I don't understand that.")
                st.error("❌ Unknown command.")

# ✍️ Manual Query
st.markdown("Or type your query:")
manual_input = st.text_input("")

if manual_input:
    st.write(f"🧠 Thinking on: `{manual_input}`")
    answer = ask_chatgpt(manual_input)
    st.success(f"🤖 Jarvis: {answer}")
    say(answer)
