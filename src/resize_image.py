
from PIL import Image

img = Image.open("../images/wonyoung.jpg")
img_resized = img.resize((224, 224))
img_resized.show()
