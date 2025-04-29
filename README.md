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
- `docs/` - Documentation

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
