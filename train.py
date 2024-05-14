# importing the necessary liberaries:
# <_________________________________>

import json
from utils import tokenize, stem, bag_of_words
import numpy as np
import torch 
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader 
from model import Modeling

# loading intents from json file
# <_________________________________>

with open('intents.json','r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = [] #  Note: The xy list contains pairs of tokenized sentences and tags

# tokenized the sentences
# <_________________________________>

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w) # we use entend because we don't what an array of arrays [ [] , [] , [] ]
        xy.append((w,tag)) 


# remove all the unecessary characters
# <_________________________________>

ignore_words = ['?',')','(','!',';','.',',']
all_words = [stem(word) for word in all_words if word not in ignore_words]
all_words = sorted(set(all_words)) # set(all_words) to return just the unique words --> remove duplicates
tags = sorted(set(tags)) # ex. (['How', 'are', 'you', '?'], 'greeting')

#preparing the dataset
# <_________________________________>

X_train = [] # accumulate the bag of words vectors ( features)
y_train = [] # store the index that corresponds to the position that tags is stored in

for (pattern_sentence,tag)in xy:
    bag = bag_of_words(pattern_sentence,all_words)
    X_train.append(bag)
    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Chat Dataset
# <_________________________________>

class ChatDataset(Dataset):
    def __init__(self, X, y):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    # dataset(index)
    def __getitem__(self, index): # It returns a tuple containing the feature vector and label for a given index.
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples


# Hyperparameter
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(all_words)
learning_rate = 0.001
num_epochs = 1000



# creating the dataloader
dataset = ChatDataset(X_train, y_train)
train_loader = DataLoader(dataset = dataset, batch_size=batch_size , shuffle=True, num_workers=0)


# check if we have th GPU available or not
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = Modeling(input_size, hidden_size , output_size).to(device)


# loss and optimizer parameters

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


# training the model

for epoch in range(num_epochs):
    for(words,labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)
        labels = labels.long()

        # forward pass
        outputs = model(words)
        loss = criterion(outputs, labels)

        # backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    if epoch % 100 == 0:
        print(f'Epoch: {epoch+1:03}/{num_epochs} | Loss: {loss.item():.8f}')

print(f'final loss, loss = {loss.item():.4f}')


# save the training data
data = {
    "model_state": model.state_dict(),
    "input_size": input_size,
    "output_size": output_size,
    "hidden_size": hidden_size,
    "all_words": all_words,
    "tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)
print(f'training complete. saving training data to {FILE}')