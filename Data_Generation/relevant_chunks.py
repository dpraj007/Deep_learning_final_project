from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

from dotenv import load_dotenv
import os

load_dotenv()

api_openai = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = api_openai

def load_and_process_markdown(markdown_dir, index_name="markdown_index"):
    # Check if embeddings already exist
    if os.path.exists(f"{index_name}.faiss"):
        # Load existing index
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.load_local(index_name, embeddings)
        return vector_store
    
    # Load markdown files
    documents = []
    for filename in os.listdir(markdown_dir):
        if filename.endswith(".md"):
            file_path = os.path.join(markdown_dir, filename)
            loader = UnstructuredMarkdownLoader(file_path)
            documents.extend(loader.load())

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    # Create embeddings and vector store
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    # Save the index
    vector_store.save_local("vectorstores/"+ str(index_name))
    
    return vector_store

def search_documents(vector_store, query, k=3):
    # Perform similarity search
    relevant_chunks = vector_store.similarity_search(query, k=k)
    
    # Convert chunks to string and return
    return "".join([chunk.page_content for chunk in relevant_chunks])

# Example usage
# if __name__ == "__main__":
#     markdown_directory = "deprications/"
#     vector_store = load_and_process_markdown(markdown_directory,index_name="bokeh_changelog_deprecations_vector_store")
    
#     # Example query
#     query = "What is the main topic?"
#     results = search_documents(vector_store, query)
    
#     # Print results
#     print(results)
    # for i, doc in enumerate(results, 1):
    #     print(f"\nResult {i}:")
    #     print(doc.page_content)
