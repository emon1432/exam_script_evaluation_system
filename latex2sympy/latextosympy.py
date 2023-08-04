from latex2sympy2 import latex2sympy, latex2latex
from sympy import *

def solve(sympy_expr):
    x = symbols('x')
    return sympy.solve(sympy_expr, x)

tex = r"\frac{d}{dx}(x^{2}+x)"
# sympy_expr = latex2sympy(tex)
# print(sympy_expr)
# print(latex2latex(tex))
#solve
sympy_expr = latex2sympy(r"\frac{d}{dx}(x^{2}+x)")
print(sympy_expr)
print(latex2latex(r"\frac{d}{dx}(x^{2}+x)"))
print(solve(sympy_expr))
