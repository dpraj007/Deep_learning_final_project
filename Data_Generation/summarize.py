from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from dotenv import load_dotenv
import os
import glob

load_dotenv()

api_gemini = os.environ.get('GEMNI_API_KEY')
from llm_request.gemini_request import get_gemini_response

prompt_template = """
You are a skilled software developer tasked with summarizing the changelog of a library. Your goal is to provide a clear and concise overview of the changes leading up to the latest version, highlighting the most important updates and providing code examples for the final version.

Here is the full changelog:
<changelog>
{logs}
</changelog>

And here is the name of the library:
<library_name>
{library_name}
</library_name>

Please follow these steps to create your summary:

1. Analyze the changelog:
   - Identify the latest version number
   - Note the key changes and features added throughout the versions
   - Pay special attention to breaking changes or significant updates

2. Summarize the changes:
   - Provide an overview of the library's evolution
   - Highlight the most important updates
   - Focus on changes that are likely to impact users of the library

3. Provide code examples:
   - For the latest version, include 1-3 code snippets that demonstrate new or changed functionality
   - Ensure the examples are clear and concise

4. Format your response as follows:
   a) Summary of Changes
   b) Key Updates
   c) Code Examples (for the latest version)

Before writing your final response, wrap your analysis in <changelog_analysis> tags to organize your thoughts and identify the most important information from the changelog. In this analysis:

1. List all versions chronologically, with their key changes.
2. For each version, quote the most significant updates directly from the changelog.
3. Highlight any breaking changes or deprecations.
4. Identify the latest version and its most important features.

Your final output should be informative, concise, and useful for developers who need to quickly understand what's new in the library.
"""

def generate_summary(library_name,change_log_dir="changelogs_by_year", save_logs_dir="summarized/", filename="bokeh_summarized"):
    # Create the save directory if it doesn't exist
    os.makedirs(save_logs_dir, exist_ok=True)

    # Get all log files in the changelog directory
    log_files = glob.glob(os.path.join(change_log_dir, "*.txt"))

    # Initialize an empty string to store the knowledge base
    logs = ""
    for log_file in log_files:
        # print(log_file)
        with open(log_file, "r") as f:
            logs += f.read() + "\n"

    prompt = prompt_template.format(logs=logs, library_name=library_name)
    try:
        response = get_gemini_response(prompt, api_gemini,model_name="gemini-exp-1206")
        # print(response[:200])
    except Exception as e:
        raise Exception(f"Error generating report: {str(e)}")

    # Save the knowledge base to a file
    summary_file = os.path.join(save_logs_dir, f"{filename}.md")
    with open(summary_file, "w") as f:
        f.write(response)

    return summary_file



# if __name__ == "__main__":
#     library_name = "Bokeh- Visualization"
#     generate_summary(library_name)