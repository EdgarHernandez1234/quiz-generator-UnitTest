import gradio as gr

import pages.main_page as main_page, pages.second_page as second_page

def shared_navbar():
    return gr.Navbar(
        visible=True,
        main_page_name="Home",
        value=[("GitHub", "https://github.com/ftrbnd/quiz-generator")]
    )

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    navbar = shared_navbar()
    main_page.demo.render()

with demo.route("Second Page"):
    navbar = shared_navbar()
    second_page.demo.render()

if __name__ == "__main__":
    demo.launch()