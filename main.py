# Resize the Window - Non Pep8 Compliant, mandated by Kivy
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '550')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import speech_recognition as sr


r = sr.Recognizer()
m = sr.Microphone()


# Root Widget
class Root(BoxLayout):
    pass


class Listen(Button):
    def record(self):
        print("Recording")
        print("Say something!")
        with m as source:
            audio = r.listen(source)
        print("Got it! Now to recognize it...")
        
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print("You said {}".format(value))
        
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


class SpeechApp(App):
    
    def build(self):
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
        return Root()


if __name__ == '__main__':
    SpeechApp().run()

