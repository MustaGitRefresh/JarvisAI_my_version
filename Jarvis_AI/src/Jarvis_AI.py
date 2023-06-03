# IMPORTS
import speaker_output
import speech_recognition as sr
import Reader as reader


# The Code Starts Here
class Jarvis:

    def __init__(self):
        self.query = None
        speaker_output.say("Hello! I am listening to you")
        while True:
            print("listening")
            self.takeCommand()
            if self.query is not None:
                speaker_output.say(self.query)
            else:
                speaker_output.say("Please repeat it again")

    def takeCommand(self):
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            mic.pause_threshold = 0.8
            mic.energy_threshold = 270
            audio = mic.listen(source)
            try:
                text = mic.recognize_google(audio, language='hi-in')
                print(f"User said {text}")
                self.query = text
            except sr.UnknownValueError:
                print("Text is not recognisable")
                self.query = None
                return

    # todo: Modify it on some occasion.
    def reader(self):
        """This is the reader"""
        text = reader.reader('speaker_output.py')
        speaker_output.say(str(text))


jarvis = Jarvis()
