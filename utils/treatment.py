
import streamlit as st

def treatment_plan():
    st.markdown(open("templates/treatment_plan.md").read(), unsafe_allow_html=True)
    condition = st.text_input("Enter your diagnosed condition:")
    if st.button("Generate Treatment Plan"):
        with st.spinner("Generating Treatment Recommendation..."):
            st.success(f"Mock Treatment for {condition}: Stay hydrated, rest, and consult your doctor if needed.")
