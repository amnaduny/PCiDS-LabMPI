from PIL import Image
from mpi4py import MPI
import numpy as np
import time

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#start = time.time()
# Root process reads the image
if rank == 0:
    image = Image.open("result15000_12000.png")
    image_data = np.array(image)

    # Split the image data into equal portions
    split_data = np.array_split(image_data, size)

else:
    split_data = None

# Scatter the image data
start_time = time.time()
split_data = comm.scatter(split_data, root=0)
scatter_time = time.time() - start_time

# Each process opens its assigned portion of the image
partial_image = Image.fromarray(split_data)

# Perform any necessary operations on the partial image
# ...

# Gather the modified partial images from all processes
start_time = time.time()
gathered_images = comm.gather(partial_image, root=0)
gather_time = time.time() - start_time

# Root process combines the partial images
if rank == 0:
    combined_image = np.concatenate(gathered_images)
    result_image = Image.fromarray(combined_image)

    # Save or display the final image
    result_image.show()

# timing information
if rank == 0:
    print("Scatter time :", scatter_time)
    print("Gather time:", gather_time)

#end = time.time()

#elapsed_time = end - start
#print("Time : ", elapsed_time)