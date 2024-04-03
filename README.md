# Voice-Assisted Chatbot for the Visually Impaired

## Overview

Our project is dedicated to designing an innovative `chatbot equipped with speech recognition capabilities` to empower **blind** individuals. The core objective is to facilitate seamless interaction with technology and others around them. By harnessing advanced speech-to-text and natural language processing technologies, our chatbot not only understands and responds to verbal queries but also identifies distinct speakers. This feature significantly enhances the conversational experience by recognizing when different individuals speak, thereby creating a more intuitive and inclusive communication aid for those with visual impairments.


## Getting Started

### Setting Up the Environment

Create a virtual environment to manage your project's dependencies:

```bash
conda create -p venv python=3.12.1 -y


#### 2. Activate you environement

```bash
conda activate ./venv

```

#### 3. install PyTorch and dependecies 

- For Installation of PyTorch see official [website](https://pytorch.org/).

```python
pip3 install torch torchvision torchaudio
```
- also install **nltk** :

```bash	
pip install nltk
```
If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

``` bash
 nltk.download('punkt')
 ```
## Running this project

### Begin by training your model:

```bash
python train.py
```

### After training, a data.pth file will be created. Proceed by initiating the chatbot:


```bash
python chat.py
```

## Customization

Tailor `intents.json` according to your requirements:

Add new `tag`, `patterns`, and `responses` to personalize the chatbot's interaction scope. Keep in mind to retrain your model following any modifications to this file.

