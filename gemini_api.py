import os
import google.generativeai as genai
import streamlit as st

# Load API key
api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
genai.configure(api_key=api_key)

# Use correct model name
model = genai.GenerativeModel("models/gemini-1.5-pro")

def generate_gemini_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"[Gemini ERROR]: {e}")
        return f"Gemini Error: {e}"
