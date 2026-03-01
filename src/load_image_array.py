
from PIL import Image
import numpy as np

# Open image
img = Image.open("../images/ningning.jpg")

# Convert image to numpy array
img_array = np.array(img)

# Show image
img.show()

# Print shape of the image array
print(img_array.shape)
