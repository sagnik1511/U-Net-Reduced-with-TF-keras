# -*- coding: utf-8 -*-
"""
Created by @sagnik1511 (https://github.com/sagnik1511). 
All rights reserved.


All useful functions of this project are in this folder.

"""
import shutil as sh


def change_dir(folder,directory):
  for i in folder:
    sh.copy2(i,directory)