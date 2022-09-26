import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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
x_mx = [[1, 2.31, 65.2, 15.3], [1, 7.07, 78.9, 17.8], [1, 7.07, 61.1, 17.8], [1, 2.18, 45.8, 18.7],
        [1, 2.18, 54.2, 18.7], [1, 2.18, 58.7, 18.7], [1, 7.87, 96.1, 15.2], [1, 7.87, 100.0, 15.2],
        [1, 7.87, 85.9, 15.2], [1, 7.87, 94.3, 15.2]]
y_ar = [24, 21.6, 34.7, 33.4, 36.2, 28.7, 27.1, 16.5, 18.9, 15.0]
d.fit(X=np.matrix(x_mx),
      y=np.array(y_ar))
d.predict(X=np.matrix(x_mx))

v = LinearRegression(fit_intercept=True)
v.fit(X=np.matrix(x_mx), y=y_ar)

prediction_for_v = v.predict(x_mx)
rmse_v = mean_squared_error(y_ar, prediction_for_v) ** 0.5
r2_for_v = r2_score(prediction_for_v, y_ar)

print({'Intercept': abs(d.coefficients[0] - v.intercept_),
       'Coefficient': (v.coef_[1:] - d.coefficients[1:]),
       'R2': abs(d.r2_score() - r2_for_v),
       'RMSE': abs(d.rmse() - rmse_v)}
      )
