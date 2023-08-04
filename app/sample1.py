# import libraries
from latex2sympy2 import latex2sympy, latex2latex
from sympy import *


def check_equations(solved_equations, equations):
    # print(solved_equations)
    first_result = solved_equations[0]

    # check if the equations are the same
    for i in range(len(solved_equations)):
        if solved_equations[i] != first_result:
            print("You have a mistake in line ", i + 1, "!")
            print("The line is ")
            print(equations[i])
            return False
    print("No mistakes!")



def solve_equations(latex_equations):
    # convert latex to sympy
    sympy_equations = []
    for latex_equation in latex_equations:
        sympy_equation = latex2sympy(latex_equation)
        sympy_equations.append(sympy_equation)
    return sympy_equations


# testing
equations = ["x^2+5x+6=0", "x^2+2x+3x-6=0", "(x+2)(x+3)=0"]
solved_equations = solve_equations(equations)
# print(solved_equations)
check_equations(solved_equations, equations)
