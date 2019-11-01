# About this folder

This folder is what you need to train and test the scripts

## Version: 1.12.0

We will be using tensorflow's 1.12.0 version.
Please create a new envt.

## What you need to pre-install

Anaconda is required
https://www.anaconda.com/distribution/#linux

This can be installed by:
```bash
bash filename.sh
```
after installation:
```bash
conda init
```

install git as well
```bash
sudo apt-get install git
```

## Setting up:

Now that you have installed anaconda and git, let's do the interesting tasks.

Git clone our repo if you haven't already
```bash
git clone https://github.com/DianaDI/compressedCV.git
cd compressedCV
cd TensorFlow
```

Download models 1.12.0 folder
```bash
git clone https://github.com/tensorflow/models/tree/r1.12.0
```
(Rename the folder as models (lowercase all))


Setup tensorflow and required files
```bash
conda create --name tfcpu tensorflow=1.12.0

conda activate tfcpu
conda install pandas
conda install pillow
conda install lxml
conda install jupyter
conda install matplotlib
conda install opencv
conda install cython
pip install pycocotools
```
