from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Import the csv_tool from our tools
from data_analysis_crew2.tools.csv_read import csv_tool

# Uncomment the following line to use an example of a custom tool
# from data_analysis_crew2.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class DataAnalysisCrew2Crew():
	"""DataAnalysisCrew2 crew"""

	@agent
	def suggestion_generation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['suggestion_generation_agent'],
			tools=[csv_tool],
			verbose=True
		)

	@agent
	def reporting_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_agent'],
			tools=[csv_tool],
			verbose=True
		)

	@agent
	def chart_generation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['chart_generation_agent'],
			allow_code_execution=True,
			verbose=True
		)

	@task
	def suggestion_generation(self) -> Task:
		return Task(
			config=self.tasks_config['suggestion_generation']
		)

	@task
	def table_generation(self) -> Task:
		return Task(
			config=self.tasks_config['table_generation']
		)

	@task
	def chart_generation(self) -> Task:
		return Task(
			config=self.tasks_config['chart_generation']
		)

	@task
	def final_report_assembly(self) -> Task:
		return Task(
			config=self.tasks_config['final_report_assembly']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the DataAnalysisCrew2 crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)