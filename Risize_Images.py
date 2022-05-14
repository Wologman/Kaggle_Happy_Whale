# A script to make a new directory with a size different to the origninal one I made at max 512
# May want to look into changing this to square images, and possibly up-sizing.

# the image_folder is a folder containing image files just to get the file names to be transferred 
# source is the original folder (so to take all the files this would be the same path)
import os
from pathlib import Path
from PIL import Image
import tqdm

project_folder = Path(__file__).resolve().parent.parent
print('Project Folder', project_folder)

image_size = 768
source = project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'train_images'
image_folder = project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'train_images' 
dest = project_folder / 'data' / 'all_train_images_768'
#source = project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'test_images'
#image_folder = project_folder / 'original_data' / 'happy-whale-and-dolphin' / 'test_images' 
#dest = project_folder / 'data' / 'all_test_images_768'

if not os.path.isdir(dest):
    os.makedirs(dest)

files = os.listdir(image_folder)

for file_name in tqdm(files):
    img = Image.open(source / file_name)
    width, height = img.size
    rescale = max([width,height]) / image_size
    if rescale > 1:
        new_width = int(width//rescale)
        new_height= int(height//rescale)
        img = img.resize((new_width, new_height),resample=3)
    img.save(dest / file_name, "JPEG")

print(len(os.listdir(image_folder)), 'files processed')