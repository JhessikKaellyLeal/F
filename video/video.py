from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video

d = str(input("Digite o caminho: "))

class WK(App):
    def build(self):
        box = BoxLayout(orientation="vertical")
        video = Video(source=d)
        video.state = "stop"
        video.size = 200, 200
        def play(button):
            if(video.state ==  "stop"):
                video.state = "play"
                button.text = "Parar"
            else:
                video.state = "stop"
                button.text = "Iniciar"
        button = Button(text="Iniciar", on_release=play)
        button.size_hint = 0.2, 0.2
        button.size_hint_x = 1
        box.add_widget(video)
        box.add_widget(button)
        return box

WK().run()