from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import shutil


def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)
    return graph


def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
    input_name = "file_reader"
    output_name = "normalized"

    # input_name :operation的名字
    file_reader = tf.read_file(file_name, input_name)

    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(
            file_reader, channels=3, name="png_reader")
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(
            tf.image.decode_gif(file_reader, name="gif_reader"))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
    else:
        image_reader = tf.image.decode_jpeg(
            file_reader, channels=3, name="jpeg_reader")
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)
    return result


def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label


if __name__ == "__main__":

    # PATH_TO_TEST_IMAGES_DIR = 'F:\\tmp\\test_picture'

    PATH_TO_TEST_IMAGES_DIR = 'F:\\Test\\TestA'
    # PATH_TO_TEST_IMAGES_DIR = 'F:\\Project\\Project\\YiTuClassify\\training20180423\scratches\\scratches'
    class_name = os.path.split(PATH_TO_TEST_IMAGES_DIR)[-1]
    IMAGES = os.listdir(PATH_TO_TEST_IMAGES_DIR)
    if len(IMAGES) == 0:
        tf.logging.warning('No files found')
    model_file = \
        'K:\\YiTuClassify0409\\训练结果集合\\0418-92.5%_240_8\\output_graph.pb'

    # 'F:\\Project\\Project\\YiTuClassify\\tmp\\output_graph.pb'
    graph = load_graph(model_file)
    # label_file = "F:\\Project\\Project\\YiTuClassify\\tmp\\output_labels.txt"
    label_file = "K:\\YiTuClassify0409\\训练结果集合\\0418-92.5%_240_8\\output_labels.txt"
    input_height = 299
    input_width = 299
    input_mean = 0
    input_std = 255
    input_layer = "Mul"
    output_layer = "final_result"
    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name)
    output_operation = graph.get_operation_by_name(output_name)
    list = []

    for image in IMAGES:

        TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, image)]
        print("Test_Image_Path： ",TEST_IMAGE_PATHS)
        with tf.Session(graph=graph) as sess:

            for image_path in TEST_IMAGE_PATHS:
                image = os.path.basename(image_path)
                t = read_tensor_from_image_file(
                    image_path,
                    input_height=input_height,
                    input_width=input_width,
                    input_mean=input_mean,
                    input_std=input_std)

                results = sess.run(output_operation.outputs[0], {
                    input_operation.outputs[0]: t
                })

                results = np.squeeze(results)
                top_k = results.argsort()[-1:][::-1]
                labels = load_labels(label_file)
                list_map = []
                for i in top_k:
                    # if labels[i] == class_name:
                    #     None
                    # else:
                    #     if os.path.exists(os.path.join(PATH_TO_TEST_IMAGES_DIR, labels[i])):
                    #         shutil.copy(TEST_IMAGE_PATHS, os.path.join(PATH_TO_TEST_IMAGES_DIR, labels[i]))
                    #     else:
                    #         os.makedirs(os.path.join(PATH_TO_TEST_IMAGES_DIR, labels[i]))
                    #         # TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, image)]
                    #         shutil.copy(TEST_IMAGE_PATHS, os.path.join(PATH_TO_TEST_IMAGES_DIR, labels[i]))

                    list_map.append(image)
                    list_map.append(labels[i])
                    list_map.append(results[i])
                list.append(list_map)
        df = pd.DataFrame(list)
        df.to_csv('output_csv.csv', index=False, header=False)
