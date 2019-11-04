# TODO pipeline
# choose compression level
# save compressed images in the according folder
# divide these into train and test
# call csv to xml
# call generate records
# call appropriate train.py from tensorflow
# train
# run on test

from src.features.compress import Compression
from src import DATA_PATH, COMPRESSED_DATA_PATH, COMP_TEST_DATA_PATH, COMP_TRAIN_DATA_PATH, CSV_TEST_INPUT, CSV_TRAIN_INPUT, \
    COMPRESSION_LVL, RECORDS_OUTPUT_TEST_PATH, RECORDS_OUTPUT_TRAIN_PATH
from src.data.move_files import separate_train_test
from TensorFlow.scripts import generate_tfrecord

# COMPRESSION
compressor = Compression(COMPRESSION_LVL)
COMPRESSED_DATA_PATH = COMPRESSED_DATA_PATH + str(COMPRESSION_LVL)
compressor.compress_bulk(DATA_PATH, COMPRESSED_DATA_PATH)

# SPLIT DATA
COMP_TRAIN_DATA_PATH = COMP_TRAIN_DATA_PATH + str(COMPRESSION_LVL)
COMP_TEST_DATA_PATH = COMP_TEST_DATA_PATH + str(COMPRESSION_LVL)
separate_train_test(data=COMPRESSED_DATA_PATH, train_data=COMP_TRAIN_DATA_PATH, test_data=COMP_TEST_DATA_PATH)

# CSV TO XML  - done only once in the beginning of project

# GENERATE RECORDS
generate_tfrecord.main(CSV_TRAIN_INPUT, COMP_TRAIN_DATA_PATH, RECORDS_OUTPUT_TRAIN_PATH)
generate_tfrecord.main(CSV_TEST_INPUT, COMP_TEST_DATA_PATH, RECORDS_OUTPUT_TEST_PATH)
