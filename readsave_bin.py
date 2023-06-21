### READ .bin FILE, OPEN IT USING PIL IMAGE, AND SAVE IT ###

import os
import numpy as np
from PIL import Image
import time

current_dir = os.getcwd() # current directory
print("cd : ", current_dir)

# retrieve the list of files in the directory
file_list = os.listdir(current_dir)

# loop through the files
for file_name in file_list:
    #print("\nfile name : ", file_name)
    if file_name.endswith('.bin'):
        start = time.time()

        file_path = os.path.join(current_dir, file_name)
        print("\nfile path :", file_path)

        print('file name : ',file_name)

        # get the filename without extension
        base_filename = os.path.splitext(file_name)[0]

        # extract the desired strings
        numbers = base_filename.split('_')

        # extract individual numbers
        width = int(numbers[0].replace("infile", ""))
        height = int(numbers[1])

        print('widht :', width)
        print('height :', height)

        # read file using numpy "fromfile()"
        with open(file_path, mode='rb') as file:
            d = np.fromfile(file,dtype=np.uint8,count=width*height).reshape(height,width)

        # make into PIL image and save
        PILimage = Image.fromarray(d)
        PILimage.save('result{0}_{1}.png'.format(width, height))
        end = time.time()

        totaltime = end - start
        print("Total time : ", totaltime)