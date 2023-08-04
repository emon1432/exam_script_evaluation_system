from PIL import Image
from pix2tex.cli import LatexOCR

img = Image.open("latexocr/captured_image.png")
model = LatexOCR()
print(model(img))
