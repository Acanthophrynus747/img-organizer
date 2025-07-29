import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

window = tk.Tk()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #clear either the linux or windows way or linux way

def sourceInput():
    global source_dir_path
    source_dir_path = filedialog.askdirectory()
    print(source_dir_path)
    return source_dir_path

def destinationInput():
    global destination_dir_path
    global dest_text
    destination_dir_path = filedialog.askdirectory()
    print(destination_dir_path)
    dest_text = destination_dir_path
    return destination_dir_path

def run():
    if 'source_dir_path' in globals() and 'destination_dir_path' in globals():
        move()
    else:
        print("Directories not selected yet")

def move():
    print(f"Moving images from {source_dir_path} to {destination_dir_path}")

    source_dir_contents = os.listdir(source_dir_path)

    num_images = len(source_dir_contents)

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
            shutil.copy2(image_path, new_folder_path)
        else:
            shutil.copy2(image_path, os.path.join(destination_dir_path, date_reformatted))

        print(f"Moved {image_file_name} to directory {date_reformatted}. ({i}/{num_images})")

    input("File organization complete. Press Enter to close.")
    clear()
    exit()
    window.destroy()

window.title("Image Organization Tool")
# root.configure(background="blue")
window.minsize(250, 250)
window.geometry("250x250+200+200")

choose_source = tk.Button(window, text = "Choose image source", command = sourceInput)
choose_source.place(x = 50, y = 50)
# choose_source.pack()

choose_destination = tk.Button(window, text = "Choose image destination", command = destinationInput)
choose_destination.place(x = 50, y = 100)
# choose_destination.pack()

run = tk.Button(window, text = "Organize", command = run)
run.place(x = 50, y = 150)

window.mainloop()



