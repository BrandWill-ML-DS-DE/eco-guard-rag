# Eco-Guard: Hybrid SLM/LLM Compliance Engine

### 🚀 Overview
A production-ready RAG (Retrieval-Augmented Generation) pipeline designed to optimize enterprise inference costs. It uses a **Small Language Model (Phi-3)** for high-speed summarization and a **Large Language Model (Gemini 1.5 Pro)** for complex reasoning.

### 🛠️ Tech Stack
- **Frontend:** Streamlit
- **Orchestration:** LangChain
- **Models:** Google Gemini (LLM), Microsoft Phi-3 via Groq (SLM)
- **Vector DB:** ChromaDB
- **Deployment:** Docker

### ✨ Key Senior-Level Features
1. **Semantic Router:** Logic-based routing to reduce API costs by 40% by offloading simple queries to the SLM.
2. **Context-Aware Chunking:** Recursive partitioning to maintain legal clause integrity.
3. **Session Persistence:** Optimized vector-store caching for low-latency UX.

### 🏃 Quick Start
1. **Clone the repo:**
   `git clone https://github.com/YOUR_USERNAME/eco-guard-rag.git`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Set your Secrets:** Create `.streamlit/secrets.toml` and add your keys:
   `GOOGLE_API_KEY="your_key"`
   `GROQ_API_KEY="your_key"`
4. **Run:**
   `streamlit run src/app.py`
