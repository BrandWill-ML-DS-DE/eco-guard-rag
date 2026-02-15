import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def process_document(uploaded_file, api_key):
    """Handles the heavy lifting of PDF ingestion and Vector DB creation."""
    try:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        loader = PyPDFLoader("temp.pdf")
        data = loader.load()
        
        # Senior move: Using recursive splitting for better semantic coherence
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200, 
            chunk_overlap=200,
            separators=["\n\n", "\n", ".", " "]
        )
        chunks = splitter.split_documents(data)
        
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=api_key
        )
        
        # Persist directory allows for faster reloading in production
        vector_db = Chroma.from_documents(
            documents=chunks, 
            embedding=embeddings,
            persist_directory="./chroma_db"
        )
        return vector_db
    except Exception as e:
        st.error(f"Error processing document: {e}")
        return None
