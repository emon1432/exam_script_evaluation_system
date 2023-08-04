# import libraries
from latex2sympy2 import latex2sympy, latex2latex
from sympy import *
import re

def split_into_equations(s):
    # print(s)
    # Remove unnecessary spaces and line breaks
    s = s.replace(" ", "").replace("\n", "")

    # Pattern to identify the starting and ending points of each equation
    pattern = r"\\begin\{array\}\{l\}(.*?)\\end\{array\}"

    # Search for the pattern in the string
    matches = re.findall(pattern, s)

    # Extract the equations from the matches and split them based on '\\\\' separator
    equations = [match.split("\\\\") for match in matches]

    # Flatten the list of equations
    equations = [eq for sublist in equations for eq in sublist]

    # Remove any leading or trailing curly braces
    equations = [eq.replace("{", "").replace("}", "").strip() for eq in equations]

    return equations

def solve_equations(latex_equations):
    # convert latex to sympy
    sympy_equations = []
    for latex_equation in latex_equations:
        sympy_equation = latex2sympy(latex_equation)
        sympy_equations.append(sympy_equation)
    return sympy_equations

def check_equations(solved_equations):
    # print(solved_equations)
    first_result = solved_equations[0]

    # check if the equations are the same
    mistake = []
    for i in range(len(solved_equations)):
        if solved_equations[i] != first_result:
            mistake.append(i+1)
    return mistake

def show_the_mistake(mistake_line_numbers, equations):
    for i in mistake_line_numbers:
        print("Mistake in line", i)
        print("Equation:", equations[i-1])
        print("")
    return

# testing
latex_str = r"\left.\begin{array}{l}{x^{2}+5x+6=0}\\{x^{2}+2x+3x-6=0}\\{(x+2)(x-3)=0}\end{array}\right." #wrong
# latex_str = r"\left.\begin{array}{l}{x^{2}+5x+6=0}\\{x^{2}+2x+3x+6=0}\\{(x+2)(x+3)=0}\end{array}\right." #correct
splited_equations = split_into_equations(latex_str)
# print(splited_equations)

# splited_equations = ["x^2+5x+6=0", "x^2+2x+3x-6=0", "(x+2)(x+3)=0"]
solved_equations = solve_equations(splited_equations)
# print(solved_equations)
mistake_line_numbers = check_equations(solved_equations)

#where the mistake
if len(mistake_line_numbers) == 0:
    print("No mistake! Good job!")
else:
    show_the_mistake(mistake_line_numbers, splited_equations)

