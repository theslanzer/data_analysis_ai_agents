from crewai import Agent, Task
from crewai_tools import FileReadTool, CSVSearchTool, CodeInterpreterTool
from llm_config import llm

csv_tool = FileReadTool(file_path="data/first_1000_rows.csv")

data_analysis_agent = Agent(
    role="Data Cleaning Specialist",
    goal=(
        "Analyze the csv dataset using the tools provided to identify missing values, incorrect data types, and potential outliers. "
        "Generate statistical summaries and correlations between variables."
    ),
    backstory="Specializes in cleaning, preparing data and analysis with expertise in data cleaning and preprocessing. ",
    tools=[csv_tool],
    llm=llm,
    verbose=True,
    allow_code_execution=True
)

data_analysis_task = Task(
    description="""
    Perform a comprehensive analysis of the dataset to identify missing values, incorrect data types, and potential outliers by reading the file. 
    This includes:
    - Identify and quantify missing data across all columns, suggesting imputation or removal strategies.
    - Validate and standardize column data types.
    - Generate descriptive statistics like mean, median, and correlations for numerical columns.
    - Analyze a subset of rows to identify patterns, data relationships, and potential anomalies in the dataset.
    - Infer the dataset's domain, such as customer reviews, sales data, or operational metrics, and suggest potential real-world applications.

    The goal is to provide stakeholders with actionable insights and ensure the dataset is clean and ready for analysis.
    """,
    expected_output="""
    - A table or list of missing values and strategies for handling them.
    - Summary of identified data types and their standardization.
    - Statistical summaries for key columns, including correlations between variables.
    - Recommendations for further analysis or preprocessing.
    """,
    agent=data_analysis_agent
)