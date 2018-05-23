#!usr/bin/env python
import os
import sys
import time
os.system('./openni')
time.sleep(5)
os.system('ffmpeg -i *.avi -r 30 ./demo/image-%4d.jpg')
time.sleep(2)
os.system('python2 tools/infer_simple.py --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml --output-dir /home/victor/detectron/detectron-visualizations --image-ext jpg --wts /home/victor/facebook/detectron-download-cache/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl demo ')
time.sleep(2)
os.system('ffmpeg -f image2 -i ./detectron-visualizations/image-%4d.jpg  -vcodec libx264 -r 30 ./output/test.avi')
os.system('rm 2018*.avi ./demo/*.jpg ./detectron-visualizations/*.jpg')
os.system('cp ./output/test.avi ./output/1.avi')
os.system('rm ./output/test.avi')
os.system('g++ video.cpp -o video `pkg-config --cflags --libs opencv` ')
time.sleep(2)
os.system('./video')
