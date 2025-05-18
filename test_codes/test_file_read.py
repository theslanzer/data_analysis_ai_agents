from crewai_tools import FileReadTool

# 1. Instantiate
csv_tool = FileReadTool(file_path="data/first_100_rows.csv")

# 3. Call the public interface
content = csv_tool.run()

print(content)
