
from PIL import Image


def image_info(path):
    """Display the image and its basic information."""
    img = Image.open(path)
    img.show()

    print("Image information:")
    print(img.info)
    print("Width and height:", img.size)
    print("Format:", img.format)
    print("Color mode:", img.mode)
    print("Color bands:", img.getbands())


def main():
    image_info("../images/ningning.jpg")
    image_info("../images/wonyoung.jpg")


if __name__ == "__main__":
    main()
