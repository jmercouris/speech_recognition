from kivy.app import App
from kivy.uix.widget import Widget


# Root Widget
class Root(Widget):
    pass


class SpeechApp(App):
    
    def build(self):
        return Root()


if __name__ == '__main__':
    SpeechApp().run()
