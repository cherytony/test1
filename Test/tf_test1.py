import tensorflow as tf
import matplotlib.pyplot as plt

"""
tf.image.crop_to_bounding_box(
    image,
    offset_height,
    offset_width,
    target_height,
    target_width
)
"""

# sess = tf.Session()
#
# file_reader = tf.read_file("mifeng.png", "file_reader")
# image_decode_jpeg = tf.image.decode_jpeg(file_reader)
#
# image_crop_to_bounding_box = tf.image.crop_to_bounding_box(image_decode_jpeg, 10, 10, 1080, 1900)
#
# plt.imshow(sess.run(image_crop_to_bounding_box))

import tensorflow as tf
import matplotlib.pyplot as plt

img_name = ["mifeng.png"]
filename_queue = tf.train.string_input_producer(img_name)
img_reader = tf.WholeFileReader()
_,image_jpg = img_reader.read(filename_queue)

image_decode_jpeg = tf.image.decode_jpeg(image_jpg)
image_decode_jpeg = tf.image.convert_image_dtype(image_decode_jpeg, dtype=tf.float32)
#image_decode_jpeg = tf.expand_dims(image_decode_jpeg, 0)

sess = tf.Session()
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

# image_crop = tf.image.resize_image_with_crop_or_pad(image_decode_jpeg, 540, 960)
# image_pad = tf.image.resize_image_with_crop_or_pad(image_decode_jpeg, 720, 960)
#
# image_central_crop = tf.image.central_crop(image_decode_jpeg, 0.5)

image_crop_to_bounding_box = tf.image.crop_to_bounding_box(image_decode_jpeg, 10, 10, 100, 100)


plt.figure()
plt.subplot(224)
plt.imshow(sess.run(image_crop_to_bounding_box))
plt.title("crop image to bounding box")
plt.show()




