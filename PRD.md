# NetOps RAG Assistant - Product Requirement Document (PRD)

| **Project Name** | NetOps RAG Assistant (Claw2.2) |
| :--- | :--- |
| **Status** | MVP (v1.0) |
| **Target User** | Network Engineers, NOC Operators |
| **Owner** | Alan Stevrie Balantimuhe |

## 1. Problem Statement
Network Engineers sering kesulitan mencari command syntax yang spesifik (terutama RouterOS v7 vs v6 vs Cisco) dan troubleshooting guide yang tersebar di mana-mana. Mencari di Google seringkali memakan waktu dan berisiko mendapatkan informasi yang usang (hallucination).

## 2. Solution Overview
Sebuah **Local RAG (Retrieval-Augmented Generation) Chatbot** yang berjalan offline di laptop engineer. Sistem ini menggunakan LLM (Claw2.2) yang diperkaya dengan knowledge base terkurasi (Markdown docs) untuk memberikan jawaban teknis yang akurat, aman (data tidak keluar), dan berbahasa Indonesia.

## 3. User Personas
- **Junior Engineer:** Butuh panduan langkah-demi-langkah ("Gimana cara set OSPF?").
- **Senior Engineer:** Butuh validasi syntax cepat ("Command BGP v7 apa ya? Lupa gue.").
- **NOC Operator:** Butuh panduan troubleshooting saat insiden ("Link down, cek apa aja?").

## 4. MVP Features (v1.0)
- [x] **Local LLM Engine:** Ollama + Llama-3 (Claw2.2 Persona).
- [x] **RAG Pipeline:** LangChain + ChromaDB untuk indexing dokumen Markdown.
- [x] **Strict Context:** Jawaban hanya berdasarkan dokumen yang di-ingest (Anti-Hallucination).
- [x] **RouterOS v7 Support:** Knowledge base awal berisi cheat sheet Mikrotik v7.
- [x] **Dockerized:** Mudah dijalankan di environment apapun tanpa merusak host.

## 5. Non-Functional Requirements
- **Privacy:** 100% Offline (No Data Sent to Cloud).
- **Latency:** Jawaban harus muncul < 5 detik (tergantung hardware host).
- **Accuracy:** Zero hallucination for critical commands (e.g., destructive commands).

## 6. Future Roadmap
- [ ] **Multi-Vendor Support:** Tambah Cisco IOS, Juniper Junos, FRR.
- [ ] **Web UI:** Interface chat yang lebih ramah pengguna (Streamlit/Gradio).
- [ ] **Log Analysis Agent:** Input raw log -> Output Root Cause Analysis.
- [ ] **Config Generator Agent:** Input intent ("Buat VLAN 10-20") -> Output Script ready-to-paste.
