# -*- coding: utf-8 -*-
"""
This python file is a supporting script to rename the file names
Example:
    from:   'C02032-US_20181127_090826_00850.xml'
    to:     'C02032-US_20181127_09082600850.xml'
    
Logic:
    for each file in given directory:
        remove the 25th character
"""
import os

directory = r'/home/s/singla/Documents/TensorFlow/workspace/training_demo/images/train/'

os.chdir(directory)

count = 0
for f in os.listdir(directory):
    if f.endswith('.xml'):
        if len(f) == 35:
            os.rename(f, str(f[:25] + f[26:]))
            count += 1

print(f'{count} files have been renamed.')
