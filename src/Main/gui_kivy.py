import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

#dictionary linking menu objects to a row in GUI
menu_gui_dict = {}

class KivyApp(App):
    def build(self):
        Window.size = (800, 600)
        self.title = "Hello, World!"
        button = Button(text="Exit")
        button.bind(on_press=quit)
        return button

app = KivyApp()
app.run()

if __name__ == '__main__':
    print("joe")