import shutil, os
from tqdm import tqdm
from src.data.make_dataset import TrainValTestSplitter


def move_files(files, dest_folder):
    print(f'----Moving to {dest_folder} started----')
    for f in tqdm(files):
        shutil.move(f, dest_folder)


def copy_files(files, dest_folder):
    print(f'---Copying to {dest_folder} started----')
    for f in tqdm(files):
        shutil.copy(f, dest_folder)


def separate_train_test(data, train_data, test_data, path_to_labels, copy=True):
    try:
        os.makedirs(train_data)
        os.makedirs(test_data)
    except OSError:
        pass

    # Split into train and test sets
    splitter = TrainValTestSplitter(path_to_data=data, path_to_labels=path_to_labels)
    data_train = splitter.data_train
    data_test = splitter.data_test

    # Separate into train and test folders
    if copy:
        print("TRAIN DATA IS BEING PROCESSED...")
        copy_files(data_train['path'], train_data)
        copy_files(data_train['labels'], train_data)
        print("TEST DATA IS BEING PROCESSED...")
        copy_files(data_test['path'], test_data)
        copy_files(data_test['labels'], test_data)
    else:
        print("TRAIN DATA IS BEING PROCESSED...")
        move_files(data_train['path'], train_data)
        move_files(data_train['labels'], train_data)
        print("TEST DATA IS BEING PROCESSED...")
        move_files(data_test['path'], test_data)
        move_files(data_test['labels'], test_data)
