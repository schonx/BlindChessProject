# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:26:21 2022

@author: felix
"""

import os
import pathlib

parent_dir = pathlib.Path(__file__).parent.resolve()

try: os.makedirs(os.path.join(parent_dir, "audio_files"))
except FileExistsError: pass

try: os.makedirs(os.path.join(parent_dir, "audio_files", "coords"))
except FileExistsError: pass

def mkdir_coor(parent_dir):
    letters = ["a","b","c","d","e","f","g","h"]
    numbers = [1,2,3,4,5,6,7,8]

    for let in letters:
        for num in numbers:
            coord = ''.join([let, str(num)])
            try:
                path = os.path.join(parent_dir, "audio_files", "coords", coord)
                os.makedirs(path)
            except FileExistsError:
                pass
            
mkdir_coor(parent_dir)