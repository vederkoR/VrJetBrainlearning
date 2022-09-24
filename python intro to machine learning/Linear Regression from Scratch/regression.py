import numpy as np


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.coefficient = np.array([])
        self.intercept = float()
        self.coefficients = None

    def fit(self, X, y):
        if self.fit_intercept:
            X = np.matrix([[1, i] for i in X])
            self.coefficients = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y).tolist()[0]
            self.coefficient = self.coefficients.tolist()[0]
            self.intercept = self.coefficients.tolist()[0]
        else:
            self.coefficients = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y).tolist()[0]

    def predict(self, X):
        return (X @ np.array(self.coefficients)).tolist()[0]


d = CustomLinearRegression(fit_intercept=False)
d.fit(X=np.matrix([[4, 1, 11], [4.5, -3, 15], [5, 2, 12], [5.5, 5, 9], [6, 0, 18], [6.5, 3, 13], [7, 6, 16]]),
      y=np.array([33, 42, 45, 51, 53, 61, 62]))

print(np.array(
    d.predict(X=np.matrix([[4, 1, 11], [4.5, -3, 15], [5, 2, 12], [5.5, 5, 9], [6, 0, 18], [6.5, 3, 13], [7, 6, 16]]))))
