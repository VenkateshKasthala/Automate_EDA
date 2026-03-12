import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_engine():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("Missing GOOGLE_API_KEY in .env")
        st.stop()
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key, temperature=0)

st.set_page_config(page_title="Data Profiler", layout="wide")
st.title(" AI Data Analysis Agent")

with st.sidebar:
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    engine = get_engine()
    
    st.subheader("Raw Data Preview")
    st.dataframe(df.head()) 

    if st.button("Generate Analysis & Insights"):
        with st.spinner("Compiling EDA Logic..."):
            code_prompt = f"""
            You are a data scientist.
            Task: Write a Python script using pandas, matplotlib, and seaborn for EDA.
    
            Here is the dataset metadata: {df.columns.tolist()}

            1. Generate summary statistics
            2. Plot distributions for numerical columns
            3. Plot correlation heatmap
            4. Identify missing values visually

            Only return executable Python code.NO introductory or concluding text.
            No Backticks(```)
            NO  extra print statements at the end (e.g., 'EDA script completed').
            """
            generated_code = engine.invoke(code_prompt).content
            st.subheader("Implementation Code")
            st.code(generated_code, language="python")

        st.divider()

        with st.spinner("Generating Technical Report..."):
            stats_summary = df.describe(include="all").to_string()
            
            insight_prompt = f"""
            You are a Senior Data Scientist. 
            Here are summary statistics: {stats_summary}
            
            Based ONLY on these numbers, Provide:
            1. Key patterns
            2. Potential data quality issues
            3. Interesting correlations
            4. Recommendations for modeling

            STRICT RULES:
            - Start the response immediately with the first heading '### 1. Key Patterns'.
            - NO conversational filler (e.g., 'Here is the analysis', 'Based on the stats').
            - Format with clean spacing and professional English.
            
            Be concise and professional.            
            """
            insights = engine.invoke(insight_prompt).content
        
            st.subheader("Technical Analysis")
            st.markdown(insights)