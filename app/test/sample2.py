import subprocess
import sympy
from sympy.abc import *


def run_in_cmd(command):
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    result = result.stdout.decode("utf-8")
    return result


def split_result(result):
    result = result.splitlines()[-1]
    return result


def get_equation(result):
    equation = result.splitlines()[-1].split("|")[1]
    return equation


def remove_space(result):
    # remove all the spaces
    result = result.replace(" ", "")
    return result


def make_string(result):
    # make the string
    result = str(result)
    return result


def find_variable(result):
    for i in result:
        if i.isalpha():
            return i


def add_times(equation, variable):
    if variable in equation:
        if equation[equation.find(variable) - 1].isdigit():
            equation = equation.replace(variable, "*" + variable)
    return equation


def final_solve(final_equation, variable):
    result = sympy.solve(final_equation, variable)
    return result


def output(result, variable):
    # result is a list
    print("The answer of " + variable + " is: " + str(result[0]))
    print("\n")


def single_output(result):
    print("The answer is: " + result)
    print("\n")


print("\nPlease enter the expression you want to solve. (e.g. 5x-10)\n")
exp = input("Expression: ")
cmd = 'mathy simplify "' + exp + '"'

print("\nSolving...\n")
step_by_step = run_in_cmd(cmd)
print(step_by_step)

get_last_line = split_result(step_by_step)

get_equation = get_equation(get_last_line)

remove_space = remove_space(get_equation)

make_string = make_string(remove_space)

find_variable = find_variable(exp)

if find_variable:
    add_times = add_times(exp, find_variable)

    final_solve = final_solve(add_times, find_variable)

    output = output(final_solve, find_variable)
else:
    single_output = single_output(make_string)
