#!usr/bin/env python
import os
import sys
import time
os.system('./openni && ffmpeg -i *.avi -r 30 -t 2 -ss 0:00 ./demo/image-%3d.jpg')
time.sleep(2)
os.system('ffmpeg -i *.avi -r 30 -t 2 -ss 0:00 ./demo/image-%3d.jpg')
os.system('python2 tools/infer_simple.py --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml --output-dir /home/victor/detectron/detectron-visualizations --image-ext jpg --wts /home/victor/facebook/detectron-download-cache/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl demo ')
time.sleep(2)
os.system('ffmpeg -f image2 -i ./detectron-visualizations/image-%3d.jpg  -vcodec libx264 -r 10 tt.avi')
#os.system('rm *.avi')
