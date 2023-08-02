import cv2
import requests
import sympy
from sympy.printing.preview import preview
from PIL import Image


# Step 1: Open Camera
# def open_camera():
#     # Initialize webcam
#     # cap = cv2.VideoCapture(0)
#     cap = cv2.VideoCapture("http://192.168.1.100:4747/video")

#     # Capture an image when space key is pressed
#     while True:
#         ret, frame = cap.read()
#         cv2.imshow("Image Capture", frame)
#         if cv2.waitKey(1) == ord(" "):
#             cv2.imwrite("captured_image.png", frame)
#             break

#     # Release webcam
#     cap.release()
#     cv2.destroyAllWindows()

#     # Return captured image
#     return frame








def main():
    # Step 1: Open Camera
    # image = open_camera()

    # # Step 2: Save Image
    # image_path = "images/captured_image.png"
    # cv2.imwrite(image_path, image)


    # Sample LaTeX string representing (a+b)^2 = a^2 + 2ab + b^2
    latex_str = r"\left(a + b\right)^{2} = a^{2} + 2 a b + b^{2}"

    


if __name__ == "__main__":
    main()
