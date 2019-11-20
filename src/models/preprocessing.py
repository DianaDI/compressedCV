from src.data.move_files import separate_train_test, copy_files
from TensorFlow.scripts import generate_tfrecord, xml_to_csv
from src.features.compress import Compression
from src import DATA_FILTERED, COMPRESSED_DATA_PATH, \
    COMP_TEST_DATA_PATH, COMP_TRAIN_DATA_PATH, \
    RECORDS_OUTPUT_TEST_PATH, RECORDS_OUTPUT_TRAIN_PATH, \
    COMPRESSION_LVL, TRAIN_DATA, TEST_DATA, LABELS_FILTERED, TRAIN_CSV, TEST_CSV

# Configure parameters
SPLIT = False
XML2CSV = False
COMPRESS = False

# SPLIT DATA
if SPLIT:
    separate_train_test(data=DATA_FILTERED, train_data=TRAIN_DATA, test_data=TEST_DATA, path_to_labels=LABELS_FILTERED)

# XML TO CSV - done only once for split
if XML2CSV:
    print("XML2CSV STARTED...")
    xml_to_csv.main(TRAIN_DATA, TRAIN_CSV)
    xml_to_csv.main(TEST_DATA, TEST_CSV)

if COMPRESS:
    print("COMPRESSION STARTED...")
    compressor = Compression(COMPRESSION_LVL)
    compressor.compress_bulk(TEST_DATA, COMP_TEST_DATA_PATH)
    compressor.compress_bulk(TRAIN_DATA, COMP_TRAIN_DATA_PATH)

# move xml files
# copy_files(TEST_DATA + f'/*.xml', COMP_TEST_DATA_PATH)
# copy_files(TRAIN_DATA + f'/*.xml', COMP_TRAIN_DATA_PATH)

# GENERATE RECORDS
print("GENERATING OF RECORDS STARTED...")
generate_tfrecord.main(TRAIN_CSV, TRAIN_DATA, RECORDS_OUTPUT_TRAIN_PATH)
generate_tfrecord.main(TEST_CSV, TEST_DATA, RECORDS_OUTPUT_TEST_PATH)
