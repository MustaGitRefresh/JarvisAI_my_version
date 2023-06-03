import win32com.client


if __name__ != '__main__':
    speaker = win32com.client.Dispatch("SAPI.SpVoice")


    def say(text):
        speaker.Speak(text)
