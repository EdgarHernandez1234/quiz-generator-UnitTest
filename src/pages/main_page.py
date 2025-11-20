import gradio as gr

with gr.Blocks() as demo:
    t = gr.Textbox()
    demo.load(lambda: 'Hi', None, t)

if __name__ == "__main__":
    demo.launch()