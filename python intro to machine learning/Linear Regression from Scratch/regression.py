import numpy as np


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):
        self.fit_intercept = fit_intercept
        self.coefficient = np.array([])
        self.intercept = float()
        self.coefficients = None
        self.predicted = None
        self.measured = None
        self.MSE = None
        self.average = None

    def fit(self, X, y):
        self.measured = y
        self.average = sum(y) / len(y)
        if self.fit_intercept:
            X = np.matrix([[1, i] for i in X])
            self.coefficients = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y).tolist()[0]
            self.coefficient = self.coefficients.tolist()[0]
            self.intercept = self.coefficients.tolist()[0]
        else:
            self.coefficients = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y).tolist()[0]

    def predict(self, X):
        self.predicted = (X @ np.array(self.coefficients)).tolist()[0]
        self.MSE = \
            sum([(self.predicted[i] - self.measured[i]) ** 2 for i in range(len(self.predicted))]) / len(self.predicted)
        return self.predicted

    def rmse(self):
        return self.MSE ** 0.5

    def r2_score(self):
        return 1 - (sum([(self.predicted[i] - self.measured[i]) ** 2 for i in range(len(self.predicted))]) /
                    (sum([(self.predicted[i] - self.average) ** 2 for i in range(len(self.predicted))])))


d = CustomLinearRegression(fit_intercept=False)
x = [[1, 0.9, 11], [1, 0.5, 11], [1, 1.75, 9], [1, 2, 8], [1, 1.4, 7], [1, 1.5, 7], [1, 3, 6], [1, 1.1, 5],
     [1, 2.6, 5], [1, 1.9, 4]]
d.fit(X=np.matrix(x),
      y=np.array([21.95, 27.18, 16.9, 15.37, 16.03, 18.15, 14.22, 18.72, 15.4, 14.69]))
d.predict(X=np.matrix(x))


print({'Intercept': d.coefficients[0],
       'Coefficient': np.array(d.coefficients[1:]),
       'R2': d.r2_score(),
       'RMSE': d.rmse()}
      )
