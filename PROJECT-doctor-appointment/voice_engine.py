import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import tempfile

def speak(text):
    """Reads text aloud. Re-initializes every time to prevent Windows audio lockups."""
    try:
        # 1. Initialize a fresh engine every single time it speaks
        engine = pyttsx3.init()
        engine.setProperty('rate', 170) 
        
        print(f"🤖 [Audio]: {text}")
        engine.say(text)
        engine.runAndWait()
        
        # 2. Delete the engine immediately after speaking to free up the audio channel
        del engine 
    except Exception as e:
        print(f"🔈 [Audio out disabled] - {text} ({e})")

def get_hybrid_input(prompt_text):
    """Speaks the prompt and listens for exactly 5 seconds."""
    speak(prompt_text)
    
    recognizer = sr.Recognizer()
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio_path = temp_audio.name
    
    try:
        fs = 44100  
        seconds = 5  
        print("   🎙️ Listening... (5 seconds)")
        
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait() 
        sf.write(temp_audio_path, recording, fs) 
        
        with sr.AudioFile(temp_audio_path) as source:
            audio_data = recognizer.record(source)
            
        spoken_text = recognizer.recognize_google(audio_data)
        print(f"   ✅ You said: {spoken_text}")
        
        return spoken_text.strip()
        
    except sr.UnknownValueError:
        speak("I didn't hear anything. Please type your answer.")
        return input("   ⌨️ Type here: ").strip()
        
    except sr.RequestError:
        speak("I am having network issues. Please type your answer.")
        return input("   ⌨️ Type here: ").strip()
        
    except KeyboardInterrupt:
        raise 
        
    except Exception:
        speak("Microphone error. Please type.")
        return input("   ⌨️ Type here: ").strip()
        
    finally:
        if os.path.exists(temp_audio_path):
            try:
                os.remove(temp_audio_path)
            except OSError:
                pass