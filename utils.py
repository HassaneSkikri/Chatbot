import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
import pyttsx3
import speech_recognition as sr

# Instantiate the stemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    # Tokenizes a sentence into words
    return nltk.word_tokenize(sentence)

def stem(word):
    # Stems the word to its root form
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    # Create a bag of words from a tokenized sentence and a list of all words
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for indx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[indx] = 1.0
    return bag

def speak(text): # Function to convert text to speech
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen(): # Function to convert speech to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "I didn't catch that. Could you please repeat?"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "There was an error with the speech service."
