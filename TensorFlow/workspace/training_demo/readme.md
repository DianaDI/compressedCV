# Explanation:
### training: SSD MODEL
### ktraining: RESNET 101 FRCNN KITTI Model
### ftraining: Faster RCNN Model


# Steps to run FRCNN and KITTI FRCNN

This folder is what you need to train and test the scripts

## Version: 1.13.0

We will be using tensorflow's 1.13.0 version.
Please create a new envt as explained in steps below.

## It is assumed that you already have
* Anaconda installed
* tensorflow model folder BRANCH: 1.12.0
* paths specified in .bashrc file

## What you need to do new:

### Summary

Make a new environment

Download two new folders, unzip them, rename them

Make changes to those two new config files

Run training in

Commands:
```bash
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar -xzvf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
mv faster_rcnn_inception_v2_coco_2018_01_28/ faster_rcnn_inception_v2_coco/


wget http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_kitti_2018_01_28.tar.gz
tar -xzvf faster_rcnn_resnet101_kitti_2018_01_28.tar.gz
mv faster_rcnn_resnet101_kitti_2018_01_28/ kitti_faster_rcnn_resnet101/


conda create --name tfgpu2
conda activate tfgpu2
conda install tensorflow-gpu=1.13
conda install pandas pillow lxml jupyter matplotlib opencv cython
```

## Very important: NO PROTOBUF this time

## Start the training
```bash
python train.py --logtostderr --train_dir=ktraining/ --pipeline_config_path=ktraining/kpipeline.config
```

## Start the tensorboard
From the training_demo folder:
```bash
tensorboard --logdir=ktraining\
```

## Evaluation
```bash
python eval.py --logtostderr --pipeline_config_path=ktraining/kpipeline.config --checkpoint_dir=ktraining/ --eval_dir=ktraining/
```
