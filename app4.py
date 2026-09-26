import os
from dotenv import load_dotenv
from google import genai
import streamlit as st
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
st.set_page_config(page_title="ai traslator",layout="wide")
st.title("ai translator")
st.caption("powered by gemini")
languages = ["English", "Hindi", "Telugu", "Kannada", "Tamil", "Malayalam", "Chinese", "French", "Japanese", "Urdu"]
if "source_language" not in st.session_state:
    st.session_state.source_language = "English"

if "destination_language" not in st.session_state:
    st.session_state.destination_language = "Hindi"
col1, col2 = st.columns(2)
with col1:
        source_language = st.selectbox(
            "Source Language",
            languages,
            index = languages.index(st.session_state.source_language)
)
with col2:
        destination_language = st.selectbox(
            "Destination Language",
            languages,
            index = languages.index(st.session_state.destination_language)
)
st.session_state.source_language = source_language
st.session_state.destination_language = destination_language
if st.button("swap"):
    temp = st.session_state.source_language
    st.session_state.source_language = st.session_state.destination_language
    st.session_state.destination_language = temp
text = st.text_area("Enter text to translate")
if st.button("translate"):
    prompt = f"""act as professional translator

strict rules:
1.don't add extra information
2.don't remove extra information
3.don't summarize the {text}
4.give me response like in native {destination_language}

source Language is {source_language}
destination Language is {destination_language}
text to translate is {text}
"""

    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = prompt)
    st.subheader("Translate")
    st.text_area("Translated Text: ",response.text)
with st.sidebar:
    st.subheader("model info")
    st.code("gemini-3.6-flash")