import matplotlib.pyplot as plt

def latex_to_image(latex_str, output_filename):
    plt.text(0.5, 0.5, f"${latex_str}$", usetex=True, fontsize=18)
    plt.axis("off")
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.close()


def main():
    # Example LaTeX expression
    latex_expression = r"{4x^{3}+\\int_{0}^{x}x^{2}dx}\\\\{4x^{3}+3x^{3}}\\\\{7x^{3}}"
                               
    # Output filename for the image (PNG format)
    output_filename = "latex_image.png"

    # Convert LaTeX to image
    latex_to_image(latex_expression, output_filename)


if __name__ == "__main__":
    main()
