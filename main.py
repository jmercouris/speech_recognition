# Resize the Window - Non Pep8 Compliant, mandated by Kivy
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()


# Root Widget
class Root(BoxLayout):
    pass


class RecordButton(Button):
    # String Property to Hold output for publishing by Textinput
    output = StringProperty('')
    
    def record(self):
        # GUI Blocking Audio Capture
        with m as source:
            audio = r.listen(source)
        
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            self.output = "You said \"{}\"".format(value)
        
        except sr.UnknownValueError:
            self.output = ("Oops! Didn't catch that")
        
        except sr.RequestError as e:
            self.output = ("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))


class SpeechApp(App):
    def build(self):
        # Calibrate the Microphone to Silent Levels
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
        # Create a root widget object and return as root
        return Root()


# When Executed from the command line (not imported as module), create a new SpeechApp
if __name__ == '__main__':
    SpeechApp().run()

