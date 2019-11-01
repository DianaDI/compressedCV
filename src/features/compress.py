from PIL import Image
from glob import glob
from os.path import basename
import os


class Compression:
    def __init__(self, compress_level, optimize, resize=False, resize_params=(0, 0)):
        """
        Init compression params
        :param compress_level: compression % (0, 100)
        :param optimize:  boolean, true flag will do an extra pass on the image to find a way
        to reduce its size as much as possible.
        :param resize: boolean, true if resize needed
        :param resize_params: specify if resize is true
        """
        self.compress_level = compress_level
        self.optimize = optimize
        self.resize = resize
        self.resize_params = resize_params

    def compress(self, path, save_path):
        img = Image.open(path)
        if self.resize:
            # downsize the image with an ANTIALIAS filter (gives the highest quality)
            img = img.resize(self.resize_params, Image.ANTIALIAS)
        img.save(save_path, optimize=self.optimize, quality=self.compress_level)

    def compress_bulk(self, data_dir, save_dir):
        try:
            os.makedirs(save_dir)
        except OSError:
            pass
        for file in glob(data_dir + "/*"):
            self.compress(file, save_dir + "/" + basename(file))

# Example run
# compressor = Compression(10, True)
# compressor.compress_bulk("../../data/test data", "../../data/compressed")
