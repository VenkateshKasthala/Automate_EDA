# Data Analysis Agent

This project is a Streamlit-based workspace designed to take the manual effort out of the first hour of any data project: Exploratory Data Analysis (EDA). Instead of writing the same boilerplate code to check for nulls, plot distributions, and calculate correlations, this agent handles the heavy lifting by generating a custom analysis suite for any CSV you upload.

The goal was to build a tool that doesn't just "chat" about data, but actually produces the code and statistical deep-dives needed to move a project into the modeling phase.

## How it Works

I designed the system to follow a specific "reasoning before execution" workflow. Most basic AI implementations fail when the dataset is too large or the data is sensitive, so I built this with a more architectural approach:

### 1. The Profiling Logic

When a file is uploaded, the app doesn't just pass the raw data to an LLM. Instead, it performs a local scan of the file using Pandas to extract the **metadata** — things like column names, data types, value distributions, and missing data counts.

### 2. Metadata-Driven Prompting

I followed the best practice of sending only this structural metadata to the **Gemini 2.5 Flash** model. This was a deliberate choice for two reasons:

* **Context Windows:** It prevents the app from breaking or slowing down when handling large datasets that would otherwise exceed the model's token limits.
* **Accuracy:** By providing a clear schema, the "Coder Agent" can write precise Python code without guessing or hallucinating what the columns contain.

### 3. Local Execution & Analysis

The **Coding agent** generates raw Python code (using Pandas, Matplotlib, and Seaborn) which is then executed within the local environment. Once the code runs, the **Analysis Agent** acts as a **Senior Data Scientist** to interpret those specific results—identifying outliers, highlighting data quality issues, and suggesting potential modeling strategies for the next phase of the project.

## Key Features

* **Boilerplate Automation:** Instant generation of summary statistics, distribution plots, and correlation heatmaps.
* **Privacy by Design:** Raw data stays in your local memory; only the schema and statistics are sent to the API.
* **Smart Recommendations:** The Analysis Agent provides insights that go beyond basic numbers to suggest how to handle data cleaning and feature engineering.

## Tech Stack

* **Python 3.12.x**
* **Streamlit** (UI)
* **LangChain** (Agent Orchestration)
* **Google Gemini 2.5 Flash** (Reasoning Engine)
* **Pandas / Seaborn** (Data Processing & Visualization)
