# Chatbot Project

## Summary

This project is focused on building a chatbot using Python, enhancing my coding skills and deepening my understanding of concepts like tokenization, natural language processing, and machine learning. Through developing this chatbot, I've gained valuable insights into practical AI applications. Join me in exploring the intricacies of chatbot technology!


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
