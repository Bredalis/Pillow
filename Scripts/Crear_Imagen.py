
from PIL import Image, ImageDraw

img_nueva = Image.new("RGB", (200, 200), color = "pink")
dibujar_en_img = ImageDraw.Draw(img_nueva)
dibujar_en_img.rectangle((50, 50, 50, 50), outline = "red", width = 10)

img_nueva.show()