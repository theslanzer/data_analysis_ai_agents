from crewai import Agent, Task
from crewai_tools import FileReadTool, CSVSearchTool, CodeInterpreterTool
from llm_config import llm

csv_tool = FileReadTool(file_path="data/first_1000_rows.csv")
column_dict = {
"AcceptedCmp1": "1 if customer accepted the offer in the 1st campaign, 0 otherwise",
"AcceptedCmp2": "1 if customer accepted the offer in the 2nd campaign, 0 otherwise",
"AcceptedCmp3": "1 if customer accepted the offer in the 3rd campaign, 0 otherwise",
"AcceptedCmp4": "1 if customer accepted the offer in the 4th campaign, 0 otherwise",
"AcceptedCmp5": "1 if customer accepted the offer in the 5th campaign, 0 otherwise",
"Response": "1 if customer accepted the offer in the last campaign, 0 otherwise",
"Complain": "1 if customer complained in the last 2 years",
"DtCustomer": "date of customer’s enrolment with the company",
"Education": "customer’s level of education",
"Marital": "customer’s marital status",
"Kidhome": "number of small children in customer’s household",
"Teenhome": "number of teenagers in customer’s household",
"Income": "customer’s yearly household income",
"MntFishProducts": "amount spent on fish products in the last 2 years",
"MntMeatProducts": "amount spent on meat products in the last 2 years",
"MntFruits": "amount spent on fruits products in the last 2 years",
"MntSweetProducts": "amount spent on sweet products in the last 2 years",
"MntWines": "amount spent on wine products in the last 2 years",
"MntGoldProds": "amount spent on gold products in the last 2 years",
"NumDealsPurchases": "number of purchases made with discount",
"NumCatalogPurchases": "number of purchases made using catalogue",
"NumStorePurchases": "number of purchases made directly in stores",
"NumWebPurchases": "number of purchases made through company’s web site",
"NumWebVisitsMonth": "number of visits to company’s web site in the last month",
"Recency": "number of days since the last purchase"
}

dataset_inference_agent = Agent(
    role="Dataset Context Specialist",
    goal=(
        "Read the CSV file and then assess the context and purpose of the dataset by analyzing column names, data types, "
        "by sampling few rows. Then, get insights about the domain and the type of data is provided."
    ),
    backstory="An expert in understanding datasets and identifying their purpose, you have a deep understanding of data science and Machine learning and data analysis",
    tools=[csv_tool],
    llm=llm,
    verbose=True,
    allow_code_execution=True
)

dataset_inference_task = Task(
    description=f"""
    Analyze the dataset by reading the file to determine its context, purpose, and structure .
    This includes:
    - Identify meaningful column names and categorize them based on their potential data types (numerical, categorical, date-time, etc.).
    - Analyze a subset of rows to identify patterns, data relationships, and potential anomalies in the dataset.
    - Infer the dataset's domain, such as customer reviews, sales data, or operational metrics, and suggest potential real-world applications.

    The goal is to provide stakeholders with an intuitive understanding of the dataset and its potential uses without requiring them to delve into the raw data.
    """,
    expected_output="""
    A descriptive overview of the dataset's structure and purpose, highlighting:
    - Data columns and their inferred roles.
    - High-level insights into the type of data (e.g., transactional, temporal, or categorical).
    - Recommendations for possible applications or use cases.
    """,
    agent=dataset_inference_agent
)