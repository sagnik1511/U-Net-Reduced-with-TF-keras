# U-Net-Lowered-with-keras
Complete U-net Implementation with keras

<img align="left" width="80px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/165px-Python-logo-notext.svg.png"/><img align="left" width="120px" src="https://colab.research.google.com/img/colab_favicon_256px.png"/><img align="left" width="80px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/173px-Tensorflow_logo.svg.png"/><img align="left" width="80px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/768px-Keras_logo.svg.png"/><br><br><br><br><br>




## Original Paper Link : [https://arxiv.org/abs/1505.04597](https://arxiv.org/abs/1505.04597)

## Special Implementations :
---

The model is implemeted using the original paper. But I have changed the filter size of the layers.
The implemented layers are reduced to 25% of the original paper.

## Original Model Architecture :

![](https://github.com/sagnik1511/U-Net-Lowered-wiith-keras/blob/main/images/u-net-architecture.png)

## Dataset :
---
   The dataset has been taken from kaggle . It had a spefici directory shape, but it was tough to execute dataset building from it, so prepared an usable dataset.
   #### Link :  [https://www.kaggle.com/azkihimmawan/chest-xray-masks-and-defect-detection](https://www.kaggle.com/azkihimmawan/chest-xray-masks-and-defect-detection)
   #### Primary Directory Tree :
   
    .
    └── root/
        ├── train_images/
        │   └── id/
        │       ├── images/
        │       │   └── id.png
        │       └── masks/
        │           └── id.png
        └── test_images/
            └── id/
                └── id.png
                
   #### Given Images :
   
   | Image | Mask |
   |-|-|
   | <img align="center" width="1280px" src="https://github.com/sagnik1511/U-Net-Lowered-wiith-keras/blob/main/images/00071198d059ba7f5914a526d124d28e6d010c92466da21d4a04cd5413362552_image.png"/> | <img align="center" width="1280px" src="https://github.com/sagnik1511/U-Net-Lowered-wiith-keras/blob/main/images/00071198d059ba7f5914a526d124d28e6d010c92466da21d4a04cd5413362552_mask.png"/> |
   
## Supporting Libraries :

| Numpy | opencv | Matplotlib |
|-|-|-|
| <img align="center" width="80px" src="https://numpy.org/images/logos/numpy.svg"/> | <img align="left" width="80px" src="https://quintagroup.com/cms/python/images/opencv-logo.png/@@images/45c400ef-455a-40a1-93b3-5f0c6a81e746.png"/> | <img align="center" width="70px" src="https://matplotlib.org/stable/_images/sphx_glr_logos2_001.png"/> |


## Dataset Directory Generation :
---

We have performed operations  to ceate the data directory like this :

                  .
                  └── root/
                      ├── train/
                      │   ├── images/
                      │   │   └── id.png
                      │   └── masks/
                      │       └── id.png
                      └── test/
                          └── id.png

