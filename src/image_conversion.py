
from PIL import Image


def main():
    image = Image.open("../images/wonyoung.jpg")

    # Convert image formats
    image_gray = image.convert("L")      # Grayscale

    # Show grayscale image
    image_gray.show()

    # Save image
    image_gray.save("../images/wonyoung2.png")


if __name__ == "__main__":
    main()
