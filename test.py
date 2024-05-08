import numpy as np
import os
import librosa
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

def extract_features(audio_path):
    audio, sample_rate = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

def train_model(dataset_path):
    features, labels = [], []
    label_names = []

    # Process each file in the dataset
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith(".mp3"):
                speaker_name = os.path.basename(root)
                if speaker_name not in label_names:
                    label_names.append(speaker_name)
                
                audio_path = os.path.join(root, file)
                mfcc_features = extract_features(audio_path)
                
                features.append(mfcc_features)
                labels.append(label_names.index(speaker_name))


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

# Usage
if __name__ == "__main__":
    model, label_names = train_model(r"voice_dataset")
    print("Model trained with label names:", label_names)
    prediction = identify_speaker(r"voice_dataset", model, label_names)
    print("the label name is ",prediction)