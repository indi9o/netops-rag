# Changelog

All notable changes to the **NetOps RAG (Claw2.2)** project will be documented here.

## [v1.0.0] - 2026-02-16 (Initial Release)

### 🚀 Features
- **Strict RAG Engine:** Answers only based on provided context (Markdown/Text).
- **Anti-Hallucination:** Prevents making up commands (e.g., `ip ospf mtu-ignore`).
- **Indonesian Persona:** Claw2.2 responds in casual Bahasa Indonesia ("Bos", "Gan").
- **RouterOS v7 Awareness:** Correct syntax for OSPF (`/routing ospf instance`) & BGP (`/routing bgp connection`).

### 🛠️ Changes
- Created Docker environment with Python 3.12, LangChain, ChromaDB.
- Implemented `ingest.py` for document parsing & vectorization.
- Implemented `chat_rag.py` for retrieval & generation.
- Added `routeros-v7-cheatsheet.md` as initial knowledge base.
- Tuned `PROMPT_TEMPLATE` to prevent hallucination (Strict Mode).
- Tuned retrieval `k=5` for better context gathering.

### 🐛 Fixes
- Fixed MTU configuration hallucination (`/system mtu set` -> `/interface ethernet set`).
- Fixed BGP command syntax for RouterOS v7 (`bgp peer` -> `bgp connection`).
- Fixed dependency conflict in `requirements.txt`.
