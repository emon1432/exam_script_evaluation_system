from pix2tex.cli import LatexOCR
import matplotlib.pyplot as plt
from PIL import Image


def latex_to_image(latex_str, output_filename):
    plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
    plt.axis("off")
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.close()


img = Image.open("app/images/correct.png")
model = LatexOCR()


extracted_text = model(img)

print(extracted_text)