import numpy as np


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        X = np.matrix([[1, i] for i in X])
        self.coefficient = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
        final_dict = {'Intercept': np.array(self.coefficient.tolist()[0][0]),
                      'Coefficient': np.array(self.coefficient.tolist()[0][1])}
        print(final_dict)


b = CustomLinearRegression()
b.fit(X=np.array([4.0, 4.5, 5, 5.5, 6.0, 6.5, 7.0]),
      y=np.array([33, 42, 45, 51, 53, 61, 62]))
