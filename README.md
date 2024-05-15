# VoiceBot: A Multifunctional Voice-Enabled Chatbot

## Overview

VoiceBot is an advanced chat application designed to demonstrate integrated functionalities of modern chatbots including text-based chatting, voice commands, text-to-speech responses, and speaker identification. This project combines Python programming, natural language processing, machine learning, and digital signal processing to create a user-friendly chatbot capable of interacting with users through both text and voice.

## Features

- **Text Chat**: Interact using typed text with responses generated from a trained model.
- **Voice Commands**: Convert spoken language into text using speech recognition.
- **Text-to-Speech**: Hear responses spoken back to you, enhancing the interactive experience.
- **Speaker Identification**: Identify and verify the speaker's identity through voice analysis.

## Technologies Used

- **Python**: Primary programming language.
- **Tkinter**: GUI toolkit for Python to create the application interface.
- **PyTorch**: For implementing and training machine learning models.
- **SpeechRecognition**: For converting spoken language into text.
- **pyttsx3**: A text-to-speech conversion library in Python.
- **Librosa**: For processing audio signals and extracting features.
- **Sklearn**: For machine learning models used in speaker identification.


## Getting Started

### Setting Up the Environment

Create a virtual environment to manage your project's dependencies:

```bash
conda create -p venv python=3.12.1 -y


#### 2. Activate you environement

```bash
conda activate ./venv

```

#### 3. install PyTorch

- For Installation of PyTorch see official [website](https://pytorch.org/).


## Running this project

### Begin by training your model:

```bash
python train.py
```

### After training, a data.pth file will be created. Proceed by initiating the chatbot:


```bash
python chat.py
```

### the final step is to start the GUI for the VoiceBot:

```bash
python3 app.py
```

## Customization

Tailor `intents.json` according to your requirements:

Add new `tag`, `patterns`, and `responses` to personalize the chatbot's interaction scope. Keep in mind to retrain your model following any modifications to this file.



# Terminology and step by step to create this project

## starting by the pipeline

1. **Tokenization**
   - Input: "Is anyone there?"
   - Output: `["Is", "anyone", "there", "?"]`

2. **Lowercasing and Stemming**
   - Process the tokens by converting to lowercase and then applying stemming (if necessary).
   - Output remains: `["is", "anyon", "there", "?"]` 

3. **Removing Punctuation Characters**
   - Exclude punctuation from tokens.
   - Output: `["is", "anyon", "there"]`

4. **Bag of Words**
   - Convert the tokens into a numerical format known as a bag of words.
   - Output Vector: `[0, 0, 0, 1, 0, 1, 0, 1]`


### 1. Create the utils.py

- Create the tokenize function 

***  
    tokenize function split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
***

- Create the stem function

***
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
***


- create the bag_of_words function 

***
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
***


##### the dataset that i use to train the model for "identify speaker" part is very larg so you can download it  [here](https://www.kaggle.com/datasets/vjcalling/speaker-recognition-audio-dataset)