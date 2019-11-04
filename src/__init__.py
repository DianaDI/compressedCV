LABEL_MAP_PATH = f'../workspace/training_demo/annotations/label_map.pbtxt'

DATA_PATH = f'../../data/harman_360h/images'
TRAIN_DATA = f'../../data/harman_360h/train'
TEST_DATA = f'../../data/harman_360h/test'

COMPRESSED_DATA_PATH = f'../../data/harman_360h/compressed'
COMP_TRAIN_DATA_PATH = f'../../data/harman_360h/train_c'
COMP_TEST_DATA_PATH = f'../../data/harman_360h/test_c'

COMPRESSION_LVL = 0.2
RECORDS_OUTPUT_TRAIN_PATH = f'../workspace/training_demo/annotations/train_c' + str(COMPRESSION_LVL) + '.record'
RECORDS_OUTPUT_TEST_PATH = f'../workspace/training_demo/annotations/test_c' + str(COMPRESSION_LVL) + '.record'

LABELS_PATH = f'../../data/harman_360h/annotations'

# TensorFlow CSV, RECORDS
CSV_TRAIN_INPUT = f'../../data/harman_360h/annotations/train_labels.csv'
CSV_TEST_INPUT = f'../../data/harman_360h/annotations/test_labels.csv'
