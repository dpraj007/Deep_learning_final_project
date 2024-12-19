import os
from langchain_community.document_loaders import DirectoryLoader
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.testset import TestsetGenerator
from dotenv import load_dotenv
import os

load_dotenv()

def generate_q_a(path, output_filename, num_qa_pairs):
    # Load documents
    loader = DirectoryLoader(path, glob="**/*.md")
    docs = loader.load()

    # Set OpenAI API key
    api_openai = os.environ.get('OPENAI_API_KEY')
    os.environ["OPENAI_API_KEY"] = api_openai

    # Initialize LLM and embeddings
    generator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
    generator_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings())

    # Generate test set
    generator = TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)
    dataset = generator.generate_with_langchain_docs(docs, testset_size=num_qa_pairs)

    # Save dataset
    output_folder = "qa_pairs_dataset"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_path = os.path.join(output_folder, output_filename)
    dataset.to_csv(output_path)

    return output_path





if __name__ == "__main__":
    
    # Set the path to the directory containing your documents
    path = "summarized"

    filename = "100_qa_on_summary_bokeh.csv"

    # Set the number of QA pairs to generate
    num_qa_pairs = 1000

    # Call the generate_q_a function
    output_path = generate_q_a(path, filename, num_qa_pairs)

    print(f"QA pairs saved to: {output_path}")

