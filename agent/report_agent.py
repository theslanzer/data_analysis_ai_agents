from crewai import Agent, Task
from crewai_tools import FileReadTool, CSVSearchTool, CodeInterpreterTool
from llm_config import llm
from agent.inference_agent import dataset_inference_task
from agent.analysis_agent import data_analysis_task
from agent.visualization_agent import visualization_task

csv_tool = FileReadTool(file_path="data/first_1000_rows.csv")
code_tool = CodeInterpreterTool()

markdown_report_agent = Agent(
    role="Report Specialist",
    goal=(
        "Compile all findings, analysis, and visualizations into a structured markdown report. "
        "Embed graphs and provide clear sections for analysis and summary. you will give detailed well formatted summart "
    ),
    backstory="Expert in synthesizing data insights into polished reports.",
    tools=[csv_tool],
    llm=llm,
    verbose=True,
    
)

markdown_report_task = Task(
    description="""
    Create a detailed markdown report summarizing all analysis and visualizations. 
    The report should include:
    - Dataset Overview: Key insights from the context analysis, such as dataset 
      structure and inferred purpose.
    - Data Cleaning Summary: Detailed information on missing data, outliers, 
      and cleaning steps performed.
    - Statistical Summary: Tables and summaries of computed descriptive statistics.
    - Visualizations: Embedded images of charts created in the visualization task, 
      with captions explaining the insights.
    - Recommendations: Suggestions for further data preprocessing, modeling, 
      or potential use cases for the dataset.

    The report should be:
    - Organized into clearly labeled sections with a logical flow.
    - Formatted for stakeholders who may not have technical expertise.
    - Focused on actionable insights and takeaways.
    """,
    expected_output="""
    - A markdown report saved as 'report.md'.
    - Includes sections for analysis, summaries, and embedded visualizations.
    The Graphs and with bar and line plots and so on 
    - Provides actionable insights and recommendations.
    add the graphs in place of wherte it is necessary make sure you give it as detailed and well formatted as possible
    """,
    agent=markdown_report_agent,
    context=[dataset_inference_task, data_analysis_task, visualization_task],
    output_file='report.md'
)