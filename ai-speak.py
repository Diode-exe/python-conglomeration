import requests
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_ollama(prompt):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        if "response" in data:
            return data["response"]
        else:
            print("Unexpected response format:")
            print(data)
            return "[Error: No response key]"
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return "[Error: Could not connect to Ollama]"
    



# Example usage
while True:
    what_to_ask = input(": ")
    reply = ask_ollama(what_to_ask)
    print("AI:", reply)
    speak(reply)
    