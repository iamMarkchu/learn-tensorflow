# 常量, 加法
import tensorflow as tf
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)
sess = tf.Session()
print(node1)
print(sess.run(node1))
print(sess.run(node3))