from src.data.move_files import separate_train_test
from TensorFlow.scripts import generate_tfrecord, xml_to_csv
from src.features.compress import Compression
from src import DATA_FILTERED, \
    COMP_TEST_DATA_PATH, COMP_TRAIN_DATA_PATH, \
    OUT_RECORDS_TEST_PATH, OUT_RECORDS_TRAIN_PATH, \
    COMPRESSION_LVL, TRAIN_DATA, TEST_DATA, LABELS_FILTERED, OUT_TRAIN_CSV, OUT_TEST_CSV

# Configure parameters
SPLIT = False
XML2CSV = False
COMPRESS = False
TFRECORDS = True

# Split data with 10% default test size
if SPLIT:
    separate_train_test(data=DATA_FILTERED, train_data=TRAIN_DATA, test_data=TEST_DATA, path_to_labels=LABELS_FILTERED)

# XML TO CSV - done only once for split
if XML2CSV:
    xml_to_csv.main(TRAIN_DATA, OUT_TRAIN_CSV)
    xml_to_csv.main(TEST_DATA, OUT_TEST_CSV)

# Compress test and train data
if COMPRESS:
    compressor = Compression(COMPRESSION_LVL)
    compressor.compress_bulk(TRAIN_DATA, COMP_TRAIN_DATA_PATH)
    compressor.compress_bulk(TEST_DATA, COMP_TEST_DATA_PATH)

# Generate tensorflow records
if TFRECORDS:
    generate_tfrecord.main(OUT_TRAIN_CSV, COMP_TRAIN_DATA_PATH, OUT_RECORDS_TRAIN_PATH)
    generate_tfrecord.main(OUT_TEST_CSV, COMP_TEST_DATA_PATH, OUT_RECORDS_TEST_PATH)
