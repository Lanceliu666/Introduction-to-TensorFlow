import tensorflow as tf
tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.Session()

# Create TensorFlow object called hello_constant
hello_constant = tf.constant('Hello World!')


# Run the tf.constant operation in the session
output = sess.run(hello_constant)
print(output)
