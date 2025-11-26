import gradio as gr

# TODO: implement
def generate_quiz_from_text(input: str, num_questions: int, question_types: list):
    return gr.Markdown(f"""
        # Generated Quiz ({num_questions} questions)
        TODO: implement
    """)
    
def render():
    with gr.Tab("Text (prompt)"):
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    label="Input Text",
                    placeholder="Enter a prompt",
                    lines=12
                )
                num_questions = gr.Slider(
                    minimum=3,
                    maximum=15,
                    value=5,
                    step=1,
                    label="Number of Questions"
                )
                question_types = gr.CheckboxGroup(["Multiple choice", "True/false", "Short answer", "Open-ended", "Fill in the blank"], label="Question types", show_select_all=True)

                generate_button = gr.Button("Generate", variant="primary")
            
            with gr.Column():
                text_output = gr.Markdown(label="Generated Quiz")
        
        generate_button.click(
            fn=generate_quiz_from_text,
            inputs=[text_input, num_questions,question_types],
            outputs=text_output
        )