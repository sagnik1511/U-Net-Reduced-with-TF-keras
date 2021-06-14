# -*- coding: utf-8 -*-
"""
Created by @sagnik1511 (https://github.com/sagnik1511). 
All rights reserved.

After setting the images into specified folder directory,
we are going to take the images into the dataset
that will be used for training.

"""
import numpy as np
import cv2

HEIGHT = 512
WIDTH = 512

X_train = np.zeros((500,HEIGHT,WIDTH,1))
y_train = np.zeros((500,HEIGHT,WIDTH,1))
X_test = np.zeros((65,HEIGHT,WIDTH,1))

for i in range(500):
  path = os.listdir('train/images/')[i]
  img = cv2.imread('train/images/'+path)
  img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
  img = cv2.resize(img, (HEIGHT,WIDTH))
  X_train[i] = img[:,:,0].reshape(512,512,1)
  img = cv2.imread('train/masks/'+path)
  img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
  img = cv2.resize(img, (HEIGHT,WIDTH))
  y_train[i] = img[:,:,0].reshape(512,512,1)


for i in range(65):
  path = os.listdir('test/')[i]
  img = cv2.imread('test/'+path)
  img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
  img = cv2.resize(img, (HEIGHT,WIDTH))
  X_test[i] = img[:,:,0].reshape(512,512,1)
  
  
X_train /= 255.0
X_test /= 255.0
y_train /= 255.0


np.save('train_image_array.npy',X_train)
np.save('train_mask_array.npy',y_train)
np.save('test_image_array.npy',X_test)