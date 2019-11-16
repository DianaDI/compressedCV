from src.data.move_files import separate_train_test, copy_files
from TensorFlow.scripts import generate_tfrecord
from src.features.compress import Compression
from src import DATA_PATH, COMPRESSED_DATA_PATH, \
    COMP_TEST_DATA_PATH, COMP_TRAIN_DATA_PATH, \
    CSV_TEST_INPUT, CSV_TRAIN_INPUT, \
    RECORDS_OUTPUT_TEST_PATH, RECORDS_OUTPUT_TRAIN_PATH, \
    COMPRESSION_LVL, TRAIN_DATA, TEST_DATA


# SPLIT DATA
# separate_train_test(data=COMPRESSED_DATA_PATH, train_data=COMP_TRAIN_DATA_PATH, test_data=COMP_TEST_DATA_PATH)

# XML TO CSV - done only once in the beginning of project

compressor = Compression(COMPRESSION_LVL)
compressor.compress_bulk(TEST_DATA, COMP_TEST_DATA_PATH)
compressor.compress_bulk(TRAIN_DATA, COMP_TRAIN_DATA_PATH)

# move xml files
copy_files(TEST_DATA + f'/*.xml', COMP_TEST_DATA_PATH)
copy_files(TRAIN_DATA + f'/*.xml', COMP_TRAIN_DATA_PATH)

# GENERATE RECORDS
generate_tfrecord.main(CSV_TRAIN_INPUT, COMP_TRAIN_DATA_PATH, RECORDS_OUTPUT_TRAIN_PATH)
generate_tfrecord.main(CSV_TEST_INPUT, COMP_TEST_DATA_PATH, RECORDS_OUTPUT_TEST_PATH)
