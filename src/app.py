# app.py

import gradio as gr
import sys
sys.path.append("../src")

from rag_pipeline import ComplaintRAG

rag = ComplaintRAG()

def chatbot_interface(question):
    answer, chunks, sources = rag.generate_answer(question)
    formatted_sources = "\n\n---\n\n".join(chunks)
    return answer, formatted_sources

# Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 CrediTrust Complaint Chatbot\nAsk a question about customer complaints")

    with gr.Row():
        question = gr.Textbox(label="Your Question", placeholder="e.g. Why are people unhappy with BNPL?")
    with gr.Row():
        answer = gr.Textbox(label="Generated Answer", lines=4)
    with gr.Row():
        sources = gr.Textbox(label="Source Complaint Chunks", lines=10)

    submit = gr.Button("Submit")
    submit.click(fn=chatbot_interface, inputs=question, outputs=[answer, sources])

    gr.Markdown("Click 'Submit' to get an AI-generated answer with sources.")

# Launch app
if __name__ == "__main__":
    demo.launch()
