# Flet App AI Assistant

This is a simple AI Assistant application built using the [Flet](https://flet.dev/) framework for Python. The application provides a chat interface where users can interact with an AI model through a custom API. The application handles user input and displays the AI's responses in a dynamic and animated way.

## Features

- A user-friendly chat interface designed with Flet components.
- Dynamic message display with animated typing effects.
- Interacts with a custom AI API to process user input and provide responses.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.8 or higher
- Pip (Python package installer)

## Installation

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that your custom AI API is running and accessible. The current setup assumes that your API is available at `http://dockerhelper.ir:8000/api/chat/`. If your API is hosted elsewhere, you may need to adjust the `api_url` in the `Prompt` class accordingly.

## Usage

To run the application, execute the following command:

```bash
python main.py
