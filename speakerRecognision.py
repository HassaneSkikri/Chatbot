import os
import numpy as np
import librosa
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def extract_features(file_path):
    try:
        audio, sample_rate = librosa.load(file_path, sr=None)
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccs_processed = np.mean(mfccs.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", file_path, "Error: ", e)
        return None 
    return mfccs_processed

def load_dataset(dataset_path):
    features = []
    labels = []
    file_count = {}  # To count files per speaker

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

def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, stratify=labels, random_state=0)
    model = LDA()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    return model

def identify_speaker(model, audio_path):
    features = extract_features(audio_path)
    if features is not None:
        speaker = model.predict([features])[0]
        return speaker
    return "Unknown"

# Main execution
if __name__ == "__main__":
    dataset_path = 'voice_dataset'  # Adjust this path
    features, labels = load_dataset(dataset_path)
    model = train_model(features, labels)

    # Save the trained model
    with open('speaker_recognition_model.pkl', 'wb') as file:
        pickle.dump(model, file)
        print("Model saved to 'speaker_recognition_model.pkl'")
