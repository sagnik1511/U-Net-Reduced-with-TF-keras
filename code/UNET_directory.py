# -*- coding: utf-8 -*-



""""
Created by @sagnik1511 (https://github.com/sagnik1511). 
All rights reserved.

We are taking the data from a specified folder sequence 
to a usable directory tree format.


"""
import os
import numpy as np
import shutil as sh
import UNET_utils
train_root = 'train_images/'
test_root = 'test_images/'

train_img_dir = []
test_img_dir = []
train_mask_dir = []

for i in os.listdir(train_root):
  train_img_dir.append(train_root+str(i)+'/'+'images/'+str(i)+'.png')
  train_mask_dir.append(train_root+str(i)+'/'+'masks/'+str(i)+'.png')
for i in os.listdir(test_root):
  test_img_dir.append(test_root+str(i)+'/'+str(i)+'.png')

change_dir( train_img_dir ,'/content/train/images/' )
change_dir( train_mask_dir ,'/content/train/masks/' )
change_dir( test_img_dir ,'/content/test/' )

