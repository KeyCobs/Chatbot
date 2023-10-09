import speech_recognition as sr

def voice_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:       
        try:
            # Adjust for ambient noise before listening
            recognizer.adjust_for_ambient_noise(source)
            
            print("Please start speaking...")
            # Listen to the audio input from the microphone
            audio = recognizer.listen(source)

            # Recognize the spoken text using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(text)
            return text

        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
            return None
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
            return None

