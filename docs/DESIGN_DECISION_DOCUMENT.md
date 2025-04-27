# ML Trading Framework - Design Decision Document

## Problem Definition and Motivation

### Problem Statement

This project aims to develop a machine learning system capable of predicting bull and bear market signals for Bitcoin trading using historical price data and technical indicators. The core problem is framed as a binary classification task where the target variable indicates whether to enter the market (bull signal = 1) or exit the market (bear signal = 0).

### Motivation

Financial markets, particularly cryptocurrency markets, exhibit high volatility and complex patterns that are challenging for human traders to interpret consistently. Machine learning models can potentially identify patterns in technical indicators that precede market transitions, providing traders with actionable signals. By comparing multiple classification algorithms, I seek to identify the most effective approach for this specific prediction task.

### Success Criteria

- Model accuracy significantly above 50% (random chance) on validation data
- Consistent performance across different market conditions
- Interpretable results that can be translated into actionable trading decisions
- Practical implementation that can be updated with new data

## Dataset Analysis

### Data Source Selection

I selected Bitcoin price data from Kaggle for several reasons:

1. High granularity (1-minute intervals)
2. Extensive historical coverage
3. Includes OHLCV (Open, High, Low, Close, Volume) data necessary for technical indicator calculation
4. Structured in a format good for time series analysis

### Data Preparation Strategy

The dataset preparation follows these key steps:

1. **Data Acquisition**: Automated downloading from Kaggle API
2. **Timestamp Conversion**: Converting Unix timestamps to datetime format
3. **Chronological Splitting**:
    - Training (60%): Earliest portion for model training
    - Validation (20%): Middle portion for hyperparameter tuning
    - Test (20%): Most recent portion for final evaluation

This chronological splitting approach was chosen specifically to respect the time-series nature of financial data, preventing data leakage that would occur with random splitting.

### Data Quality Assessment

Initial exploratory analysis revealed:

- No significant missing values in core OHLCV fields
- Consistent time intervals (1-minute granularity)
- No anomalous price movements requiring special treatment

## Feature Engineering

### Target Variable Definition

The target variable ("signal") is derived using a moving average crossover strategy:

- When the Short-Term Moving Average (10-minute SMA) crosses above the Long-Term Moving Average (60-minute SMA), a buy signal (1) is generated
- When the Short-Term Moving Average falls below the Long-Term Moving Average, a sell signal (0) is generated

This approach was chosen as it's a well-established technique in technical analysis for identifying trend reversals. Since we're using 1-minute interval data, these windows represent 10-minute and 60-minute time periods.

### Technical Indicators Selection

I implemented several technical indicators as features, each chosen for specific market insights they provide:

1. **Simple Moving Average (SMA)**: Smooths price action to identify trends by averaging price over specified periods.
2. **Exponential Moving Average (EMA)**: Similar to SMA but gives more weight to recent prices.
3. **Relative Strength Index (RSI)**: Momentum oscillator measuring speed and change of price movements.
4. **Rate of Change (ROC)**: Calculates percentage price change over specified periods.
5. **Momentum**: Measures price change acceleration.
6. **Stochastic Oscillator**: Compares closing price to price range over time.

## Model Selection and Evaluation

### Model Selection Criteria

I evaluated multiple classification algorithms based on:

1. Performance on validation data
2. Training time efficiency
3. Compatibility with feature characteristics
4. Interpretability of results

### Models Evaluated

Fourteen different classification models were implemented and compared, organized into categories:

**Linear Models**:

1. **Linear Discriminant Analysis (LDA)**
2. **Logistic Regression (LOG)**
3. **Stochastic Gradient Descent (SGD)** with log loss
4. **Linear Support Vector Machines (LinearSVM)**

**Tree-based Models**:

5. **Decision Tree (TREE)**
6. **Random Forest (RF)**
7. **Bagging Classifier (BAG)** with Decision Trees as base estimators

**Boosting Models**:

8. **AdaBoost (ADA)**
9. **Gradient Boosting Machine (GBM)**
10. **XGBoost (XGB)**
11. **CatBoost (CAT)**

**Distance and Probability-based Models**:

12. **Gaussian Naive Bayes (NB)**
13. **K-Nearest Neighbors (KNN)**

**Neural Network Models**:

14. **Multi-layer Perceptron (MLP)** with hidden layers (100, 50)

### Evaluation Methodology

Models were evaluated using:

1. Accuracy on training data to assess fit
2. Accuracy on validation data to assess generalization
3. Accuracy on complete dataset for final comparison

## Visualization Strategy

### Time Series Visualization

Implemented time series visualizations to:

1. Display raw price data alongside signals
2. Compare technical indicators (SMA_10, SMA_60) with generated signals
3. Visualize train/validation splits of the data

### Model Performance Visualization

Model performance is visualized using:

1. Heatmaps of accuracy scores across different datasets (training, validation, complete)
2. Comparative bar charts for model performance benchmarking

## Results and Insights

### Model Performance Summary

Initial results show promising performance from ensemble methods (Random Forest, XGBoost, CatBoost) compared to simpler models. This aligns with expectations as ensemble methods can better capture the complex non-linear relationships in financial data.

## Conclusion

The ML Trading Framework successfully implements a complete machine learning pipeline for predicting bull/bear market signals using Bitcoin price data and technical indicators. The modular architecture enables easy extension and experimentation with different features and models. While current results show promise, several areas for improvement have been identified for future development.

This project demonstrates a practical application of machine learning to financial time series prediction, balancing technical rigor with practical implementation considerations.
