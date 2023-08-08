# import matplotlib.pyplot as plt

# def latex_to_image(latex_str, output_filename):
#     plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
#     plt.axis("off")
#     plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
#     plt.close()


# def main():
#     # Example LaTeX expression
#     latex_expression = r"\left.\begin{array}{c}{\int _{1}^{2}\dfrac{3}{2x^{2}+x-1}dx}\\{\int _{1}^{2}\dfrac{3}{( 2x-1)(x+1)}dx}\\{\int _{1}^{2}\dfrac{2}{(2x-1)}+\dfrac{1}{(x+1)}dx}\\{\dfrac{(2\ln3)}{2}-\dfrac{(2\ln1)}{2}}\\{\ln(9/2)}\end{array}\right."
                               
#     # Output filename for the image (PNG format)
#     output_filename = "latex_image.png"

#     # Convert LaTeX to image
#     latex_to_image(latex_expression, output_filename)


# if __name__ == "__main__":
#     main()
import requests
import numpy as np
from latex2sympy2 import latex2sympy, latex2latex

print(latex2latex('\int_{1}^{2}\dfrac{3}{2x^{2}+x-1}dx'))