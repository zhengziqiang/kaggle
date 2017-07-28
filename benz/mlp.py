# coding=utf-8
import tensorflow as tf
import numpy as np
import os
from numpy import genfromtxt

feature_nd = genfromtxt('/home/zzq/kaggle/benz/feature', delimiter=',')
one_hot = genfromtxt('/home/zzq/kaggle/benz/one_hot', delimiter=',')
time_tag=np.genfromtxt("/home/zzq/kaggle/benz/test_tag",delimiter=',')
# Parameters
learning_rate = 0.002
training_epochs = 20000
batch_size = 100
display_step = 100

# Network Parameters
n_hidden_1 = 500  # 1st layer number of features
n_hidden_2 = 300  # 2nd layer number of features
n_hidden_3 = 200
n_hidden_4 = 50
n_input = 376  # MNIST data input (img shape: 28*28)
n_classes = 9  # MNIST total classes (0-9 digits)

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)

    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_3 = tf.nn.relu(layer_3)

    layer_4 = tf.add(tf.matmul(layer_3, weights['h4']), biases['b4'])
    layer_4 = tf.nn.relu(layer_4)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_4, weights['out']) + biases['out']
    return out_layer


# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'h4': tf.Variable(tf.random_normal([n_hidden_3, n_hidden_4])),
    'out': tf.Variable(tf.random_normal([n_hidden_4, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'b4': tf.Variable(tf.random_normal([n_hidden_4])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
# with tf.device('/gpu:0'):
pred = multilayer_perceptron(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
# optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# changed by zzq
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)

# Launch the graph
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    for epoch in range(training_epochs):
        sess.run(init)
        avg_cost = 0.

        _, c = sess.run([optimizer, cost], feed_dict={x: feature_nd,
                                                      y: one_hot})
        avg_cost += c

        # avg_cost/=total_batch
        # # Display logs per epoch step
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch + 1), "cost=", \
                  "{:.9f}".format(avg_cost))
    print("Optimization Finished!")
    test_feat = genfromtxt('/home/zzq/kaggle/benz/test_feature.csv', delimiter=',')
    # sess.run(pred,feed_dict={x:test_feat})
    index = tf.argmax(pred, 1)
    # print (index.eval(feed_dict={x:test_feat}))
    # 这样就可以打印出值了
    # out=file('/home/zzq/kaggle/house/test_file/test.txt','a+')
    # out.write((index.eval(feed_dict={x:test_feat})))
    # out.close()
    my_list = index.eval(feed_dict={x: test_feat})
    print type(index)

    if os.path.isfile('/home/zzq/result/benz/result.csv'):
        os.remove('/home/zzq/result/benz/result.csv')
    out = file('/home/zzq/result/benz/result.csv', 'a+')
    id_pro = 'ID,y\n'
    out.write(id_pro)
    out.close()
    for i in range(len(my_list)):
        out = file('/home/zzq/result/benz/result.csv', 'a+')
        my_list[i] += 7
        my_list[i] *= 10.0
        xian = str(int(time_tag[i])) + ',' + '%.8f' % my_list[i] + '\n'
        out.write(xian)
        out.close()