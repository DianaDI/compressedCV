# About this folder

This folder is what you need to train and test the scripts

## Version: 1.12.0

We will be using tensorflow's 1.12.0 version.
Please create a new envt as explained in steps below.

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

## Very important: 
Download protoc
https://github.com/protocolbuffers/protobuf/releases
[Download link for linux 64bit](https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protoc-3.10.1-linux-x86_64.zip)

unzip all of its contents into protobuf folder
Then, from within TensorFlow/models/research/
```bash
../../../protobuf/bin/protoc object_detection/protos/*.proto --python_out=.

export PYTHONPATH=$PYTHONPATH:/user/ubuntu/compressedCV/TensorFlow/models/research/object_detection
export PYTHONPATH=$PYTHONPATH:/user/ubuntu/compressedCV/TensorFlow/models/research:/user/ubuntu/compressedCV/TensorFlow/models/research/slim
```



## Testing time
cd into compressedCV/TensorFlow/models/research/object_detection/
```bash
jupyter notebook
```
In the browser, now open object_detection_tutorial ipython notebook and run all cells.
