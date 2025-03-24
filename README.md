# Support-Data-Insight-Analysis-Crew

A powerful data analysis tool built with CrewAI that analyzes support ticket data, generates visualizations, and produces comprehensive reports.

## Overview

This project uses the CrewAI framework to create a specialized AI crew for analyzing CSV data from support tickets. The crew performs multiple specialized tasks in sequence:

1. **Data Analysis & Suggestion Generation**: Analyzes support ticket data and generates actionable suggestions.
2. **Table Generation**: Creates informative tables summarizing key metrics.
3. **Chart Generation**: Produces visual representations of data trends.
4. **Final Report Assembly**: Compiles all analyses into a cohesive, professional markdown report.

## Features

- **Automated Data Analysis**: Analyzes support ticket data to identify patterns and trends
- **Visualized Insights**: Generates tables and charts to visualize key metrics
- **Actionable Suggestions**: Provides specific recommendations based on data analysis
- **Professional Reporting**: Compiles all information into a well-structured markdown report
- **Flexible Configuration**: Easily configurable through YAML files

## Project Structure

```
data_analysis_crew2/
├── data/                         # Contains CSV data files
│   └── support_tickets_data.csv  # Support ticket dataset
├── reports/                      # Generated reports and visualizations
├── src/
│   └── data_analysis_crew2/
│       ├── config/               # Configuration files
│       │   ├── agents.yaml       # Agent configurations
│       │   └── tasks.yaml        # Task configurations
│       ├── tools/                # Custom tools
│       │   ├── csv_read.py       # Tool for reading CSV data
│       │   └── custom_tool.py    # Template for custom tools
│       ├── crew.py               # Main crew setup
│       └── main.py               # Entry point for running the crew
└── tests/                        # Test files
```

## How It Works

This project leverages the CrewAI framework to create a team of specialized AI agents, each with specific roles:

1. **Suggestion Generation Agent**: Analyzes raw data and generates actionable recommendations.
2. **Reporting Agent**: Organizes data into tables and creates the final report.
3. **Chart Generation Agent**: Creates visual representations of data trends.

These agents work together through a series of sequential tasks, each building upon the previous one to create a comprehensive analysis.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- CrewAI 0.75.0 or higher


### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd data_analysis_crew2
   ```

2. Install dependencies:
   ```
   pip install -e .
   ```

3. Make sure you have an OpenAI API key in your `.env` file:
   ```
   OPENAI_API_KEY=your-api-key
   ```

### Running the Crew

Run the crew with:

```
python -m data_analysis_crew2.main
```

Or use the CrewAI CLI:

```
crewai run
```

The generated report will be saved to `reports/data_analysis_report.md`.

### Testing the Crew

You can test the crew with:

```
crewai test
```

## Viewing Reports

The crew generates professional markdown reports that can be viewed with:

- VS Code with Markdown Preview (Ctrl+Shift+V)
- Dedicated markdown viewers like Typora or Obsidian
- Any markdown-compatible viewer
