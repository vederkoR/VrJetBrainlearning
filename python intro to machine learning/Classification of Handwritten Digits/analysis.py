# write your code here
from collections import Counter
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import Normalizer


# # Stage 3

def fit_predict_eval(model, features_train, features_test, target_train, target_test):
    model.fit(features_train, target_train)
    y_pred = model.predict(features_test)
    score = accuracy_score(target_test, y_pred)
    print(f'Model: {model}\nAccuracy: {score:.3}\n')


if __name__ == "__main__":
    (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data(path="mnist.npz")
    x_train = x_train.reshape(len(x_train), -1)
    X_train, X_test, y_train, y_test = train_test_split(x_train[0:6000], y_train[0:6000], train_size=0.7,
                                                        random_state=40)
    normalizer = Normalizer()
    x_train_norm = normalizer.transform(X_train)
    x_test_norm = normalizer.transform(X_test)
    models = (KNeighborsClassifier(),
              DecisionTreeClassifier(random_state=40),
              LogisticRegression(random_state=40, solver="liblinear"),
              RandomForestClassifier(random_state=40))
    for model in models:
        fit_predict_eval(
            model=model,
            features_train=x_train_norm,
            features_test=x_test_norm,
            target_train=y_train,
            target_test=y_test,
        )

    print("The answer to the 1st question: yes")
    print("The answer to the 2nd question: KNeighborsClassifier-0.953, RandomForestClassifier-0.937")

# # Stage 1
# classes = np.array(y_train)
# x_train = x_train.reshape(len(x_train), -1)
# print("Classes:", np.unique(classes))
# print("Features' shape:", x_train.shape)
# print("Target's shape:", y_train.shape)
# print(f"min: {np.min(x_train):.1f}, max: {np.max(x_train):.1f}")

# # Stage 2
#     print("x_train shape:", X_train.shape)
#     print("x_test shape:", X_test.shape)
#     print("y_train shape:", y_train.shape)
#     print("y_test shape:", y_test.shape)
#     print("Proportion of samples per class in train set:")
#     print(pd.Series(y_train).value_counts(normalize=True))

