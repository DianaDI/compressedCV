from PIL import Image
from glob import glob
import os
from os.path import basename
from tqdm import tqdm


def rgb2gray(data_dir, save_dir, img_format=".bmp"):
    """
    Convert rgb image to gray scale. Filters out images in input dir by img format
    :param data_dir: input dir
    :param save_dir:
    :param img_format:
    """
    print(f'DATA FOLDER {data_dir} CONVERTING TO GRAYSCALE STARTING')
    try:
        os.makedirs(save_dir)
    except OSError:
        pass
    for file in tqdm(glob(data_dir + "/*" + img_format)):
        gray_img = Image.open(file).convert('L')
        gray_img.save(save_dir + "/" + basename(file))
        gray_img.close()
