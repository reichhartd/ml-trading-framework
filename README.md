# ML Trading Framework

A comprehensive machine learning framework for predicting bull/bear market signals using Bitcoin time series data. This project implements a complete ML pipeline for financial time series prediction, including data acquisition, preprocessing, feature engineering, model training, evaluation, and visualization.

## Project Overview

This framework is designed to predict trading signals (bull/bear market indicators) for Bitcoin price data using machine learning classification techniques. The system:

1. Downloads and processes Bitcoin historical price data
2. Applies technical indicators as features (SMA, EMA, RSI, ROC, Momentum, Stochastic Oscillator)
3. Generates bull/bear market signals based on moving average crossovers
4. Evaluates multiple classification models to predict these signals
5. Provides visualization tools for data exploration and results interpretation

## Repository Structure

- `src/` - Main source code
    - `config/` - Configuration settings
    - `data/` - Data acquisition and preprocessing
    - `features/` - Feature engineering and technical indicators
    - `models/` - Model selection, training and evaluation
    - `utils/` - Utility functions including logging
    - `visualization/` - Visualization components
- `data/` - Data storage (raw, processed, and splits)
- `notebooks/` - Jupyter notebooks for exploration
- `tests/` - Test suite
- `docs/` - Documentation

## Machine Learning Pipeline

1. **Problem Formulation**: Binary classification predicting bull/bear market signals for Bitcoin trading using technical indicators
2. **Dataset Preparation**: Chronological time series splitting (60/20/20 for train/validation/test)
3. **Feature Engineering**: Technical indicators (SMA, EMA, RSI, ROC, Momentum, Stochastic Oscillator)
4. **Model Selection**: Comparison of 14 classification models
    - Linear Models:
        - Linear Discriminant Analysis (LDA)
        - Logistic Regression (LOG)
        - Stochastic Gradient Descent (SGD)
        - Linear Support Vector Machines (LinearSVM)
    - Tree-based Models:
        - Decision Tree (TREE)
        - Random Forest (RF)
        - Bagging Classifier (BAG)
    - Boosting Models:
        - AdaBoost (ADA)
        - Gradient Boosting Machine (GBM)
        - XGBoost (XGB)
        - CatBoost (CAT)
    - Distance and Probability-based Models:
        - Gaussian Naive Bayes (NB)
        - K-Nearest Neighbors (KNN)
    - Neural Network Models:
        - Multi-layer Perceptron (MLP)
5. **Performance Metrics**: Accuracy scores for training, validation and complete datasets
6. **Visualization**: Time series plots, correlation matrices, model performance comparisons

## Installation and Setup

```zsh
poetry install
```

## Usage

```zsh
# Run the entire pipeline
poetry run python -m src

# To disable plots
# Edit src/config/main.py and set PLOT_DATA = False
```

## Key Components

- **Dataset Class**: Handles downloading, processing, and splitting Bitcoin price data
- **Technical Indicators**: Calculates various technical indicators used as features
- **Bull/Bear Signal Generation**: Creates target variable based on 10-minute and 60-minute moving average crossovers
- **Model Evaluation**: Trains and evaluates multiple classification models

## Results and Visualization

The framework includes visualization tools for:

- Time series data with signals
- Missing data analysis
- Correlation matrices
- Model performance comparison

## Requirements

Dependencies are listed in `pyproject.toml` and include:

- pandas
- numpy
- scikit-learn
- xgboost
- catboost
- kaggle
- matplotlib
- seaborn
- plotly
