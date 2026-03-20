from app.rag.loader import load_documents
from app.rag.chunker import split_documents
from app.rag.embedder import create_vectorstore
from app.rag.retriever import load_retriever

files = [
    "data/sample1.pdf",
    "data/sample2.pdf"
]

docs = load_documents(files)
chunks = split_documents(docs)

create_vectorstore(chunks)

retriever = load_retriever()

results = retriever.invoke(
    "termination clause"
)
print("Retrieved:", len(results))