import streamlit as st
import os
from src.loader import load_document
from src.chunker import chunk_text
from src.embeddings import embed_text
from src.vector_store import store_embeddings
from src.rag_pipeline import generate_answer

st.set_page_config(page_title="AI Document Q&A")

st.title("📄 AI Document Question Answering System")

uploaded_files = st.file_uploader(
    "Upload Documents (PDF, TXT, CSV)",
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        path = os.path.join("data", file.name)
        with open(path, "wb") as f:
            f.write(file.read())

        text = load_document(path)
        chunks = chunk_text(text)
        embeddings = embed_text(chunks)
        metadata = [{"source": file.name}] * len(chunks)

        store_embeddings(chunks, embeddings, metadata)

    st.success("Documents processed successfully!")

question = st.text_input("Ask your question")

if question:
    answer, sources = generate_answer(question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Source Documents")
    for s in sources:
        st.write(s["source"])
