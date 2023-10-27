#!/usr/bin/python3
# -*- coding: utf-8 -*-
from struct import unpack
import os
# Specify the directory path where "coffee.bmp" is located
directory_path = "/home/sergio/Desktop/my python tasks/working_with_files"
print(directory_path)

# Then, provide the full path to the "coffee.bmp" file separately
file_path = directory_path + "/coffee.bmp"

with open(file_path, "rb") as f:
    f.seek(18)
    width, height = unpack("ii", f.read(8))
    f.seek(2, 1)
    bpp = unpack("H", f.read(2))[0]

print("Width: ", width, "px") # Width:  256 px
print("Height: ", height, "px") # Height:  256 px
print("Color depth: ", bpp, "bpp") # Color depth:  32 bpp