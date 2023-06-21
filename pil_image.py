from PIL import Image
import time

start = time.time()
# Open the image file
image = Image.open("result1500_1200.png")

# Perform operations on the image
# ...

# Display or save the modified image
image.show()
end = time.time()

elapsed_time = end - start
print("Time : ", elapsed_time)

