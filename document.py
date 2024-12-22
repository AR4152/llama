from typing import Iterator
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument
from docling.document_converter import DocumentConverter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tempfile import TemporaryDirectory
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os
import glob
from langchain_milvus import Milvus

class DoclingPDFLoader(BaseLoader):
    """
    Loader for extracting and converting PDF documents using Docling's DocumentConverter.

    Attributes:
        file_path (list[str] | str): Path(s) to the PDF files to load.
    """

    def __init__(self, file_path) -> None:
        self._file_paths = file_path if isinstance(file_path, list) else [file_path]
        self._converter = DocumentConverter()

    def lazy_load(self) -> Iterator[LCDocument]:
        for source in self._file_paths:
            dl_doc = self._converter.convert(source).document
            text = dl_doc.export_to_markdown()
            yield LCDocument(page_content=text)

def fetch_data_embeddings(folder_path: str):
    """
    Process documents from a folder, split their content, and create a Milvus-based retriever.

    Args:
        folder_path (str): Path to the folder containing documents.

    Returns:
        retriever: A retriever object for querying embedded document data.
    """
    files = glob.glob(os.path.join(folder_path, "*.pdf"))
    loader = DoclingPDFLoader(files)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    docs = loader.load()
    splits = text_splitter.split_documents(docs)
    HF_EMBED_MODEL_ID = "BAAI/bge-small-en-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name=HF_EMBED_MODEL_ID)
    MILVUS_URI = os.environ.get(
        "MILVUS_URI", f"{(tmp_dir := TemporaryDirectory()).name}/milvus_demo.db"
    )

    vectorstore = Milvus.from_documents(
        splits,
        embeddings,
        connection_args={"uri": MILVUS_URI},
        drop_old=True,
    )

    return vectorstore.as_retriever()