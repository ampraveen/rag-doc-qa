AI-Powered Document Question Answering
System
Project Overview
This project implements an AI-powered document question-answering system using
Retrieval-Augmented Generation (RAG). Users can upload enterprise documents and ask natural
language questions. The system retrieves relevant document content and generates accurate,
context-aware answers using a Large Language Model.
Objectives
• Process and manage unstructured documents
• Generate embeddings and store them in a vector database
• Retrieve relevant content using similarity search
• Generate grounded answers using a Groq LLM
• Provide source references for validation
Technology Stack
• Programming Language: Python
• UI Framework: Streamlit
• LLM Provider: Groq (LLaMA 3.1)
• Vector Database: ChromaDB
• Embedding Model: Sentence Transformers
• IDE: Visual Studio Code
System Architecture
Uploaded documents are processed and split into chunks. Each chunk is converted into vector
embeddings and stored in a vector database. User queries are embedded using the same model
and matched against stored vectors. Retrieved context is passed to the Groq LLM to generate
accurate responses.
Testing & Results
The system was tested with multiple document formats such as PDF, TXT, and CSV. Queries
related to document summaries and specific information returned accurate answers with
appropriate source references.
Limitations
• Accuracy depends on document quality and chunking strategy
• Large documents may require optimized chunk sizes
• Responses are limited to retrieved context
Conclusion
This project successfully demonstrates a complete RAG workflow for document-based question
answering. It showcases practical integration of embeddings, vector databases, and large language
models in a real-world application.
<img width="858" height="858" alt="image" src="https://github.com/user-attachments/assets/0af01ba6-519d-4466-bb20-12529740b1ba" />


