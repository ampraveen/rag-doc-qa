import os
from dotenv import load_dotenv
from groq import Groq

from src.embeddings import embed_text
from src.vector_store import search

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client using API key from environment
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(question: str):
    """
    Generates a context-aware answer using RAG (Retrieval-Augmented Generation)
    """

    # Step 1: Convert question to embedding
    query_embedding = embed_text([question])[0]

    # Step 2: Retrieve relevant document chunks
    results = search(query_embedding)

    # Step 3: Combine retrieved chunks into context
    context = "\n".join(results["documents"][0])

    # Step 4: Construct prompt
    prompt = f"""
You are an AI assistant. Answer the question ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    # Step 5: Call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Step 6: Return answer and source metadata
    answer = response.choices[0].message.content
    sources = results["metadatas"][0]

    return answer, sources
