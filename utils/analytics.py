
import streamlit as st
import pandas as pd
import plotly.express as px

def health_analytics():
    st.markdown(open("templates/analytics.md").read(), unsafe_allow_html=True)
    file = st.file_uploader("Upload Health Metrics CSV", type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)
        for col in df.columns[1:]:
            fig = px.line(df, x=df.columns[0], y=col, title=f"{col} Trend Over Time", markers=True)
            st.plotly_chart(fig)
