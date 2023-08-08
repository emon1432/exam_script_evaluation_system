import matplotlib.pyplot as plt

def latex_to_image(latex_str, output_filename):
    plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
    plt.axis("off")
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.close()



# Example LaTeX expression
latex_expression = r"\left.\begin{array}{c}{x^{2}+5x+6=0}\to{x^{2}+2x+3x-6=0}\\{x(x+2)+ 3 (x+2)=0}\to{(x+2)(x-3)=0}\end{array}\right."
                            
# Output filename for the image (PNG format)
output_filename = "latex_image.png"

# Convert LaTeX to image
latex_to_image(latex_expression, output_filename)


