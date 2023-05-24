import cv2
import matplotlib.pyplot as plt
from path import Path
from htr_pipeline import read_page, DetectorConfig


# Initialize webcam
cap = cv2.VideoCapture(0)
# Capture an image when space key is pressed
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        cv2.imwrite("data/capture.png", frame)
        break


# Release webcam and close window
cap.release()
cv2.destroyAllWindows()

# Read image and detect text


for img_filename in Path("data").files("*.png"):
    print(f"Reading file {img_filename}")

    # read text
    img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    read_lines = read_page(img, DetectorConfig(height=1000))

    # output text
    for read_line in read_lines:
        print(" ".join(read_word.text for read_word in read_line))

    # plot image with detections and texts as overlay
    plt.figure(img_filename)
    plt.imshow(img, cmap="gray")
    for i, read_line in enumerate(read_lines):
        for read_word in read_line:
            bbox = read_word.bbox
            xs = [bbox.x, bbox.x, bbox.x + bbox.w, bbox.x + bbox.w, bbox.x]
            ys = [bbox.y, bbox.y + bbox.h, bbox.y + bbox.h, bbox.y, bbox.y]
            plt.plot(xs, ys, c="r" if i % 2 else "b")
            plt.text(bbox.x, bbox.y, read_word.text)

plt.show()
