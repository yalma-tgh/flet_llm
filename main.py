import flet as ft
import time
import requests


def main_style():
    return {
        "width": 420,
        "height": 500,
        "bgcolor": "#141518",
        "border_radius": 10,
        "padding": 15,
    }

def prompt_style():
    return {
        "width": 420,
        "height": 40,
        "border_color": "white",
        "content_padding": 10,
        "cursor_color": "white",
    }

class MainContentArea(ft.Container):
    def __init__(self):
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True,
        )
        self.content = self.chat

class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str) -> None:
        self.name = name
        self.message = message
        self.text = ft.Text(self.message)
        super().__init__(spacing=4)
        self.controls.extend([ft.Text(self.name, opacity=0.6), self.text])

class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView):
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        self.chat = chat

    def animate_text_output(self, name: str, prompt: str):
        word_list: list = []
        msg = CreateMessage(name, "")
        self.chat.controls.append(msg)

        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)

    def user_output(self, prompt):
        self.animate_text_output(name="Me", prompt=prompt)

    def ai_output(self, prompt):
        # Define the URL of your Django API
        api_url = "http://dockerhelper.ir:8000/api/chat/"
        
        try:
            response = requests.post(api_url, json={"message": prompt})
            
            if response.status_code == 200:
                response_data = response.json()
                response_text = response_data.get('response', '').strip()
            else:
                response_text = "Error: Unable to get a response from the API."
            
        except requests.exceptions.RequestException as e:
            response_text = f"Error: {str(e)}"
        
        self.animate_text_output(name="Custom API", prompt=response_text)

    def run_prompt(self, event):
        text = event.control.value
        self.value = ""
        self.update()
        self.user_output(prompt=text)
        self.ai_output(prompt=text)

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "dark"

    main = MainContentArea()
    prompt = Prompt(chat=main.chat)

    page.add(
        ft.Text("Flet App AI Assistant", size=28, weight="w800"),
        main,
        ft.Divider(height=6, color="transparent"),
        prompt,
    )

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
