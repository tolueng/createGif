
# To use the imageio library, you need to install it first. You can do this using pip:
# pip install imageio
# Also install Pillow for image resizing: pip install Pillow
# Import required libraries
import imageio.v3 as iio  # For reading and writing images/GIFs
import numpy as np        # For handling image data as arrays
from PIL import Image     # For opening and resizing images

# List of image file names to include in the GIF
fileNames = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cat4.jpg', 'cat5.jpg']

# This list will store the image data (as numpy arrays)
images = []

# Open the first image to determine the target size for all images
first_img = Image.open(fileNames[0])
target_size = first_img.size  # (width, height)

# Add the first image (converted to numpy array) to the images list
images.append(np.array(first_img))

# Loop through the rest of the images
for fileName in fileNames[1:]:
    img = Image.open(fileName)              # Open image
    img = img.resize(target_size, Image.LANCZOS)  # Resize to match first image
    img_array = np.array(img)               # Convert to numpy array
    images.append(img_array)                # Add to list

# Save all images as a GIF
# duration=500 means each frame lasts 500ms; loop=0 means infinite loop
iio.imwrite('cats.gif', images, duration=500, loop=0)