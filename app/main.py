# import libraries
import cv2
import requests
from sympy import *
from sympy.printing.preview import preview
from PIL import Image
from pix2tex.cli import LatexOCR
import base64
import numpy as np



def open_camera():
    # Initialize webcam
    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('http://192.168.1.155:4747/video')

    # Capture an image when space key is pressed
    while True:
        ret, frame = cap.read()
        cv2.imshow("Image Capture", frame)
        if cv2.waitKey(1) == ord(' '):
            cv2.imwrite("app/images/captured_image.png", frame)
            break

    # Release webcam
    cap.release()
    cv2.destroyAllWindows()

    # Return captured image
    return frame    
    

def image_to_latex(image):
    #convert image to base64
    retval, buffer = cv2.imencode('.png', image)
    jpg_as_text = base64.b64encode(buffer)
    #convert base64 to string
    jpg_as_text = jpg_as_text.decode('utf-8')
    #convert string to image
    jpg_original = base64.b64decode(jpg_as_text)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    image = cv2.imdecode(jpg_as_np, flags=1)
    #save image
    cv2.imwrite("app/images/captured_image.png", image)
    #convert image to latex
    latex_str = LatexOCR().predict("app/images/captured_image.png")
    return latex_str
    



#main function
if __name__ == '__main__':
    # #step 1: open camera
    # image = open_camera()

    # #step 2: preview image
    # cv2.imshow("Captured Image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #step 3: image to latex
    image = cv2.imread("app/images/captured_image.png")
    latex_str = image_to_latex(image)
    print(latex_str)