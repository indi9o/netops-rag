import argparse
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Config
DB_PATH = "chroma_db/"
MODEL_NAME = "claw2.2"  # Pakai Claw 2.2 yang kita buat!
EMBEDDING_MODEL = "llama3"

PROMPT_TEMPLATE = """
Kamu adalah asisten NetOps RAG yang sangat patuh pada konteks.
Jawablah pertanyaan HANYA berdasarkan context berikut.

ATURAN KERAS:
1. JANGAN gunakan pengetahuan dari luar context ini!
2. JANGAN halusinasi command yang tidak ada di text.
3. Jika jawaban tidak ada di context, KATAKAN: "Maaf Bos, info itu gak ada di kitab suci saya. Coba update knowledge base dulu."

Context:
{context}

---

Pertanyaan: {question}
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Pertanyaan buat Claw RAG")
    args = parser.parse_args()
    
    # 1. Load DB (Otak Cadangan)
    print("🧠 Loading Knowledge Base...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL, base_url="http://host.docker.internal:11434")
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    
    # 2. Search (Cari Jawaban Relevan)
    # Naikin k=5 biar konteks lebih luas (termasuk bagian bawah file)
    results = db.similarity_search_with_score(args.query, k=5)
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # 3. Generate Answer (Claw Jawab)
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    model = ChatOllama(model=MODEL_NAME, base_url="http://host.docker.internal:11434")
    
    print(f"\n🤖 Claw2.2 Menjawab ({len(results)} context found):\n")
    chain = prompt | model
    response = chain.invoke({"context": context_text, "question": args.query})
    
    print(response.content)

if __name__ == "__main__":
    main()
