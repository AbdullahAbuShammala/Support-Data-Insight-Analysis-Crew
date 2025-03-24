from crewai_tools import FileReadTool

# Create a tool for reading the CSV file
csv_tool = FileReadTool(file_path='src/data_analysis_crew2/data/support_tickets_data.csv') 