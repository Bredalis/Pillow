
from PIL import Image

img = Image.open("../IMG/Wonyoung.jpg")
img_rotada = img.rotate(90)
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)

img_rotada.show()
img_flip.show()