import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

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

