from crewai import Crew, Process
from agent.inference_agent import dataset_inference_agent, dataset_inference_task 
from agent.analysis_agent import data_analysis_agent,data_analysis_task
from agent.visualization_agent import visualization_agent, visualization_task
from agent.report_agent import markdown_report_agent, markdown_report_task

csv_analysis_crew = Crew(
    agents=[
        dataset_inference_agent,
        data_analysis_agent,
        visualization_agent,
        markdown_report_agent
    ],
    tasks=[dataset_inference_task, data_analysis_task, visualization_task, markdown_report_task],
    process=Process.sequential,
    verbose=True
)