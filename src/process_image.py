
from PIL import Image
import numpy as np


def load_and_process_image(path, size=(244, 244)):
    """
    Open an image, resize it, convert it to RGB, 
    normalize pixel values, and display it.
    """
    img = Image.open(path).convert("RGB")
    img = img.resize(size)
    img_array = np.array(img) / 255.0

    img.show()
    print(img_array)

    return img_array


if __name__ == "__main__":
    image_array = load_and_process_image("../images/wonyoung2.png")
