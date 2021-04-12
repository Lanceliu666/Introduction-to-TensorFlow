import tensorflow.compat.v1 as tf
#tf.disable_v2_behavior()

#import tensorflow as tf
tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.Session()

x = tf.placeholder(tf.string)

output = sess.run(x, feed_dict={x: 'Hello World'})

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

output = sess.run(y, feed_dict={x: 'Test String', y: 123, z: 45.67})

print(output)
