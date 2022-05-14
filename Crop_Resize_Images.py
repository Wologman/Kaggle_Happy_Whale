# A script to crop and resize the output inference from an object detection model
# Open the CSV file with the annotations from object detection in COCO format
# Crop the images
# Resize to a square of specified dimensions

# put this file in the "code" folder, one below the project folder.  

# dest = the destination folder
# image_folder = where all the original images are stored

import os
from pathlib import Path
from PIL import Image
import pandas as pd
import numpy as np
import tqdm

project_folder = Path(__file__).resolve().parent.parent  
print('Project Folder', project_folder)

image_size = 768

image_folders = [project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'train_images', 
                project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'test_images' ]
destination_folders = [project_folder / 'data' / 'cropped_resized_768_train',
                        project_folder / 'data' / 'cropped_resized_768_test']
csv_paths = [project_folder / 'data' / 'all_train_images_768.csv',
            project_folder / 'data' / 'all_test_images_768.csv']

for dest, csv_path, image_folder in zip(destination_folders, image_folders, csv_paths):
    if not os.path.isdir(dest):
        os.makedirs(dest)

    # Go down the csv line by line.  Because then it's easy to open the file by filename.

    df = pd.read_csv (csv_path)
    df = df.reset_index()  # make sure indexes pair with number of rows

    for index, row in tqdm(df.iterrows()):

        file_name = row['filename']

        # The logic here is to do no crop if there are no objects detected
        left= 0 if np.isnan(row['xmin']) else row['xmin']
        top = 1 if np.isnan(row['ymin']) else row['ymin']
        right = 1 if np.isnan(row['xmax']) else row['xmax']
        bottom = 0 if np.isnan(row['ymax']) else row['ymax']

        img = Image.open(image_folder / file_name)
        w, h = img.size

        img = img.crop((left*w, top*h, right*w, bottom*h))
        img = img.resize((image_size, image_size),resample=3)

        img.save(dest / file_name, "JPEG")


    list = os.listdir(dest) # dir is your directory path
    number_files = len(list)
    print(number_files, 'files saved to: ', dest)