#!/usr/bin/env python3
"""
Machine Learning Pipeline Template
Production-ready ML workflow
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from typing import Tuple, Dict, Any
import joblib

class MLPipeline:
    """End-to-end ML pipeline."""

    def __init__(self, model, random_state: int = 42):
        self.model = model
        self.scaler = StandardScaler()
        self.random_state = random_state
        self.is_fitted = False

    def preprocess(self, X: pd.DataFrame) -> np.ndarray:
        """Preprocess features."""
        return self.scaler.fit_transform(X) if not self.is_fitted else self.scaler.transform(X)

    def train(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> Dict[str, Any]:
        """Train model with train/test split."""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )

        # Preprocess
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Train
        self.model.fit(X_train_scaled, y_train)
        self.is_fitted = True

        # Evaluate
        y_pred = self.model.predict(X_test_scaled)

        return {
            'accuracy': accuracy_score(y_test, y_pred),
            'report': classification_report(y_test, y_pred, output_dict=True)
        }

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Make predictions."""
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def save(self, path: str):
        """Save pipeline."""
        joblib.dump({'model': self.model, 'scaler': self.scaler}, path)

    @classmethod
    def load(cls, path: str) -> 'MLPipeline':
        """Load pipeline."""
        data = joblib.load(path)
        pipeline = cls(data['model'])
        pipeline.scaler = data['scaler']
        pipeline.is_fitted = True
        return pipeline
