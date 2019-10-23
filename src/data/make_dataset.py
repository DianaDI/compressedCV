import glob
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


class TrainValTestSplitter:
    def __init__(self, path_to_data):
        """
        Train-validation-test splitter, stores all the filenames
        :param path_to_data: path to images
        """
        path_to_data = f'{path_to_data}'
        self.data = pd.DataFrame()
        self.data['path'] = glob.glob(path_to_data)
        self._split_data()

    def _split_stats(self, df):
        print(f'Size: {len(df)}')
        print(f'Percentage from original data: {len(df) / len(self.data)}')

    def _split_data(self):
        """
        Creates data_train, data_val, data_test dataframes with filenames
        """
        # train | validate test split
        splitter = GroupShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
        generator = splitter.split(self.data)
        idx_train, idx_validate_test = next(generator)

        print('=================Train subset=================')
        self.data_train = self.data.iloc[idx_train, :].reset_index(drop=True)
        self._split_stats(self.data_train)

        # validate | test split
        data_val_test = pd.concat([self.data[self.data.label == 1], self.data.iloc[self.data.iloc[idx_validate_test, :].index]])
        splitter = GroupShuffleSplit(n_splits=1, test_size=0.50, random_state=42)
        generator = splitter.split(self.data)
        idx_val, idx_test = next(generator)

        print('=============Validation subset===============')
        self.data_val = data_val_test.iloc[idx_val, :]
        self.data_val = self.data_val.sample(len(self.data_val)).reset_index(drop=True)
        self._split_stats(self.data_val)

        print('=================Test subset=================')
        self.data_test = data_val_test.iloc[idx_test, :]
        self.data_test = self.data_test.sample(len(self.data_test)).reset_index(drop=True)
        self._split_stats(self.data_test)
