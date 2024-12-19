from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from dotenv import load_dotenv
import os
import glob

load_dotenv()

api_gemini = os.environ.get('GEMNI_API_KEY')
from llm_request.gemini_request import get_gemini_response

prompt_template = """You are a skilled software developer tasked with analyzing logs for code deprecations in a specific library. Your goal is to identify and report on all instances of deprecated code found in the logs.

Here's the name of the library you'll be analyzing:
<library_name>
{library_name}
</library_name>

And here are the logs you need to analyze:
<logs>
{logs}
</logs>

Please follow these steps to complete your task:

1. Carefully read through the logs for the {library_name} library.
2. Identify all instances of code deprecation mentioned in the logs.
3. For each deprecation, provide:
   - A brief explanation of what has been deprecated
   - Generate an example with a real world use case of the deprecated code (IMPORTANT: Only include code that is actually deprecated)

After your analysis, provide a structured report of the deprecations you've found. Use the following format for each deprecation:

1. Deprecation: [Brief description of what was deprecated]
   Example:
   Usecase : **one line description of the deprecated code example**
   ```
   [Include ONLY the deprecated code here]
   ```
   

Repeat this format for each deprecation you find.

Remember: Only include examples of code that is explicitly stated as deprecated in the logs. Do not speculate or include code that isn't clearly marked as deprecated.

Please proceed with your analysis and report of the deprecations in the {library_name} library logs.
"""

def generate_deprication_knowledgebase(library_name, change_log_dir="changelogs_by_year", save_logs_dir="deprications/", filename="deprications"):
    # Create the save directory if it doesn't exist
    os.makedirs(save_logs_dir, exist_ok=True)

    # Get all log files in the changelog directory
    log_files = glob.glob(os.path.join(change_log_dir, "*.txt"))

    # Initialize an empty string to store the deprications
    deprications_file = os.path.join(save_logs_dir, f"{filename}.md")
    with open(deprications_file, "w") as f:
        for log_file in log_files:
            # print(f"Processing log file: {log_file}")
            with open(log_file, "r") as log:
                logs = log.read()
            prompt = prompt_template.format(logs=logs, library_name=library_name)
            try:
                response = get_gemini_response(prompt, api_gemini, model_name="gemini-2.0-flash-exp")
                # print(f"Truncated response: {response[:200]}")
                f.write(response)
            except Exception as e:
                raise Exception(f"Error generating report for {log_file}: {str(e)}")

    return deprications_file



# if __name__ == "__main__":
#     library_name = "Bokeh- Visualization"
#     print(generate_deprication_knowledgebase(library_name))