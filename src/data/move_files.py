import shutil, os
from tqdm import tqdm
from src import LABELS_PATH
from src.data.make_dataset import TrainValTestSplitter


def move_files(files, dest_folder):
    print("----Moving to ", dest_folder, " started----")
    for f in tqdm(files):
        shutil.move(f, dest_folder)


def separate_train_test(data, train_data, test_data):
    try:
        os.makedirs(train_data)
        os.makedirs(test_data)
    except OSError:
        pass

    # Split into train and test sets
    splitter = TrainValTestSplitter(path_to_data=data, path_to_labels=LABELS_PATH)
    data_train = splitter.data_train
    data_test = splitter.data_test

    # Separate into train and test folders
    move_files(data_train['path'], train_data)
    move_files(data_train['labels'], train_data)

    move_files(data_test['path'], test_data)
    move_files(data_test['labels'], test_data)

# if __name__ == '__main__':
#     separate_train_test(DATA_PATH)
