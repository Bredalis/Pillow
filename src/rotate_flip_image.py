
from PIL import Image

# Open the image
img = Image.open("../images/wonyoung.jpg")

# Rotate the image 90 degrees
img_rotated = img.rotate(90)

# Flip the image horizontally
img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

# Show the results
img_rotated.show()
img_flipped.show()
