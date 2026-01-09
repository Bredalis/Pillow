
from PIL import Image

img = Image.open("../IMG/Wonyoung.jpg")
img_gray = img.convert("L") # Escala de grises
img_rgb = img.convert("RGB") # RGB

img_gray.show()

# Guardar imagen
img_gray.save("../IMG/Wonyoung2.png")