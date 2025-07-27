'''
https://www.python-engineer.com/posts/file-organization/


shutil.copy('source', 'destination')  # new metatags
shutil.copy2('source', 'destination')  # copies metadata, too

os.remove("filename")  # error if not found
os.rmdir("folder")  # error if not empty, or not found
shutil.rmtree("folder")  # works for non empty directories

input folder of images, 102Canon
output images in folders by date

enter file path to image folder
enter path to destination

https://stackoverflow.com/questions/48631908/python-extract-metadata-from-png/62456315#62456315

https://www.geeksforgeeks.org/python/how-to-get-file-creation-and-modification-date-or-time-in-python/

https://www.geeksforgeeks.org/python/how-to-extract-image-metadata-in-python/
'''

from PIL import Image
from PIL.ExifTags import TAGS
import os
import time
import tkinter as tk
from tkinter import filedialog
import shutil

root = tk.Tk()
root.withdraw()

source_dir_path = filedialog.askdirectory()
print(source_dir_path)

destination_dir_path = filedialog.askdirectory()
print(destination_dir_path)

source_dir_contents = os.listdir(source_dir_path)

# print(source_dir_contents)

for i in range(len(source_dir_contents)):
    image_file_name = source_dir_contents[i]
    image_path = os.path.join(source_dir_path, image_file_name)
    # print(image_path)

    image = Image.open(image_path)
    image.load()
    # print(image)

    exifdata = image.getexif()

    date_time = exifdata.get(306)
    split_date_time = date_time.split()
    date = split_date_time[0]

    date_reformatted = date.replace(":", "-")

    destination_dir_contents = os.listdir(destination_dir_path)

    if date_reformatted not in destination_dir_contents:
        new_folder_path = os.path.join(destination_dir_path, date_reformatted)
        print(f"Creating directory {date_reformatted} in {destination_dir_path}")
        os.mkdir(new_folder_path)
        print(f"Moving {image_file_name} to directory {date_reformatted}")
        shutil.copy2(image_path, new_folder_path)
    else:
        shutil.copy2(image_path, os.path.join(destination_dir_path, date_reformatted))
        print(f"Moving {image_file_name} to directory {date_reformatted}")



    
# for tag_id in exifdata:

#     tag_name = TAGS.get(tag_id, tag_id)

#     value = exifdata.get(tag_id)

    

#     print(f"{tag_id}: {tag_name}: {value}")
# print(img.info)

# last modified might be the one to use for images, fresh off the card created would work too probably
