
from PIL import Image

def info_imagen(url):
	img = Image.open(url)
	img.show()

	print("Información de la imagen:")
	print(img.info)
	print("Ancho y Alto:", img.size)
	print("Formato:", img.format)
	print("Escala de colores:", img.mode)
	print("Banda de color:", img.getbands())

info_imagen("../IMG/NingNing.jpg")
info_imagen("../IMG/Wonyoung.jpg")