# Create GIF from Images

This project provides a simple Python script to create an animated GIF from a set of images. It uses the `imageio` and `Pillow` libraries to read, resize, and combine images into a GIF file.

## Demo Images
The cat pictures (`cat1.jpg`, `cat2.jpg`, etc.) included in this project were selected randomly to showcase the functionality. You can replace them with your own images as needed.

## Features
- Reads multiple image files (JPG, PNG, etc.)
- Automatically resizes all images to match the first image's dimensions
- Creates a GIF with customizable frame duration and looping

## Requirements
- Python 3.x
- imageio
- Pillow
- numpy

## Installation
Install the required packages using pip:

```bash
pip install imageio Pillow numpy
```

## Usage
1. Place your image files in the same directory as the script.
2. Edit the `filenames` list in the script to include your image file names.
3. Run the script:

```bash
python create_gif.py
```

4. The output GIF (e.g., `team.gif` or `cats.gif`) will be saved in the same directory.

## Example
```python
import imageio.v3 as iio
import numpy as np
from PIL import Image

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

first_img = Image.open(filenames[0])
target_size = first_img.size
images.append(np.array(first_img))

for filename in filenames[1:]:
    img = Image.open(filename)
    img = img.resize(target_size, Image.LANCZOS)
    images.append(np.array(img))

iio.imwrite('team.gif', images, duration=500, loop=0)
```

## Notes
- All images must be accessible and readable by the script.
- All images will be resized to the dimensions of the first image in the list.
- The `duration` parameter sets the time (in milliseconds) each frame is displayed.
- The `loop` parameter controls how many times the GIF repeats (0 = infinite).

## License
This project is licensed under the MIT License.
