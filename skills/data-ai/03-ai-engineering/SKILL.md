---
name: ai-engineering
description: Master AI engineering with deep learning, TensorFlow, PyTorch, model deployment, and AI applications including LLMs and agents.
---

# AI Engineering

## Deep Learning Basics
```python
import tensorflow as tf
from tensorflow import keras

# Build model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

# Compile
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(X_train, y_train, epochs=20, batch_size=32)

# Evaluate
test_loss, test_accuracy = model.evaluate(X_test, y_test)
```

## PyTorch
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        return self.fc2(x)

# Training loop
optimizer = torch.optim.Adam(model.parameters())
loss_fn = nn.CrossEntropyLoss()

for epoch in range(20):
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = loss_fn(outputs, y_batch)
        loss.backward()
        optimizer.step()
```

## Transfer Learning
```python
# Use pretrained model
base_model = keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

# Add custom layers
model = keras.Sequential([
    base_model,
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

## Model Deployment
```python
# Save model
model.save('my_model.h5')

# FastAPI endpoint
from fastapi import FastAPI
import numpy as np

app = FastAPI()
model = keras.models.load_model('my_model.h5')

@app.post("/predict")
async def predict(data: list):
    prediction = model.predict(np.array([data]))
    return {"prediction": prediction.tolist()}
```

## AI Agents & LLMs
```python
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# Agent with tools
agent = initialize_agent(
    tools,
    llm=OpenAI(),
    agent="zero-shot-react-description",
    verbose=True
)

result = agent.run("What is 2 + 2?")
```

## Key Concepts

✅ Layers & activations
✅ Backpropagation
✅ Batch normalization
✅ Regularization
✅ CNNs for vision
✅ RNNs for sequences
✅ Transformers
✅ Fine-tuning
✅ Model serving

