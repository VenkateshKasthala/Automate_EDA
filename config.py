import pandas as pd
from langchain_ollama import OllamaLLM

def get_llm():
    return OllamaLLM(model="mistral")

def get_schema_info(file_path):
    # Extracts metadata from CSV file.
    df = pd.read_csv(file_path)
    schema_info = {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "shape": df.shape
    }
    return schema_info, df

def get_statistical_summary(df):

    # Generates a string-based summary for the LLM to analyze.
    # include="all" captures both numeric and categorical columns
    return df.describe(include="all").to_string()