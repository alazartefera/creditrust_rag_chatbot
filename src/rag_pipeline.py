# src/rag_pipeline.py

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from transformers import pipeline

class ComplaintRAG:
    def __init__(self, embedding_model_name="all-MiniLM-L6-v2", persist_directory="vector_store"):
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.client = chromadb.Client(Settings(persist_directory=persist_directory))
        self.collection = self.client.get_collection("complaints")
        self.generator = pipeline("text-generation", model="gpt2")  # Replace with LLM of your choice

    def embed_query(self, question):
        return self.embedding_model.encode([question])[0]

    def retrieve_chunks(self, query, k=5):
        query_vector = self.embed_query(query)
        results = self.collection.query(query_embeddings=[query_vector], n_results=k)
        texts = results["documents"][0]
        sources = results["metadatas"][0]
        return texts, sources

    def format_prompt(self, context, question):
        return (
            "You are a financial analyst assistant for CrediTrust. "
            "Your task is to answer questions about customer complaints. "
            "Use the following retrieved complaint excerpts to formulate your answer. "
            "If the context doesn't contain the answer, say you don't have enough information.\n\n"
            f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )

    def generate_answer(self, question, k=5):
        chunks, sources = self.retrieve_chunks(question, k)
        context = "\n---\n".join(chunks)
        prompt = self.format_prompt(context, question)

        output = self.generator(prompt, max_length=200, do_sample=True, temperature=0.7)
        return output[0]["generated_text"].split("Answer:")[-1].strip(), chunks, sources
