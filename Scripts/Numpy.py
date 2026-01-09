
from PIL import Image
import numpy as np

img = Image.open("../IMG/NingNing.jpg")
img_array = np.array(img)

img.show()
print(img_array.shape)