import os
from os.path import abspath, dirname

ROOT_PATH = dirname(dirname(abspath(__file__)))

# Annotations
LABELS_PATH = f'/home/ubuntu/data/annotations'
FILTERED_ANNOTATIONS = f'/home/ubuntu/data/annotations_filtered'
LABEL_MAP_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt'

# Original data
DATA_PATH = f'/home/ubuntu/data/data_original/images'
DATA_FILTERED = f'/home/ubuntu/data/data_original/images_filtered'
TRAIN_DATA = f'/home/ubuntu/data/data_original/train'
TEST_DATA = f'/home/ubuntu/data/data_original/test'

# CSV PATH
TRAIN_CSV = DATA_PATH + f'/csv/train_labels.csv'
TEST_CSV = DATA_PATH + f'/csv/test_labels.csv'

# Compression
COMPRESSION_LVL = 0

COMPRESSED_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL)
COMP_TRAIN_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/train'
COMP_TEST_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/test'

RECORDS_OUTPUT_TRAIN_PATH = DATA_PATH + f'/records/train_' + str(COMPRESSION_LVL) + '.record'
RECORDS_OUTPUT_TEST_PATH = DATA_PATH + f'/records/test_' + str(COMPRESSION_LVL) + '.record'
