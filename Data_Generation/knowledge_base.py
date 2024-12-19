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
You are an expert software developer tasked with explaining changes in a library's changelog. Your goal is to provide clear, detailed explanations that even junior developers can understand.

Here's the name of the library:
<library_name>
{library_name}
</library_name>

And here's the changelog:
<changelog>
{logs}
</changelog>

Your task is to explain each change in the changelog in detail, provide code examples, and present the information in the simplest form possible. 

For each change in the changelog, follow these steps:

1. Break down the change in <change_breakdown> tags. In this breakdown:
   - Quote the exact change from the changelog
   - Identify the type of change (e.g., new feature, bug fix, deprecation)
   - Categorize the change (major, minor, patch) based on semantic versioning principles
   - List potential impacts on existing code
   - Consider backward compatibility issues
   - Brainstorm simple explanations
   - Outline potential code examples
   - Write a one-sentence summary of the change for quick reference
   - Use this checklist to ensure you don't miss anything:
     [ ] Change quoted
     [ ] Change type identified
     [ ] Change categorized
     [ ] Impacts listed
     [ ] Backward compatibility considered
     [ ] Simple explanations brainstormed
     [ ] Code examples outlined
     [ ] One-sentence summary written

2. After your breakdown, provide your explanation in the following format:

   <change_number>X</change_number>
   <change_description>
   [Provide a clear, simple explanation of the change]
   </change_description>
   
   <code_example>
   [Provide one or more relevant code examples]
   </code_example>
   
   <simple_explanation>
   [Explain the change and its implications in the simplest terms possible]
   </simple_explanation>

Repeat this process for each change in the changelog. Ensure that you don't miss any changes and that each explanation is thorough and easy to understand.

Remember, your goal is to help developers quickly grasp what has changed and how it might affect their code.
"""

def generate_knowledgebase(library_name,change_log_dir="changelogs_by_year", save_logs_dir="knowledgebase/", filename="bokeh_knowledgebase"):
    # Create the save directory if it doesn't exist
    os.makedirs(save_logs_dir, exist_ok=True)

    # Get all log files in the changelog directory
    log_files = glob.glob(os.path.join(change_log_dir, "*.txt"))

    # Initialize an empty string to store the knowledge base
    knowledge_base = ""

    for log_file in log_files:
        # print(log_file)
        with open(log_file, "r") as f:
            logs = f.read()

        prompt = prompt_template.format(logs=logs, library_name=library_name)
        try:
            response = get_gemini_response(prompt, api_gemini,model_name="gemini-exp-1206")
            # print(response[:200])
            knowledge_base += response + "\n\n"  # Append the response to the knowledge base
        except Exception as e:
            raise Exception(f"Error generating report for {log_file}: {str(e)}")

    # Save the knowledge base to a file
    knowledge_base_file = os.path.join(save_logs_dir, f"{filename}.md")
    with open(knowledge_base_file, "w") as f:
        f.write(knowledge_base)

    return knowledge_base_file



# if __name__ == "__main__":
#     library_name = "Bokeh- Visualization"
#     generate_knowledgebase(library_name)