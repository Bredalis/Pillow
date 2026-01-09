
from PIL import Image

img = Image.open("../IMG/Wonyoung.jpg")

# (izquierda, arriba, derecha, abajo)
img_recortar = img.crop((50, 50, 300, 300))
img_recortar.show()