from PIL import Image
from pix2tex.cli import LatexOCR
import matplotlib.pyplot as plt


def latex_to_image(latex_str, output_filename):
    plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
    plt.axis("off")
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.close()


img = Image.open("images/latex_image.png")
model = LatexOCR()

# Extract text from image
extracted_text = model(img)

#print extracted text
print(extracted_text)

# Convert LaTeX to image
latex_to_image(extracted_text, "latex_image.png")

# Display image
img = Image.open("latex_image.png")
img.show()
