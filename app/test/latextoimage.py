import matplotlib.pyplot as plt

def latex_to_image(latex_str, output_filename):
    plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
    plt.axis("off")
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.close()



# Example LaTeX expression
latex_expression = r"\left.\begin{array}{c}{(x-2)^2+1=2x-3}\\{(x^2+4-4x)+1=2x-3}\\{x^2+5-4x-2x+3=0}\\{x^2-6x+8=0}\end{array}\right."
                            
# Output filename for the image (PNG format)
output_filename = "app/test/images/latex.png"

# Convert LaTeX to image
latex_to_image(latex_expression, output_filename)


