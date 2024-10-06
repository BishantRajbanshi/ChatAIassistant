import openai

openai.api_key = 'YOUR_API_KEY'

def get_gpt4_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ultron is listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google STT service")
        return ""



import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def ultron():
    while True:
        # Listen to user input
        user_input = listen()

        if user_input.lower() == "exit":
            print("Goodbye!")
            speak("Goodbye!")
            break

        if user_input:
            # Get response from GPT-4
            gpt4_response = get_gpt4_response(user_input)
            print(f"Ultron: {gpt4_response}")

            # Speak the response
            speak(gpt4_response)

if __name__ == "__main__":
    ultron()
