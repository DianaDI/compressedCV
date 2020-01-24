from src.data.move_files import separate_train_test
from TensorFlow.scripts import generate_tfrecord, xml_to_csv
from src.features.compress import Compression
from src.features.grayscale import rgb2gray
from src import DATA_FILTERED, \
    COMP_TEST_DATA_PATH, COMP_TRAIN_DATA_PATH, \
    OUT_RECORDS_TEST_PATH, OUT_RECORDS_TRAIN_PATH, \
    COMPRESSION_LVL, TRAIN_DATA, TEST_DATA, LABELS_FILTERED, \
    OUT_TRAIN_CSV, OUT_TEST_CSV, \
    TRAIN_DATA_G, TEST_DATA_G, \
    COMP_TEST_DATA_PATH_G, COMP_TRAIN_DATA_PATH_G, \
    OUT_RECORDS_TRAIN_PATH_G, OUT_RECORDS_TEST_PATH_G, \
    OUT_TRAIN_CSV_JPG, OUT_TEST_CSV_JPG

# Configure parameters
SPLIT = False
XML2CSV = False
MAKEGRAY = False
COMPRESS = False
TFRECORDS = True
ISGRAY = True
ISJPG = True

# Split data with 10% default test size
if SPLIT:
    separate_train_test(data=DATA_FILTERED, train_data=TRAIN_DATA, test_data=TEST_DATA, path_to_labels=LABELS_FILTERED)

# Make gray scale
if MAKEGRAY:
    rgb2gray(TRAIN_DATA, TRAIN_DATA_G)
    rgb2gray(TEST_DATA, TEST_DATA_G)
    ISGRAY = True

# XML TO CSV - done only once for split
if XML2CSV:
    xml_to_csv.main(TRAIN_DATA, OUT_TRAIN_CSV_JPG if ISJPG else OUT_TRAIN_CSV)
    xml_to_csv.main(TEST_DATA, OUT_TEST_CSV_JPG if ISJPG else OUT_TEST_CSV)

# Compress test and train data
if COMPRESS:
    compressor = Compression(COMPRESSION_LVL)

    compressor.compress_bulk(TRAIN_DATA if not ISGRAY else TRAIN_DATA_G,
                             COMP_TRAIN_DATA_PATH if not ISGRAY else COMP_TRAIN_DATA_PATH_G)

    compressor.compress_bulk(TEST_DATA if not ISGRAY else TEST_DATA_G,
                             COMP_TEST_DATA_PATH if not ISGRAY else COMP_TEST_DATA_PATH_G)

# Generate tensorflow records
if TFRECORDS:
    generate_tfrecord.main(OUT_TRAIN_CSV_JPG if ISJPG else OUT_TRAIN_CSV,
                           COMP_TRAIN_DATA_PATH if not ISGRAY else COMP_TRAIN_DATA_PATH_G,
                           OUT_RECORDS_TRAIN_PATH if not ISGRAY else OUT_RECORDS_TRAIN_PATH_G)

    generate_tfrecord.main(OUT_TEST_CSV_JPG if ISJPG else OUT_TEST_CSV,
                           COMP_TEST_DATA_PATH if not ISGRAY else COMP_TEST_DATA_PATH_G,
                           OUT_RECORDS_TEST_PATH if not ISGRAY else OUT_RECORDS_TEST_PATH_G)
