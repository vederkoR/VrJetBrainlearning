import os

import numpy as np
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error as mape
from sklearn.model_selection import train_test_split


def data_loader():
    # checking ../Data directory presence
    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # download data if it is unavailable
    if 'data.csv' not in os.listdir('../Data'):
        url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/data.csv', 'wb').write(r.content)

def mape(y_test, pred):
    y_test, pred = np.array(y_test), np.array(pred)
    mape = np.mean(np.abs((y_test - pred) / y_test))
    return mape

def main():
    # read data
    data_loader()
    data = pd.read_csv('../Data/data.csv')

    # write your code here
    X = np.array(data.rating).reshape(-1, 1)
    y = np.array(data.salary)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    prediction = lr_model.predict(X_test)
    mape_final = mape(y_test, prediction)
    print(round(lr_model.intercept_, 5), round(lr_model.coef_[0], 5), round(mape_final, 5))


if __name__ == "__main__":
    main()
