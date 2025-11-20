import gradio as gr

def generate_questions(value):
    print("Received file!", type(value))
    return value

def file_input():
    return gr.File(file_types=[".txt"],label="Upload a .txt file")

def textbox_output():
    return gr.Textbox(label="Generated Questions")

with gr.Blocks() as demo:
    f = gr.Interface(fn=generate_questions, inputs=[file_input()], outputs=[textbox_output()], flagging_mode="never")

if __name__ == "__main__":
    demo.launch()
