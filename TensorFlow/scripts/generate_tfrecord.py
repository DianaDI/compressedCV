#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:

# Create train data:
python generate_tfrecord.py --csv_input=/home/s/singla/Documents/TensorFlow/workspace/training_demo/annotations/train_labels.csv --img_path=/home/s/singla/Documents/TensorFlow/workspace/training_demo/images/train  --output_path=/home/s/singla/Documents/TensorFlow/workspace/training_demo/annotations/train.record

# Create test data:
python generate_tfrecord.py --csv_input=/home/s/singla/Documents/TensorFlow/workspace/training_demo/annotations/test_labels.csv --img_path=/home/s/singla/Documents/TensorFlow/workspace/training_demo/images/test  --output_path=/home/s/singla/Documents/TensorFlow/workspace/training_demo/annotations/test.record
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
# import tensorflow.compat.v1 as tf
import tensorflow as tf
import sys
sys.path.append("../../models/research")

from PIL import Image
import dataset_util
from collections import namedtuple, OrderedDict

# tf.disable_v2_behavior()

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('img_path', '', 'Path to images')
FLAGS = flags.FLAGS

# TO-DO replace this with label map
# for multiple labels add more else if statements
def class_text_to_int(row_label):
    if row_label == 'Pedestrian':
      return 1
    elif row_label == 'Bicycle':
      return 2
    elif row_label == 'Motorbike':
      return 3
    elif row_label == 'PassengerCar':
      return 4
    elif row_label == 'Van':
      return 5
    elif row_label == 'Truck':
      return 6
    elif row_label == 'Bus':
      return 7
    elif row_label == 'Bike_Bicycle_w/out_human':
      return 8
    elif row_label == 'Ignored':
      return 9  
    else:
        None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    # check if the image format is matching with your images.
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(os.getcwd(), FLAGS.img_path)
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
