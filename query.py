# MLHub toolkit for llama - query
# ml query llama

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

import os
from langchain_ollama import OllamaLLM
from typing import Iterable

from langchain_core.documents import Document as LCDocument
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from document import fetch_data_embeddings

# -----------------------------------------------------------------------
# Command line argument and options
# -----------------------------------------------------------------------

def cli(query: str):
    """
    Simple `hello world` string output.
    """

    health_data_folder_path = get_health_data_folder_path()
    retriever = fetch_data_embeddings(health_data_folder_path)
    prompt = PromptTemplate.from_template(
        "Context information is below.\n---------------------\n{context}\n---------------------\nGiven the context information and not prior knowledge, answer the query.\nQuery: {question}\nAnswer:\n"
    )

    llm = OllamaLLM(model="smollm")
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    print(rag_chain.invoke(query))

# -----------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------

def format_docs(docs: Iterable[LCDocument]):
    return "\n\n".join(doc.page_content for doc in docs)

def get_health_data_folder_path():
    folder_path = os.getenv('MLHUB_LLAMA_HEALTH_DATA')

    if folder_path is None:
        print("Error: The environment variable 'MLHUB_LLAMA_HEALTH_DATA' is not set.")
        raise

    if not os.path.isdir(folder_path):
        print(f"Error: The path '{folder_path}' is not a valid directory.")
        raise

    return folder_path
    
if __name__ == "__main__":
    cli()