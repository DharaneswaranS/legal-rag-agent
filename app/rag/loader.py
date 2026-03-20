from langchain_community.document_loaders import PyPDFLoader

def load_documents(file_paths):
    documents = []

    for path in file_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        documents.extend(docs)

    return documents