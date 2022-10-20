# write your code here
from collections import Counter
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

(x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data(path="mnist.npz")

# # Stage 1
# classes = np.array(y_train)
# x_train = x_train.reshape(len(x_train), -1)
# print("Classes:", np.unique(classes))
# print("Features' shape:", x_train.shape)
# print("Target's shape:", y_train.shape)
# print(f"min: {np.min(x_train):.1f}, max: {np.max(x_train):.1f}")

# # Stage 2
x_train = x_train.reshape(len(x_train), -1)
X_train, X_test, y_train, y_test = train_test_split(x_train[0:6000], y_train[0:6000], train_size=0.7, random_state=40)
print("x_train shape:", X_train.shape)
print("x_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
print("Proportion of samples per class in train set:")
print(pd.Series(y_train).value_counts(normalize=True))

