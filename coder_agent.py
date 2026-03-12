from config import get_llm, get_schema_info

def run_eda_agent(file_path):
    llm = get_llm()
    metadata, df = get_schema_info(file_path)

    prompt = f"""
    You are a data scientist.
    
    Here is the dataset metadata:
    {metadata}

    Write Python code using pandas, matplotlib, and seaborn to:
    1. Generate summary statistics
    2. Plot distributions for numerical columns
    3. Plot correlation heatmap
    4. Identify missing values visually

    Only return executable Python code.
    """

    print("Generating EDA Code via Mistral")
    generated_code = llm.invoke(prompt)
    
    print(generated_code)
    return generated_code

if __name__ == "__main__":
    CSV_PATH = "/Users/kvenkateshrao/Downloads/Ice Cream Ratings.csv"
    run_eda_agent(CSV_PATH)