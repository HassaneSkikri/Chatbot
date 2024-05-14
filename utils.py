#_______________________________________________________________________________________________________________________#
# Liberaries to be imported #
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
import pyttsx3
import speech_recognition as sr
import os
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import os
import librosa
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#_______________________________________________________________________________________________________________________#

stemmer = PorterStemmer()

#_______________________________________________________________________________________________________________________#

def tokenize(sentence):
    # Tokenizes a sentence into words
    return nltk.word_tokenize(sentence)


#_______________________________________________________________________________________________________________________#
def stem(word):
    # Stems the word to its root form
    return stemmer.stem(word.lower())


#_______________________________________________________________________________________________________________________#

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for indx, word in enumerate(all_words):
        if word in tokenized_sentence:
            bag[indx] = 1.0
    return bag


#_______________________________________________________________________________________________________________________#
# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#_______________________________________________________________________________________________________________________#
# Function to convert speech to text
def listen(): 
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


# identify speaker part:
#_______________________________________________________________________________________________________________________#

def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, sr=None)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_processed = np.mean(mfccs.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", file_path, "Error: ", e)
        return None
    return mfccs_processed

#_______________________________________________________________________________________________________________________#
def load_dataset(dataset_path):
    features = []
    labels = []
    file_count = {}  

    for speaker_dir in os.listdir(dataset_path):
        speaker_path = os.path.join(dataset_path, speaker_dir)
        if os.path.isdir(speaker_path):
            for file in os.listdir(speaker_path):
                if file.endswith((".wav", ".mp3")):
                    file_path = os.path.join(speaker_path, file)
                    mfccs = extract_features(file_path)

                    if mfccs is not None:
                        features.append(mfccs)
                        labels.append(speaker_dir)  
                        file_count[speaker_dir] = file_count.get(speaker_dir, 0) + 1

    print("Files per speaker:", file_count)
    return np.array(features), labels


#_______________________________________________________________________________________________________________________#

def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels, random_state=0)
    model = LDA()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    return model


#____________________________________________________________________________________________________________________#
def identify_speaker(model, audio_path):
    features = extract_features(audio_path)
    if features is not None:
        speaker = model.predict([features])[0]
        return speaker
    return "Unknown"


#____________________________________________________________________________________________________________________#

def load_model(model_path):
    # Load a model from a pickle file
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model


#____________________________________________________________________________________________________________________#


# if __name__ == "__main__":
    # dataset_path = 'voice_dataset'
    # features, labels = load_dataset(dataset_path)
    # model = train_model(features, labels)
    # Optionally, save the model to a file for later use
    # with open('model.pkl', 'wb') as f:
    #     pickle.dump(model, f)
    # model = load_model('model.pkl')
    # test_audio_path = 'voice_dataset\Speaker0040\Speaker0040_000.wav'
    # print("Identified Speaker:", identify_speaker(model, test_audio_path))
