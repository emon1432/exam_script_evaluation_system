import re
from latex2sympy2 import latex2sympy, latex2latex


def split_into_equations(s):
    #s = r"\left.\begin{array}{c}{\int _{1}^{2}\dfrac{3}{2x^{2}+x-1}dx}\\{\int _{1}^{2}\dfrac{3}{( 2x-1)(x+1)}dx}\\{\int _{1}^{2}\dfrac{2}{(2x-1)}+\dfrac{1}{(x+1)}dx}\\{\dfrac{(2\ln3)}{2}-\dfrac{(2\ln1)}{2}}\\{\ln(9/2)}\end{array}\right."

    #result = ['\int_{1}^{2}\dfrac{3}{2x^{2}+x-1}dx','\int_{1}^{2}\dfrac{3}{(2x-1)(x+1)}dx','\int_{1}^{2}\dfrac{2}{(2x-1)}+\dfrac{1}{(x+1)}dx','\dfrac{(2\ln3)}{2}-\dfrac{(2\ln1)}{2}','\ln(9/2)']

    # replace ' ' with ''   
    s = s.replace(' ','')

    # Pattern to identify the starting and ending points of each equation
    pattern = r"\\begin\{array\}\{[a-zA-Z]\}(.*?)\\end\{array\}"

    # Search for the pattern in the string
    matches = re.findall(pattern, s)
    

    # Remove leading and trailing curly braces and split equations based on '\\'
    equations = [match.strip("{}").split("\\\\") for match in matches]
    print(equations)

    # Flatten the list of equations and remove leading/trailing whitespace
    equations = [eq.strip() for sublist in equations for eq in sublist]

    # Remove first '{' or last '}'  
    equations = [eq[1:] if eq[0] == '{' else eq for eq in equations]
    equations = [eq[:-1] if eq[-1] == '}' else eq for eq in equations]
    print(equations)
    

    return equations





latex_expression = r"\left.\begin{array}{c}{\int _{1}^{2}\dfrac{3}{2x^{2}+x-1}dx}\\{\int _{1}^{2}\dfrac{3}{( 2x-1)(x+1)}dx}\\{\int _{1}^{2}\dfrac{2}{(2x-1)}+\dfrac{1}{(x+1)}dx}\\{\dfrac{(2\ln3)}{2}-\dfrac{(2\ln1)}{2}}\\{\ln(9/2)}\end{array}\right."
latex_expression = r"\left.\begin{array}{l}{x^{2}+5x+6=0}\\{x^{2}+2x+3x-6=0}\\{(x+2)(x+3)=0}\end{array}\right." #correct

equations = split_into_equations(latex_expression)
# print(equations)

for equation in equations:
    print(equation)
    print("")
    print(latex2latex(equation))

