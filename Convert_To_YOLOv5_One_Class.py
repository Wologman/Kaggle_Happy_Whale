# I made the annotations using CVAT with 3 classes.  Left, Right, Unknown
# Writing a script to convert the format to 1 class.
# Manually changed obj.names to just cetatean (from left, right, unknown)
# manually changed obj.data to just 1 class

import os
from pathlib import Path

folder_name = 'data/yolo1_1_happy_whale_2048_train _1_class/obj_train_data'

project_folder = Path(__file__).resolve().parent.parent
print('Project Folder', project_folder)

data_folder = project_folder / folder_name
files =  os.listdir(data_folder)

for file_name in files:
    with open(data_folder / file_name, 'r+', encoding='utf-8') as f:   #w+ deletes the content on open!
        lines = f.readlines()  # returning and empty string!  Why?
        f.truncate(0)
        f.seek(0)   #Needed to step back the cursor to the top I think, prevents invalid char
        for line in lines:
            newline = line[:0] + '0' + line[1:]
            f.write(newline)
        f.close