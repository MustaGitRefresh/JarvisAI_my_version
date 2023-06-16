# IMPORTS
import speaker_output
import speech_recognition as sr
import Reader


# The Code Starts Here
class Jarvis:

    def __init__(self):
        self.file_name = None
        speaker_output.say("Hello! I am listening to you")
        while True:
            print("listening")
            self.query = self.takeCommand()
            if self.query is not None:
                speaker_output.say("Running your command")
                self.checkCommand()
            else:
                speaker_output.say("Please repeat it again")

    def takeCommand(self, prompt=""):
        mic = sr.Recognizer()
        with sr.Microphone() as source:
            mic.pause_threshold = 0.8
            mic.energy_threshold = 270
            audio = mic.listen(source)
            try:
                if prompt:
                    speaker_output.say(prompt)
                text = mic.recognize_google(audio, language='en-in')
                print(f"User said {text}")
                return str(text)
            except sr.UnknownValueError:
                print("Text is not recognisable")
                self.query = None
                return

    def checkCommand(self):
        if "read file" in self.query.lower():
            speaker_output.say("Please enter the file name")
            self.file_name = input()
            file_text = Reader.reader(self.file_name)
            speaker_output.say(str(file_text))


jarvis = Jarvis()
