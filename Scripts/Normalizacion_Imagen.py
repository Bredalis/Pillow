
from PIL import Image
import numpy as np

img = Image.open("../IMG/Wonyoung2.png").convert("RGB")
img = img.resize((244, 244))
img_array = np.array(img) / 255.0

img.show()
print(img_array)