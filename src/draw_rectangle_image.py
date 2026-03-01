
from PIL import Image, ImageDraw


def create_and_draw_image():
    """Create a new RGB image and draw a rectangle on it."""
    # Create a new pink image of size 200x200
    img = Image.new("RGB", (200, 200), color="pink")

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Draw a red rectangle
    # Note: (50, 50, 50, 50) is a single point, rectangle won't be visible
    # If you want a visible rectangle, 
    # use different coordinates, e.g., (50, 50, 150, 150)
    draw.rectangle((50, 50, 150, 150), outline="red", width=10)

    # Show the image
    img.show()


if __name__ == "__main__":
    create_and_draw_image()
