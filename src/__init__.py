import os
from os.path import abspath, dirname

ROOT_PATH = dirname(dirname(abspath(__file__)))

# Annotations
LABELS_PATH = ROOT_PATH + f'/data/harman_360h/annotations'
LABEL_MAP_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt'

# Original data
DATA_PATH = ROOT_PATH + f'/data/harman_360h/images'
TRAIN_DATA = ROOT_PATH + f'/data/harman_360h/train'
TEST_DATA = ROOT_PATH + f'/data/harman_360h/test'

# Compression
COMPRESSION_LVL = 20

COMPRESSED_DATA_PATH = ROOT_PATH + f'/data/harman_360h/compressed' + str(COMPRESSION_LVL)
COMP_TRAIN_DATA_PATH = ROOT_PATH + f'/data/harman_360h/train_c' + str(COMPRESSION_LVL)
COMP_TEST_DATA_PATH = ROOT_PATH + f'/data/harman_360h/test_c' + str(COMPRESSION_LVL)

# TensorFlow CSV, RECORDS
CSV_TRAIN_INPUT = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/train_labels.csv'
CSV_TEST_INPUT = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/test_labels.csv'

RECORDS_OUTPUT_TRAIN_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/train_c' + str(COMPRESSION_LVL) + '.record'
RECORDS_OUTPUT_TEST_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/test_c' + str(COMPRESSION_LVL) + '.record'
