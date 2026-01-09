
from PIL import Image

img = Image.open("../IMG/Wonyoung.jpg")
img_resized = img.resize((224, 224))
img_resized.show()