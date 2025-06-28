
import streamlit as st
import os
import requests

def call_ibm_granite(prompt):
    api_key = st.secrets["IBM_API_KEY"]
    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "prompt": prompt,
        "model": "granite-3-3-8b-instruct"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("response", "No response from model.")
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Exception occurred: {e}"

def patient_chat():
    st.markdown(open("templates/patient_chat.md").read(), unsafe_allow_html=True)
    question = st.text_input("🩺 Your Question:")
    if st.button("Ask AI"):
        with st.spinner("Generating AI response..."):
            answer = call_ibm_granite(question)
            st.success(answer)
