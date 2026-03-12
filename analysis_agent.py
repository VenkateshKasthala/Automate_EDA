from config import get_llm, get_schema_info, get_statistical_summary

def run_analysis_pipeline(file_path):
    llm = get_llm()
    metadata, df = get_schema_info(file_path)
    
    stats_string = get_statistical_summary(df)
    
    insight_prompt = f"""
    You are a Senior Data Scientist. 

    Here are summary statistics: {stats_string}
    
    Based ONLY on these numbers, Provide:
    - Key patterns
    - Potential data quality issues
    - Interesting correlations
    - Recommendations for modeling
    
    Be concise and professional.
    """

    insights = llm.invoke(insight_prompt)
    print(insights)

if __name__ == "__main__":
    CSV_PATH = "/Users/kvenkateshrao/Downloads/Ice Cream Ratings.csv"
    run_analysis_pipeline(CSV_PATH)