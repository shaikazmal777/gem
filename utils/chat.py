import streamlit as st
from gemini_api import generate_gemini_response

def patient_chat():
    st.markdown(open("templates/patient_chat.md").read(), unsafe_allow_html=True)
    question = st.text_input("🩺 Your Question:")
    
    if st.button("Ask AI"):
        with st.spinner("Generating AI response..."):
            answer = generate_gemini_response(question)
            st.success(answer)
