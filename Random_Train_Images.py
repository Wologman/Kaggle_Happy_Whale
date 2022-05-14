# This script was to select a random subset of files from a folder to do some annotations for training
# conda create -n 'yolov5' python = 3.9.1
# conda activate yolov5      

import os
import random
from pathlib import Path
from PIL import Image

project_folder = Path(__file__).resolve().parent.parent
print('Project Folder', project_folder)

image_size = 512
source = project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'train_images'
dest = project_folder / 'data' / 'resized_random_images'
if not os.path.isdir(dest):
    os.makedirs(dest)
files = os.listdir(source)
no_of_files = 2048  #len(files) // 25

for file_name in random.sample(files, no_of_files):
    #img_path = shutil.move(source / file_name, dest / file_name)
    img = Image.open(source / file_name)
    width, height = img.size
    rescale = max([width,height]) / image_size
    if rescale > 1:
        new_width = int(width//rescale)
        new_height= int(height//rescale)
        img = img.resize((new_width, new_height),resample=3)
    img.save(dest / file_name, "JPEG")