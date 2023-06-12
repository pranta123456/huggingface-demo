from transformers import pipeline
import gradio as gr 

model = pipeline("summarization")

def predict(promt):
    summary = model(promt)[0]["summary_text"]
    return summary 

with gr.Blocks() as demo:
    input_sent = gr.Textbox(label="Input text")
    output = gr.Textbox(label="text")
    summ_btn = gr.Button("Summarize")
    summ_btn.click(fn=predict, inputs=input_sent, outputs=output)

demo.launch(share=True)