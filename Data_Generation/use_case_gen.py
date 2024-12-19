from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from dotenv import load_dotenv
import os
import glob

load_dotenv()

api_gemini = os.environ.get('GEMNI_API_KEY')
from llm_request.gemini_request import get_gemini_response

usecase_prompt_template = """ You are a software developer and creative thinker tasked with generating potential use cases for a library based on its changelog. Your goal is to come up with a wide range of innovative and practical applications for this library.

Here is the summarized changelog:
<summarized_logs>
{summarized_logs}
</summarized_logs>

Here is the name of the library:
<library_name>
{library_name}
</library_name>

Your task is to generate a list of {number_of_usecases} ideas for use cases that can be further used to generate code for this library. Please follow these steps:

1. Analyze the changelog to understand the library's features, updates, and capabilities.
2. Brainstorm potential use cases across various industries and scenarios.
3. Generate {number_of_usecases} unique and diverse use case ideas.
4. Format the ideas as a list of strings in a JSON array.

Before providing the final list, wrap your thought process and initial brainstorming inside <analysis_and_brainstorming> tags. This will help ensure a thorough and creative approach to generating use cases. It's okay for this section to be quite long, as we want a comprehensive analysis and brainstorming process. 

Your final output should be a well-structured JSON array containing {number_of_usecases} strings, each representing a unique use case idea. Ensure that the ideas are diverse and cover a wide range of potential applications. Make sure every idea is well explained.

Example output format:
```json
[
  "Use case idea 1",
  "Use case idea 2",
  "Use case idea 3",
  ...
  "Use case idea {number_of_usecases}"
]
```

Please proceed with your analysis and generation of use case ideas. Every use case or ideas should be to utilize the above library and easy to code.

"""

def generate_usecases(library_name, change_log_summary_dir="summarized/bokeh_summarized.md", save_logs_dir="usecases/", filename="bokeh_usescases",number_of_usecases=10):
    # Create the save directory if it doesn't exist
    os.makedirs(save_logs_dir, exist_ok=True)

    # Read the changelog summary file
    with open(change_log_summary_dir, "r") as f:
        summarized_logs = f.read()

    prompt = usecase_prompt_template.format(summarized_logs=summarized_logs, library_name=library_name,number_of_usecases=number_of_usecases)
    try:
        response = get_gemini_response(prompt, api_gemini, model_name="gemini-2.0-flash-exp")
        file = os.path.join(save_logs_dir, f"{filename}.md")
        with open(file, "w") as f:
            f.write(response)
        return file
    except Exception as e:
        raise Exception(f"Error generating use cases: {str(e)}")



if __name__ == "__main__":
    library_name = "Bokeh- Visualization"
    print(generate_usecases(library_name,change_log_summary_dir="summarized/bokeh_summarized.md",filename="bokeh_usecases",number_of_usecases=300))