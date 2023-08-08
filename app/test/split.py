import re
from latex2sympy2 import latex2sympy, latex2latex


def split_into_equations(input_str):
    print(input_str)
    # Remove unnecessary spaces and line breaks
    input_str = input_str.replace(" ", "").replace("\n", "")

    # Pattern to identify the starting and ending points of each equation
    pattern = r"\\begin\{array\}\{c\}\{(.*?)\\end\{array\}"

    # Search for the pattern in the string
    matches = re.findall(pattern, input_str)

    # Extract the equations from the matches and split them based on '\\\\' separator
    


        

    return matches







# latex_expression = r"\left.\begin{array}{c}{\int _{1}^{2}\dfrac{3}{2x^{2}+x-1}dx}\\{\int _{1}^{2}\dfrac{3}{( 2x-1)(x+1)}dx}\\{\int _{1}^{2}\dfrac{2}{(2x-1)}+\dfrac{1}{(x+1)}dx}\\{\dfrac{(2\ln3)}{2}-\dfrac{(2\ln1)}{2}}\\{\ln(9/2)}\end{array}\right."
# latex_expression = r"\left.\begin{array}{l}{x^{2}+5x+6=0}\\{x^{2}+2x+3x-6=0}\\{(x+2)(x+3)=0}\end{array}\right." #correct

latex_expression = r"\left.\begin{array}{c}{{x^{2}+5x+6=0\rightarrow x^{2}+2x+3x-6=0}}\\ {{x(x+2)+3(x+2)=0\rightarrow(x+2)(x-3)=0}}\end{array}\right."

equations = split_into_equations(latex_expression)
print(equations)

# for equation in equations:
#     print(equation)
#     print("")
#     print(latex2latex(equation))
