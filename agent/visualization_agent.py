from crewai import Agent, Task
from crewai_tools import FileReadTool, CSVSearchTool, CodeInterpreterTool
from llm_config import llm

csv_tool = FileReadTool(file_path="data/first_1000_rows.csv")

visualization_agent = Agent(
    role="Visualization Expert",
    goal=(
        "Generate meaningful visualizations usig python such as histograms, scatter plots, line plots, bar charts, "
        "and heatmaps using pyhton to provide insights into the data. Save all visualizations to a 'graphs/' directory."
    ),
    backstory="Specializes in creating compelling and informative visualizations. you are an expert in python pandas matplotlib and seaborn and data visualization and will create story  ",
    tools=[csv_tool],
    llm=llm,
    verbose=True,
    allow_code_execution=True
)

visualization_task = Task(
    description="""
    Create meaningful visualizations dynamically based on the dataset's content using python. 
    The visualizations should include:
    - Histograms: For numerical columns to showcase data distributions.
    - Bar Charts: For categorical columns with limited unique values to highlight frequencies.
    - Correlation Heatmaps: To represent the correlations between numerical variables.
    - Scatter Plots and Line Plots: To show relationships and trends.
    - Any other relevant visualizations based on the dataset's content.

    Save the visualizations as image files in the 'graphs/' directory and ensure they are 
    properly labeled with titles, axis names, and legends.

    These visualizations aim to uncover key patterns and relationships in the dataset.
    """,
    expected_output="""
    - A set of graphs saved in the 'graphs/' directory.
    - Each graph is annotated and labeled for clarity and ready for embedding in the final report.
    use the matplotlib library to create graphs.

    """,
    agent=visualization_agent
)