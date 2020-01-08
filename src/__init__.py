from os.path import abspath, dirname

ROOT_PATH = dirname(dirname(abspath(__file__)))

# Annotations
LABELS_PATH = f'/home/ubuntu/data/annotations'
LABELS_FILTERED = f'/home/ubuntu/data/data_original/annotations_filtered2'
LABEL_MAP_PATH = ROOT_PATH + f'/TensorFlow/workspace/training_demo/annotations/label_map.pbtxt'

# Original data
DATA_PATH = f'/home/ubuntu/data/data_original/images'
DATA_FILTERED = f'/home/ubuntu/data/data_original/images_filtered2'
TRAIN_DATA = f'/home/ubuntu/data/data_original/train'
TEST_DATA = f'/home/ubuntu/data/data_original/test'

# CSV PATH
OUT_TRAIN_CSV = f'/home/ubuntu/data/data_original/csv/train_labels.csv'
OUT_TEST_CSV = f'/home/ubuntu/data/data_original/csv/test_labels.csv'

# Compression
COMPRESSION_LVL = 40

COMP_TRAIN_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/train'
COMP_TEST_DATA_PATH = f'/home/ubuntu/data/images_' + str(COMPRESSION_LVL) + f'/test'

OUT_RECORDS_TRAIN_PATH = f'/home/ubuntu/data/data_original/records/train_' + str(COMPRESSION_LVL) + '.record'
OUT_RECORDS_TEST_PATH = f'/home/ubuntu/data/data_original/records/test_' + str(COMPRESSION_LVL) + '.record'
