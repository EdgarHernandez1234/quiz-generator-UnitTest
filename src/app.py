import gradio as gr

import inputs.text_tab as text_tab, inputs.file_tab as file_tab

with gr.Blocks(title="Automatic Quiz Generator") as demo:
    gr.Markdown("""
        # COMP 582 - Automatic Quiz Generator
        ### Select your input method by selecting a tab
    """)
    
    with gr.Tabs():
        text_tab.render()
        file_tab.render()

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())