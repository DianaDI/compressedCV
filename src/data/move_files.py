import shutil, os
from tqdm import tqdm
from src import TRAIN_DATA, TEST_DATA, DATA_PATH, LABELS_PATH
from src.data.make_dataset import TrainValTestSplitter


def move_files(files, dest_folder):
    for f in tqdm(files):
        shutil.move(f, dest_folder)


if __name__ == '__main__':
    try:
        os.makedirs(TRAIN_DATA)
        os.makedirs(TEST_DATA)
    except OSError:
        pass

    # Split into train and test sets
    splitter = TrainValTestSplitter(path_to_data=DATA_PATH, path_to_labels=LABELS_PATH)
    data_train = splitter.data_train
    data_test = splitter.data_test

    # Separate into train and test folders
    move_files(data_train['path'], TRAIN_DATA)
    move_files(data_train['labels'], TRAIN_DATA)

    move_files(data_test['path'], TEST_DATA)
    move_files(data_test['labels'], TEST_DATA)
