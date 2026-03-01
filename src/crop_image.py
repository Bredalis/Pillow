
from PIL import Image


def crop_image(path, crop_box):
    """
    Open an image and crop it.
    
    Parameters:
    - path: str, path to the image file
    - crop_box: tuple of 4 ints, (left, top, right, bottom)
    
    Returns:
    - cropped Image object
    """
    img = Image.open(path)
    cropped_img = img.crop(crop_box)
    cropped_img.show()
    return cropped_img


if __name__ == "__main__":
    # Define path and crop box
    image_path = "../images/wonyoung.jpg"
    box = (50, 50, 300, 300)  # (left, top, right, bottom)
    
    # Crop and display the image
    crop_image(image_path, box)
