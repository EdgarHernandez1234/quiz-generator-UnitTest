
ifeq ($(OS),Windows_NT)
run:
	@echo Run 'gradio src/app.py' to start the application
	@cmd /K ".\gradio-env\Scripts\activate.bat"
else
run:
	@echo Run 'gradio src/app.py' to start the application
	@cd . && bash -c "source gradio-env/bin/activate && exec bash"
endif