
import streamlit as st

def predict_disease():
    st.markdown(open("templates/disease_prediction.md").read(), unsafe_allow_html=True)
    symptoms = st.text_area("Enter your symptoms (comma separated):")
    if st.button("Predict Disease"):
        with st.spinner("Analyzing Symptoms..."):
            st.info("Mock Prediction: Common Cold, Migraine, or Mild Fever.")
