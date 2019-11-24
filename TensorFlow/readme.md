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
wget https://github.com/tensorflow/models/tree/r1.12.0
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
../../protobuf/bin/protoc object_detection/protos/*.proto --python_out=.

export PYTHONPATH=$PYTHONPATH:/home/[user_name]/TensorFlow/models/research
export PYTHONPATH=$PYTHONPATH:/home/[user_name]/TensorFlow/models/research:/home/[user_name]/TensorFlow/models/research/slim

```



## Testing time
cd into compressedCV/TensorFlow/models/research/object_detection/
```bash
jupyter notebook
```
In the browser, now open object_detection_tutorial ipython notebook and run all cells.

If everything works, then follow the next steps:

## Creating records file:
After copying the images into test and train folder, follow the given steps
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#creating-tensorflow-records

## Download the model zoo:
SSD inception v2 coco [direct download link](http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2018_01_28.tar.gz)

[All other models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md#coco-trained-models-coco-models)
Extract its contents into training_demo/pre-trained-model (do not create folder into folder)

## Make changes to config file
The config file is located into training folder. Please make absolute address changes.

## Start the training
```bash
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_inception_v2_coco.config
```

## Start the tensorboard
From the training_demo folder:
```bash
tensorboard --logdir=training\
```

## Export inference graph
```bash
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_inception_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-532 --output_directory trained-inference-graphs/output_inference_graph_v1.pb
```
