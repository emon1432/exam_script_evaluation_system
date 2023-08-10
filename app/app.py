# import libraries
import cv2
import requests
from sympy.printing.preview import preview
from PIL import Image, ImageFont, ImageDraw
from pix2tex.cli import LatexOCR
import base64
import numpy as np
from latex2sympy2 import latex2sympy, latex2latex
import re
import os
import matplotlib.pyplot as plt


def open_camera():
    # Initialize webcam
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("http://192.168.1.102:4747/video")

    # Capture an image when space key is pressed
    while True:
        ret, frame = cap.read()
        cv2.imshow("Image Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord(" "):
            # get the last file name in app/images and set the new file name
            files = os.listdir("app/images")
            new_file = ""
            # if the file does not exist, set the new file name to extracted_latex_1
            if len(files) == 0:
                new_file = "demo1"
            else:
                # get the last number in the file name and increase it by 1
                last_file = files[-1]
                last_number = int(last_file.split("demo")[-1].split(".")[0])
                new_file = "demo" + str(last_number + 1)
            cv2.imwrite("app/images/" + new_file + ".png", frame)
            break

    # Release webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

    # return the image path
    return "app/images/" + new_file + ".png"


def image_to_latex(image_path):
    # get the last file name in app/gen and set the new file name
    files = os.listdir("app/gen")
    new_file = ""
    # if the file does not exist, set the new file name to extracted_latex_1
    if len(files) == 0:
        new_file = "extracted_latex_1"
    else:
        # get the last number in the file name and increase it by 1
        last_file = files[-1]
        last_number = int(last_file.split("_")[-1].split(".")[0])
        new_file = "extracted_latex_" + str(last_number + 1)

    # print("New file name:", new_file)

    command = "mpx convert " + image_path + " app/gen/" + new_file + ".tex"
    # os.system(command)

    # clear the screen
    # os.system("cls")
    new_file = 'extracted_latex_5'

    # file_path = "app/gen/" + new_file + ".tex.zip"
    # rename the file
    # os.rename(file_path, "app/gen/" + new_file + ".tex")

    # read the file
    with open("app/gen/" + new_file + ".tex", "r") as file:
        data = file.read()

    # remove ' ' from the string
    data = data.replace(" ", "")

    # remove first '\[' and last '\]' if they exist
    if data.startswith("\["):
        data = data[2:]
    if data.endswith("\]"):
        data = data[:-2]

    # delete the file
    # os.remove("app/gen/" + new_file + ".tex")

    return data


def split_into_equations(s):
    # print(s)
    # Remove unnecessary spaces and line breaks
    s = s.replace(" ", "").replace("\n", "")

    # Pattern to identify the starting and ending points of each equation
    pattern = r"\\begin\{array\}\{[a-zA-Z]\}(.*?)\\end\{array\}"

    # Search for the pattern in the string
    matches = re.findall(pattern, s)

    # Extract the equations from the matches and split them based on '\\\\' separator
    equations = [match.split("\\\\") for match in matches]

    # Flatten the list of equations
    equations = [eq for sublist in equations for eq in sublist]

    # Remove any leading or trailing curly braces
    # equations = [eq.replace("{", "").replace("}", "").strip() for eq in equations]

    return equations


def solve_equations(latex_equations):
    sympy_equations = []
    for latex_equation in latex_equations:
        sympy_equation = latex2latex(latex_equation)
        sympy_equations.append(sympy_equation)
    return sympy_equations


def check_equations(solved_equations):
    # print(solved_equations)
    first_result = solved_equations[0]

    # check if the equations are the same
    mistake = []
    for i in range(len(solved_equations)):
        if solved_equations[i] != first_result:
            mistake.append(i + 1)
    return mistake


def show_the_mistake(mistake_line_numbers, equations):
    for i in mistake_line_numbers:
        print("Mistake in line", i)
        print("Equation:", equations[i - 1])
        print("")
    return


def output(
    splitted_equations,
    mistake_line_numbers,
    marks,
    output_filename="app/result/output.png",
):
    fig, ax = plt.subplots(figsize=(6, 4))  # Adjust the figsize as needed

    for i, equation in enumerate(splitted_equations):
        if i + 1 in mistake_line_numbers:
            color = "red"
        else:
            color = "black"

        ax.text(
            0.5,
            0.9 - i * 0.3,  # Adjust the vertical position for each line
            f"${equation}$",
            usetex=True,
            fontsize=18,
            color=color,
            horizontalalignment="center",
        )

    ax.text(
        0.5,
        0.9 - (i + 1) * 0.3,
        f"Marks = {marks}",
        usetex=True,
        fontsize=20,
        color="green",
        horizontalalignment="center",
    )
    ax.axis("off")
    plt.tight_layout()  # Ensure that the equations do not overlap
    plt.savefig(output_filename, format="png", bbox_inches="tight", pad_inches=0)
    plt.show()


# main function
if __name__ == "__main__":
    # step 1: open camera
    # image_path = open_camera()

    # step 2: check the image
    # if image_path == "":
    #     print("No image! Please try again!")
    #     exit()

    # step 3: image to latex
    # image_path = "app\images\demo1.png"
    # image_path = "app\images\demo2.png"
    # image_path = "app\images\demo3.png"
    # image_path = "app\images\demo4.png"
    # image_path = "app\images\demo5.png"
    image_path = "app\images\demo6.png"

    latex_str = image_to_latex(image_path)
    # latex_str = r"\left.\begin{array}{c}{x^{2}+5x+6=0}\\{x^{2}+2x+3x-6=0}\\{x(x+2)+3(x+2)=0}\\{(x+2)(x-3)=0}\end{array}\right."

    # step 4: split into equations
    splitted_equations = split_into_equations(latex_str)

    # step 5: solve equations
    solved_equations = solve_equations(splitted_equations)

    # step 6: check equations
    mistake_line_numbers = check_equations(solved_equations)

    # step 7: show the mistake
    marks = ""
    if len(mistake_line_numbers) == 0:
        print("\nNo mistake! Good job!")
        print("You got 10 out of 10!\n")
        marks = "10/10"
    else:
        show_the_mistake(mistake_line_numbers, splitted_equations)
        print("\n Total marks is 10. Total mistake is", len(mistake_line_numbers))
        mark = input("How many marks do you want to give? = ")
        marks = str(int(mark)) + "/10"

    # step 8: create a new image with the splitted equations and mark the mistake and show the marks
    output(splitted_equations, mistake_line_numbers, marks)
