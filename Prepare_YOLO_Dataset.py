# Prepare Train, Test & Val Datasets from a single YOLO 1.1 Dataset
# Useful reference: https://blog.paperspace.com/train-yolov5-custom-data/
# Delete the destination folder manually first.  Currently 'yolo_data'
# The yaml file constructor at the end may need checking.

import os
from pathlib import Path
import random
import shutil
from sklearn.model_selection import train_test_split
import yaml
random.seed(87)

project_folder = Path(__file__).resolve().parent.parent
print('Project Folder', project_folder)

data_folder = project_folder / 'data' / 'yolo_data'    #The folder being prepared for YOLO

image_folder = project_folder / 'data' / 'resized_random_images_512'    #Source for images
annot_folder = project_folder / 'data' / 'yolo1_1_happy_whale_2048_train _1_class' / 'obj_train_data' #Source for annotations

img_dest = data_folder / 'images'     # Destination for images
annot_dest = data_folder / 'labels'   # Destination for anotations

os.makedirs(img_dest)
os.makedirs(annot_dest)

annotation_files = os.listdir(annot_folder)
image_files = os.listdir(image_folder)   #If original size images preferred, re-populate this folder from the source one

image_files.sort()
annotation_files.sort()

# Split the dataset into train-valid-test splits 
train_images, val_images, train_annotations, val_annotations = train_test_split(image_files, annotation_files, test_size = 0.2, random_state = 1)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.25, random_state = 1)

directories = [img_dest / 'train', img_dest / 'val', img_dest / 'test', 
               annot_dest / 'train', annot_dest / 'val', annot_dest / 'test']

file_list = [train_images, val_images, test_images, train_annotations, val_annotations, test_annotations]

#Utility function to move images 
def copy_files_to_folder(source_folder, list_of_files,  destination_folder):
    for f in list_of_files:
        try:
            shutil.copy(source_folder / f, destination_folder)
        except:
            print(f)
            assert False

for dest in directories:
    os.makedirs(dest)

# Move the splits into their folders
copy_files_to_folder(image_folder, train_images, img_dest / 'train')
copy_files_to_folder(image_folder, val_images, img_dest / 'val')
copy_files_to_folder(image_folder, test_images, img_dest / 'test')
copy_files_to_folder(annot_folder, train_annotations, annot_dest / 'train')
copy_files_to_folder(annot_folder, val_annotations, annot_dest / 'val')
copy_files_to_folder(annot_folder, test_annotations, annot_dest / 'test')

'''
# Creating the yaml and file path text (below) is better done inside the yolo notebook,  
# or script as the file path information needs to be correct relative to the notebook.

#### Create train, val and test path data
with open(data_folder / '/train_images.txt', "w") as file:
   for path in train_images:
       file.write(path + "\n")

with open(data_folder / 'val_images.txt', "w") as file:
    for path in test_images:
        file.write(path + "\n")
        
with open(data_folder / 'test_images.txt', "w") as file:
    for path in test_images:
        file.write(path + "\n")

##### Create configuration .yml   For the destination YOLO will be run.

final_project_folder = Path('Kaggle/Happy_Whale')  # This is where the prepared data will sit when used later (eg in COLAB, Kaggle etc.)

config = {'path': 'Kaggle/Happy_Whale/',
          'train': 'Kaggle/Happy_Whale/yolo_data/images/train',
          'val': 'Kaggle/Happy_Whale/yolo_data/images/val',
          'test': 'Kaggle/Happy_Whale/yolo_data/images/test', 
          'nc': 1,
          'names': ['catacean']}

with open(data_folder / 'happy_whale.yaml', "w") as file:
    yaml.dump(config, file, default_flow_style=False)
'''