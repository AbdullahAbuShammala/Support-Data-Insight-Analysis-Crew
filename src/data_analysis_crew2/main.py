#!/usr/bin/env python
import sys
import os
from data_analysis_crew2.crew import DataAnalysisCrew2Crew
from crewai import LLM

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.

def run():
    """
    Run the crew.
    """
    result = DataAnalysisCrew2Crew().crew().kickoff()
    
    # Save the report to a markdown file
    os.makedirs('reports', exist_ok=True)
    with open('reports/data_analysis_report.md', 'w') as f:
        f.write(result.raw)
    
    print(f"Report saved to reports/data_analysis_report.md")
    return result


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        filename = sys.argv[2] if len(sys.argv) > 2 else 'training.pkl'
        DataAnalysisCrew2Crew().crew().train(n_iterations=iterations, filename=filename)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DataAnalysisCrew2Crew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    try:
        iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 1
        model_name = sys.argv[2] if len(sys.argv) > 2 else 'gpt-4o'
        # Create an LLM instance for evaluation
        eval_llm = LLM(model=model_name)
        result = DataAnalysisCrew2Crew().crew().test(n_iterations=iterations, eval_llm=eval_llm)
        
        # Save the test report to a markdown file
        os.makedirs('reports', exist_ok=True)
        with open('reports/data_analysis_test_report.md', 'w') as f:
            f.write(result.raw)
        
        print(f"Test report saved to reports/data_analysis_test_report.md")
        return result

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
