from PIL import Image
from pix2tex.cli import LatexOCR


# image to latex
def image_to_latex(image_path):
    img = Image.open(image_path)
    model = LatexOCR()
    extracted_text = model(img)
    extracted_text = r"\left." + extracted_text + r"\right."
    return extracted_text


# image path
image_path = "app/test/images/test7.PNG"

# image to latex
latex_str = image_to_latex(image_path)

# print latex
print(latex_str)
