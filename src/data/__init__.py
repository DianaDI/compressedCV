from glob import glob
from tqdm import tqdm
import os
import shutil
from os.path import basename, isfile
from src.data.move_files import copy_files
from src import LABELS_PATH, DATA_PATH, LABELS_FILTERED, DATA_FILTERED


def filter_out_odd_annotations(annotation_dir, data_dir, output_dir_xml, output_dir_data):
    try:
        os.makedirs(output_dir_xml)
        os.makedirs(output_dir_data)
    except OSError:
        pass
    cnt = 0
    for f in tqdm(glob(annotation_dir + "/*.xml")):
        xml_name = basename(f)[:-3]
        img_path = data_dir + "/" + xml_name + "bmp"
        if isfile(img_path):
            shutil.copy(f, output_dir_xml)
            shutil.copy(img_path, output_dir_data)
            cnt += 1
        else:
            print("Not found correspondence for: ", img_path)
    print(f'In total {cnt} files copied')


if __name__ == '__main__':
    filter_out_odd_annotations(LABELS_PATH, DATA_PATH, LABELS_FILTERED, DATA_FILTERED)
