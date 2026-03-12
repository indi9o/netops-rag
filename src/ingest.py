import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Config
DATA_PATH = "data/"
DB_PATH = "chroma_db/"
# Pake embedding model 'nomic-embed-text' (kalau ada) atau 'llama3' aja cukup
EMBEDDING_MODEL = "llama3"

def main():
    print("🚀 Starting Knowledge Ingestion...")
    
    # 1. Load Documents
    loader = DirectoryLoader(DATA_PATH, glob="*.md", loader_cls=TextLoader)
    documents = loader.load()
    print(f"📄 Loaded {len(documents)} documents.")

    # 2. Split Text (Chunking)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"🔪 Split into {len(chunks)} chunks.")

    # 3. Save to Vector DB (Chroma)
    print("💾 Saving to ChromaDB (This might take a while)...")
    # PENTING: base_url arahin ke host.docker.internal buat akses Ollama di host
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL, base_url="http://host.docker.internal:11434")
    
    Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings,
        persist_directory=DB_PATH
    )
    print("✅ Ingestion Complete! Brain is ready.")

if __name__ == "__main__":
    main()
