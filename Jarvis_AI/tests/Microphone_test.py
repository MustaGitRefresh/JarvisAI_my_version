import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("listening")
    audio = recognizer.listen(source)

    try:
        final_text = recognizer.recognize_google(audio)
        print(final_text)
    except sr.UnknownValueError:
        print("Speech couldn't be recognised")
    except Exception as e:
        print("Something went wrong")
        print(e)
