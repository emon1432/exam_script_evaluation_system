import cv2
import pytesseract

# Initialize webcam
cap = cv2.VideoCapture(0)

# Capture an image when space key is pressed
while True:
    ret, frame = cap.read()
    cv2.imshow("Image Capture", frame)
    if cv2.waitKey(1) == ord(' '):
        cv2.imwrite("captured_image1.jpg", frame)
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()

# Read the image
img = cv2.imread('captured_image1.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pre-process the image to remove noise and smooth it
gray = cv2.medianBlur(gray, 3)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Perform OCR using Tesseract
text = pytesseract.image_to_string(gray, lang='eng')

# Print the extracted text
print(text)
