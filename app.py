
import streamlit as st
from utils.chat import patient_chat
from utils.disease_predict import predict_disease
from utils.treatment import treatment_plan
from utils.analytics import health_analytics

st.set_page_config(page_title="HealthAI Assistant", layout="wide")

st.markdown("""
    <style>
        .main {background-color: #f0f2f6;}
        .sidebar .sidebar-content {background-color: #e0f7fa;}
        .stButton>button {
            background-color: #00796b;
            color: white;
            font-weight: bold;
            border-radius: 0.5rem;
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #ffffff;
            border-radius: 0.5rem;
            padding: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 HealthAI: Intelligent Healthcare Assistant")

menu = st.sidebar.radio("📋 Menu", ["💬 Patient Chat", "🧪 Disease Prediction", "💊 Treatment Plan", "📊 Health Analytics"])

if menu == "💬 Patient Chat":
    patient_chat()
elif menu == "🧪 Disease Prediction":
    predict_disease()
elif menu == "💊 Treatment Plan":
    treatment_plan()
elif menu == "📊 Health Analytics":
    health_analytics()
