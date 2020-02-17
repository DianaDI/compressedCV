from PIL import Image
from pathlib import Path
from glob import glob
from os.path import basename
from tqdm import tqdm
import os


class Compression:
    def __init__(self, compress_level, optimize=True, log=True, resize=False, resize_params=(0, 0)):
        """
        Init compression params
        :param compress_level: compression % (0, 100)
        :param optimize:  boolean, true flag will do an extra pass on the image to find a way
        to reduce its size as much as possible.
        :param log: boolean, prints log information
        :param resize: boolean, true if resize needed
        :param resize_params: specify if resize is true
        """
        self.compress_level = compress_level
        self.optimize = optimize
        self.resize = resize
        self.resize_params = resize_params
        self.log = log
        self.img_format = ".bmp"

    def compress(self, path, save_path):
        img = Image.open(path)
        if self.resize:
            # downsize the image with an ANTIALIAS filter (gives the highest quality)
            img = img.resize(self.resize_params, Image.ANTIALIAS)
        img.save(save_path[:-4] + '.jpg', optimize=self.optimize, quality=self.compress_level)
        img.close()

    def compress_bulk(self, data_dir, save_dir):
        try:
            os.makedirs(save_dir)
        except OSError:
            pass

        if self.log:
            print(f'COMPRESSION OF {data_dir} HAS STARTED')
            print(f'INPUT DIR SIZE: {self.get_dir_size(data_dir)}')

        for file in tqdm(glob(data_dir + "/*" + self.img_format)):
            self.compress(file, save_dir + "/" + basename(file))

        if self.log: print("COMPRESSED DIR SIZE: " + self.get_dir_size(save_dir))

    def get_dir_size(self, path):
        root_directory = Path(path)
        size = sum(f.stat().st_size for f in root_directory.glob('**/*'))
        return str(size) + " bytes"
