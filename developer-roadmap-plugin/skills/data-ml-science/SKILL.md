---
name: data-ml-science
description: Build machine learning systems with Python, scikit-learn, TensorFlow, and PyTorch. Master data preprocessing, feature engineering, model training, and deployment. Use when building ML pipelines, analyzing data, or implementing AI solutions.
---

# Data Science & Machine Learning

Build intelligent systems using machine learning, deep learning, and data analytics.

## Quick Start

### Data Preparation with Pandas
```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load and explore data
df = pd.read_csv('data.csv')
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values
df.fillna(df.mean(), inplace=True)  # Fill with mean
df.dropna(inplace=True)  # Remove rows with NaN

# Feature engineering
df['age_squared'] = df['age'] ** 2
df['is_premium'] = (df['spending'] > df['spending'].median()).astype(int)

# Data normalization
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['age', 'spending']])
```

### Scikit-Learn Classification
```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall: {recall_score(y_test, y_pred):.3f}")
print(f"F1: {f1_score(y_test, y_pred):.3f}")

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Mean: {scores.mean():.3f} (+/- {scores.std():.3f})")
```

### Deep Learning with TensorFlow
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Build neural network
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(28*28,)),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# Compile
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)
    ]
)

# Evaluate
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy:.3f}")
```

### PyTorch Training Loop
```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# Define model
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

model = NeuralNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10):
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
```

## ML Fundamentals

### Model Selection
- **Linear Models**: Fast, interpretable, good for linear relationships
- **Tree-based**: Handle non-linearity, feature importance
- **SVM**: Good for high-dimensional data
- **Neural Networks**: Complex patterns, requires more data

### Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.3f}")
```

### Handling Imbalanced Data
```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

# SMOTE for oversampling minority class
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Pipeline with resampling
pipeline = Pipeline([
    ('smote', SMOTE()),
    ('undersampler', RandomUnderSampler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```

## Feature Engineering

### Numerical Features
- **Scaling**: StandardScaler, MinMaxScaler, RobustScaler
- **Binning**: Convert continuous to categorical
- **Log Transform**: Handle skewed distributions
- **Polynomial Features**: Create higher-order interactions

### Categorical Features
- **One-Hot Encoding**: For nominal categories
- **Label Encoding**: For ordinal categories
- **Target Encoding**: Encode with target mean
- **Frequency Encoding**: Replace with frequency

## Evaluation Metrics

### Classification
- **Accuracy**: Overall correctness
- **Precision**: True positives / predicted positives
- **Recall**: True positives / actual positives
- **F1**: Harmonic mean of precision and recall
- **ROC-AUC**: Threshold-independent evaluation

### Regression
- **MSE**: Mean squared error
- **RMSE**: Root mean squared error
- **MAE**: Mean absolute error
- **R²**: Coefficient of determination

## Interview Questions

1. How do you handle missing data?
2. What's the difference between training and test sets?
3. Explain overfitting and how to prevent it
4. What's the bias-variance tradeoff?
5. How do you evaluate an imbalanced classification problem?

## Resources

- Scikit-Learn: https://scikit-learn.org
- TensorFlow: https://www.tensorflow.org
- PyTorch: https://pytorch.org
- Kaggle: https://www.kaggle.com/learn
- Fast.ai: https://fast.ai
