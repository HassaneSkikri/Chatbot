import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
import pyttsx3
import speech_recognition as sr

import os
import numpy as np
from pyAudioAnalysis import audioBasicIO
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA


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
import os
import numpy as np
import librosa
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

def train_model(dataset_path):
    features, labels = [], []
    label_names = []

    # Process each file in the dataset
    for file in os.listdir(dataset_path):
        if file.endswith(".mp3"):
            speaker_name = file.split('.')[0]  # Assuming filename is 'speakername.mp3'
            label_names.append(speaker_name)
            file_path = os.path.join(dataset_path, file)

            # Load the audio file and extract MFCC features
            audio, sample_rate = librosa.load(file_path, sr=None)  # sr=None to maintain original sample rate
            mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
            mean_features = np.mean(mfccs.T, axis=0)  # Taking the mean across time frames
            
            features.append(mean_features)
            labels.append(len(label_names) - 1)

    # Train a simple LDA model
    model = LDA()
    model.fit(features, labels)
    return model, label_names


def identify_speaker(audio_path, model, label_names):
    # Load the audio file and extract MFCC features
    audio, sample_rate = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    mean_features = np.mean(mfccs.T, axis=0)  # Taking the mean across time frames
    
    # Predict the label of the new audio file
    predicted_label = model.predict([mean_features])[0]
    return label_names[predicted_label]
