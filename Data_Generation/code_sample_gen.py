from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from typing import List
from dotenv import load_dotenv
import os
import glob
import csv

from relevant_chunks import *

load_dotenv()



api_gemini = os.environ.get('GEMNI_API_KEY')
from llm_request.gemini_request import get_gemini_response

code_sample_prompt_template = """ You are an expert programmer tasked with generating code based on a specific use case and library. Your goal is to provide complete, functional code that addresses the given requirements.

Here are the details for the code generation task:

<code_usecase>
{code_usecase}
</code_usecase>

<library>
{library}
</library>

Please generate code that fulfills the described use case using the specified library. Follow these steps and guidelines:

1. Analyze the requirements and plan your approach.
2. Determine all necessary imports and dependencies.
3. Write clear, efficient, and well-commented code.
4. Include error handling and follow best practices for the given library and use case.
5. Provide installation instructions for any required packages.

Your final output should be formatted as follows:

1. Installation instructions (if necessary)
2. Full code, including all imports and main implementation, formatted in a markdown code block
3. Brief explanation of the code and any important considerations

Begin your response with your thought process in <code_planning> tags, then proceed with the code generation.
"""

code_refine_prompt_template=''' You are an experienced software developer tasked with refining and updating a piece of code. Your goal is to improve the code by referencing specific library documentation and considering relevant deprecation notices and changes.

Here is the code you need to refine:
<code_to_refine>
{code}
</code_to_refine>

The library in the context is:
<library>
{library}
</library>

Consider the following deprecation references:
<deprecation_references>
{deprecation_references}
</deprecation_references>

Also, take into account these relevant changes:
<change_references>
{changes_references}
</change_references>

Instructions:
1. Carefully review the provided code.
2. Consult the library documentation for best practices and up-to-date methods.
3. Check the deprecation references to identify if any deprecated features or functions used in the code.
4. Review the relevant changes to understand any updates or new features that could be applied.
5. Identify areas in the code that can be refined or improved based on steps 2-4.
6. Apply the necessary refinements to the code.
7. Verify that the refined code maintains its original functionality while incorporating the improvements.

Output Format:
After your analysis, provide the refined code.
'''

def depricated_chunks(query):
    deprecation_directory = "deprications/"
    vector_store = load_and_process_markdown(deprecation_directory,index_name="bokeh_changelog_deprecations_vector_store")
    results = search_documents(vector_store=vector_store, query=query)
    return results

def summarized_chunks(query):
    deprecation_directory = "summarized/"
    vector_store = load_and_process_markdown(deprecation_directory,index_name="bokeh_changelog_summarized_vector_store")
    results = search_documents(vector_store=vector_store, query=query)
    return results

def knowledgebase_chunks(query):
    deprecation_directory = "knowledgebase/"
    vector_store = load_and_process_markdown(deprecation_directory,index_name="bokeh_changelog_knowledgebase_vector_store")
    results = search_documents(vector_store=vector_store, query=query)
    return results

import json

def generate_code_sample(library, usecase_list):
    
    print(f"Generating code samples for {library} library")

    code_samples = []

    for use_case in usecase_list:
        k_chunks=""
        d_chunks=""
        print(f"Generating code for use case: {use_case}")
        prompt1= code_sample_prompt_template.format(library=library,code_usecase=use_case)
        try:
            response = get_gemini_response(prompt1, api_gemini, model_name="gemini-2.0-flash-exp")
            truncated_response = response[:100] + "..."
            print(truncated_response)
        except Exception as e:
            raise Exception(f"Error generating use cases: {str(e)}")
        
        if response:
            k_chunks = knowledgebase_chunks(response)
            print(k_chunks[:100]+"...")
            d_chunks = depricated_chunks(response)
            print(d_chunks[:100]+"...")

            prompt2=code_refine_prompt_template.format(code=response,library=library,deprecation_references=d_chunks,changes_references=k_chunks)
            try:
                response2 = get_gemini_response(prompt2, api_gemini, model_name="gemini-2.0-flash-exp")
                truncated_response2 = response2[:100] + "..."
                print(truncated_response2)
            except Exception as e:
                raise Exception(f"Error generating use cases: {str(e)}")

            code_samples.append({
                'usecase': use_case,
                'response1': response,
                'response2': response2,
                'knowledgebase_chunks': k_chunks,
                'depricated_chunks': d_chunks
            })

            # Save the data intermittently
            with open('code_samples/generated_code_sample_data.json', 'w') as file:
                json.dump(code_samples, file, indent=2)









if __name__ == "__main__":
    usecase_list=[
      "Build a system that allows to visualize and analyse data with custom callbacks and interactions.",
      "Develop a tool to visualize and compare different algorithms with customizable parameters.",
     "Create an interactive tool to visualizes data on a timeline with zooming and filtering options.",
      "Build a platform that allows to create dashboards with custom layouts and responsive design.",
     "Develop a system that can serve different types of data from different sources with interactive visualisations.",
    "Create an interactive interface to visualise data in a table format with filtering and sorting.",
    "Build an interactive tool that visualizes complex data structures using network graphs.",
    "Develop a system to visualize the relationships between different entities using graphs.",
      "Create a platform for creating custom charts and interactive visualizations for use in reports.",
       "Build an interactive tool for visualizing complex multi-dimensional datasets.",
        "Create a system to create and visualize animated time series.",
        "Build a tool to compare different algorithms side by side with interactive plots.",
         "Create an interface to visualise financial data using candlestick charts and other options.",
         "Build an interactive tool to visualize user activity in different apps using heat maps and charts.",
        "Create an interface that allows to embed interactive plots into websites.",
        "Build a system to create custom dashboards with different visualizations and interactions.",
        "Create an interface to create and customize different types of maps with custom data layers.",
        "Build a tool to create reports with interactive visualizations and summaries of data.",
         "Create a system that allows to visualize and compare datasets using different visual encodings.",
        "Create an interactive visualization tool for educational content.",
        "Build an interactive tool to visualize network traffic and infrastructure.",
        "Create a system to create and visualize data of different scientific experiments.",
        "Build an interactive platform to visualize and manage project timelines with Gantt charts.",
        "Create a platform to visualize and analyze medical data with interactive charts and analysis tools.",
        "Build a system that allows to create custom visualisations using data transformations.",
        "Create a tool to create animated interactive visualizations for presentations and reports.",
        "Build a system to visualize and compare the performance of different software versions using interactive dashboards.",
        "Create a platform to visualise user behavior across different websites with interactive charts.",
        "Build an interactive tool to manage and visualise student attendance and grades.",
         "Create a tool to visualise user feedback and reviews using sentiment analysis.",
        "Build an interactive system for visualising the process of creating and maintaining complex systems.",
         "Create a platform that visualizes the flow of information across social media platforms.",
        "Build a system that allows to visualise and manage different types of online data and activity.",
        "Create an interface that allows to visualize and analyse data in real time with updates and alerts.",
        "Build a tool that allows to compare and visualize performance of different types of investments over time.",
        "Create a system to visualize different aspects of business operations and performance.",
        "Build a tool for collaborative data visualization with different users.",
        "Create a platform for visualizing and analyzing data of public infrastructure and services."
    ]
    library_name = "Bokeh- Visualization"
    generate_code_sample(library=library_name, usecase_list=usecase_list)