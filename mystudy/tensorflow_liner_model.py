'''
利用tensorflow定义线性模型，并训练求解。
基本步骤：    1. 定义模型
            2.  定义损失函数
            3. 定义训练过程
            4. 获取数据，训练模型

'''

import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
TRUE_W = tf.convert_to_tensor([[3.0,2.0]])
TRUE_b = 2.0
NUM_EXAMPLES = 1000
inputs = tf.random_normal(shape=[2,NUM_EXAMPLES])
noise = tf.random_normal(shape=[NUM_EXAMPLES])
#outputs = tf.tensordot(inputs, TRUE_W,axes=1) + TRUE_b + noise
outputs = tf.matmul(TRUE_W,inputs) + TRUE_b+ noise

class LinerModel(object):
    def __init__(self):
        self.W = tf.Variable(tf.ones([1,2]))
        self.b = tf.Variable(0.0)
    def __call__(self, x):
        #output = self.W*x + self.b
        output = tf.matmul(self.W,x)+self.b
        return output
def Loss_MSE(real,predict):
    loss = tf.reduce_mean(tf.square(real - predict))
    return loss
def train(model, inputs, outputs, learning_rate = 0.1):
    with tf.GradientTape() as t:
        current_loss = Loss_MSE(model(inputs), outputs)
    dW, db = t.gradient(current_loss,[model.W, model.b])
    model.W.assign_sub(dW*learning_rate)
    model.b.assign_sub(db*learning_rate)


model = LinerModel()

plt.scatter(inputs, outputs, c='b')
plt.scatter(inputs, model(inputs), c='r')
plt.show()
print('Current loss: '),
print(Loss_MSE(model(inputs), outputs).numpy())


ax = plt.figure().add_subplot(111, projection = '3d')
ax.scatter(inputs[0,:], inputs[1,:], outputs, c = 'r', marker = '^') #点为红色三角形
ax.scatter(inputs[0,:], inputs[1,:], model(inputs), c = 'b', marker = 'o') #点为红色三角形
plt.show()



# Collect the history of W-values and b-values to plot later
Ws, bs = [], []
epochs = range(50)
for epoch in epochs:
  Ws.append(model.W.numpy())
  bs.append(model.b.numpy())
  current_loss = Loss_MSE(model(inputs), outputs)
  train(model, inputs, outputs, 0.1)
  print('Epoch %2d: W=%1.2f b=%1.2f, loss=%2.5f' %
        (epoch, Ws[-1][0][0], bs[-1], current_loss))

# Let's plot it all
plt.plot(epochs, Ws[0], 'r',
         epochs, bs, 'b')
plt.plot([TRUE_W] * len(epochs), 'r--',
         [TRUE_b] * len(epochs), 'b--')
plt.legend(['W', 'b', 'true W', 'true_b'])
plt.show()


