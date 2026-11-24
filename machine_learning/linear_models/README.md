# Linear Models

This directory contains linear models implemented with scikit-learn.

## Linear regression

`0-linear_regression.py` provides `Linear_Regression()`, which returns an
untrained `sklearn.linear_model.LinearRegression` model with default
hyperparameters. The function takes no arguments. Its only import is
`from sklearn import linear_model`.

Load the function and train the model with feature data `X` and targets `y`:

```python
Linear_Regression = __import__('0-linear_regression').Linear_Regression

model = Linear_Regression()
print(model.get_params())

X = [[0], [1], [2], [3]]
y = [1, 3, 5, 7]
model.fit(X, y)

print(model.coef_)       # [2.]
print(model.intercept_)  # Approximately 1.0
print(model.predict([[4]]))  # [9.]
```

Training with `fit(X, y)` creates the learned attributes `coef_` and
`intercept_`. These attributes are unavailable before training.

## Requirements

- Python 3
- scikit-learn
- pycodestyle for style validation

From this directory, check the Python file with:

```sh
pycodestyle 0-linear_regression.py
```
