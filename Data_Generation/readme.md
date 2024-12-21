## Improving LLM's performance on Niche Libraries by finetuning and unlearning on LLM's using synthetic data.

Steps to run the code

pip install -r requirements.txt

Currently the repo is work in progress

The individual files as part of the bigger pipeline to create synthetic data on niche libraries (ex bokeh here)

changelog_explainer.py  - to explain every change with examples to save as knowledgebase.

code_sample_gen.py- generated code sample for respective usecase

deprication.py- finds all the changes of deprreiction of code.

relevant_chunks.py- finds all the relevant chunks of changes in the knowledge base

summarize.py- sumarizes all the chage logs

use_case_gen.py - generateed usecases based on the knowledge base.