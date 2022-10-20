# write your code here
import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path="mnist.npz")

classes = np.array(y_train)
x_train = x_train.reshape(len(x_train), -1)
print("Classes:", np.unique(classes))
print("Features' shape:", x_train.shape)
print("Target's shape:", y_train.shape)
print(f"min: {np.min(x_train):.1f}, max: {np.max(x_train):.1f}")

