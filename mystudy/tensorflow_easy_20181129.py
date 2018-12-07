import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras





tf.enable_eager_execution()

x = tf.ones((2, 2))

with tf.GradientTape() as t:
    t.watch(x)
    y = tf.reduce_sum(x)
    z = tf.multiply(y, y)

# Derivative of z with respect to the original input tensor x
dz_dx = t.gradient(z, x)
for i in [0, 1]:
    for j in [0, 1]:
        assert dz_dx[i][j].numpy() == 8.0

x = tf.convert_to_tensor( 3.0)
with tf.GradientTape(persistent=True) as t:
  t.watch(x)
  y = x * x
  z = y * y
dz_dx = t.gradient(z, x)  # 108.0 (4*x^3 at x = 3)
dy_dx = t.gradient(y, x)  # 6.0
del t  # Drop the reference to the tape


x = tf.zeros([2, 2])
x += 2  # This is equivalent to x = x + 2, which does not mutate the original
        # value of x
print(x)




layer = tf.keras.layers.Dense(10, input_shape=(None, 5))
layer(tf.zeros([10, 5]))
layer.variables

layer.kernel, layer.bias

tf.keras.layers.BatchNormalization


tf.keras.layers.Conv2D















