import gradio as gr

def generate_questions(value):
    print("Received file!", type(value))
    return value

def file_input():
    return gr.File(file_types=[".txt"],label="Upload a .txt file")

def textbox_output():
    return gr.Textbox(label="Generated Questions")

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            file_input = gr.File(file_types=[".txt"], label="Upload a .txt file")
            submit_btn = gr.Button("Generate Questions", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(label="Generated Questions")
    
    submit_btn.click(fn=generate_questions, inputs=file_input, outputs=output)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
