import glob
import pandas as pd
from sklearn.model_selection import train_test_split


class TrainValTestSplitter:
    def __init__(self, path_to_data, path_to_labels, test_size=0.2, val=False):
        """
        Train-validation-test splitter, stores all the filenames
        :param path_to_data: path to images
        :param val: boolean, true if validation set needed to be split up
        """
        self.val = val
        path_to_data = f'{path_to_data + "/*"}'
        path_to_labels = f'{path_to_labels + "/*"}'
        self.data = pd.DataFrame()
        self.data['path'] = sorted(glob.glob(path_to_data))
        self.data['labels'] = sorted(glob.glob(path_to_labels))
        self.test_size = test_size
        self.random_state = 42
        self._split_data()

    def _split_stats(self, df):
        print(f'Size: {len(df)}')
        print(f'Percentage from original data: {len(df) / len(self.data)}')

    def _split_data(self):
        """
        Creates data_train, data_val, data_test dataframes with filenames
        """

        data_train, data_test, labels_train, labels_test = train_test_split(self.data['path'], self.data['labels'], test_size=self.test_size,
                                                                            random_state=self.random_state)
        if self.val:
            data_train, data_val, labels_train, labels_val = train_test_split(data_train, labels_train, test_size=self.test_size,
                                                                              random_state=self.random_state)

        print('=============Train subset===============')
        self.data_train = pd.DataFrame()
        self.data_train['path'] = data_train
        self.data_train['labels'] = labels_train
        self._split_stats(data_train)

        print('=============Test subset===============')
        self.data_test = pd.DataFrame()
        self.data_test['path'] = data_test
        self.data_test['labels'] = labels_test
        self._split_stats(data_test)

        if self.val:
            print('===========Validation subset============')
            self.data_val = pd.DataFrame()
            self.data_val['path'] = data_val
            self.data_val['labels'] = labels_val
            self._split_stats(data_val)
