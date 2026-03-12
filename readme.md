# Data Profiling Agent

A lightweight Streamlit application that automates the initial stages of Exploratory Data Analysis. The tool uses Gemini 2.5 Flash to generate clean Python implementation code and high-level statistical insights from uploaded CSVs.

## Core Functionality

* **Automated Code Generation**: Produces boilerplate for summary statistics, distributions, and correlation heatmaps using Pandas, Matplotlib, and Seaborn.
* **Prompt Engineering**: Leverages custom system instructions and negative constraints to ensure the LLM returns only raw, executable Python code without conversational filler or unnecessary formatting.
* **Technical Insights**: Provides concise analysis of data patterns, quality issues (outliers/nulls), and modeling recommendations based on descriptive statistics.
* **Cloud Integration**: Uses cloud-based processing to maintain a zero-footprint on local system resources (RAM/CPU).

## Tech Stack

* **Language**: Python 3.12.x
* **Framework**: Streamlit
* **LLM**: Gemini 2.5 Flash
* **Environment**: python-dotenv
