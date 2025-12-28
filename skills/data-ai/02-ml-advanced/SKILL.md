---
name: data-ml-advanced
description: Master advanced machine learning. Learn scikit-learn, model selection, hyperparameter tuning, ensemble methods, and model evaluation.
---

# Advanced Machine Learning

## Model Training Pipeline
```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocessing
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_scaled, y_train)

# Evaluate
y_pred = model.predict(X_test_scaled)
from sklearn.metrics import accuracy_score, precision_score, recall_score
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"CV Score: {scores.mean():.3f}")
```

## Hyperparameter Tuning
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
    scoring='f1'
)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")
```

## Feature Engineering
```python
# Scaling
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Encoding categorical
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Feature creation
df['age_squared'] = df['age'] ** 2
df['log_income'] = np.log(df['income'])

# Feature selection
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)
```

## Ensemble Methods
```python
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    VotingClassifier
)

# Voting ensemble
voting_clf = VotingClassifier([
    ('rf', RandomForestClassifier()),
    ('gb', GradientBoostingClassifier()),
    ('lr', LogisticRegression())
])
voting_clf.fit(X_train, y_train)
```

## Evaluation Metrics
- **Accuracy**: (TP+TN)/(TP+TN+FP+FN)
- **Precision**: TP/(TP+FP)
- **Recall**: TP/(TP+FN)
- **F1-Score**: 2*(Precision*Recall)/(Precision+Recall)
- **AUC-ROC**: Area under ROC curve
- **Confusion Matrix**: TP, TN, FP, FN

## Key Concepts

✅ Train/test/validation split
✅ Overfitting & underfitting
✅ Bias-variance tradeoff
✅ Cross-validation
✅ Feature importance
✅ Class imbalance handling
✅ Model selection
✅ Regularization

