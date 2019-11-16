import os
from os.path import abspath, dirname

ROOT_PATH = dirname(dirname(abspath(__file__)))

# Annotations
LABELS_PATH = ROOT_PATH + f'/data/harman_360h/annotations'
LABEL_MAP_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt'

# Original data
DATA_PATH = f'/home/ubuntu/data/images'
TRAIN_DATA = f'/home/ubuntu/data/images/train'
TEST_DATA = f'/home/ubuntu/data/images/test'

# Compression
COMPRESSION_LVL = 20

COMPRESSED_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL)
COMP_TRAIN_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/train'
COMP_TEST_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/test'

# TensorFlow CSV, RECORDS
CSV_TRAIN_INPUT = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/train_labels.csv'
CSV_TEST_INPUT = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/test_labels.csv'

RECORDS_OUTPUT_TRAIN_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/train_c' + str(COMPRESSION_LVL) + '.record'
RECORDS_OUTPUT_TEST_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/test_c' + str(COMPRESSION_LVL) + '.record'
