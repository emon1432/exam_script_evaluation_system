import cv2
import pytesseract

# Initialize webcam
cap = cv2.VideoCapture(0)

# Capture an image when space key is pressed
while True:
    ret, frame = cap.read()
    cv2.imshow("Image Capture", frame)
    if cv2.waitKey(1) == ord(' '):
        cv2.imwrite("captured_image.jpg", frame)
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()

# open the captured image
img = cv2.imread("captured_image.jpg")

# Convert image to grayscale
gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display original and grayscale images
cv2.imshow('Original Image', frame)
cv2.imshow('Grayscale Image', gray_image)

# cv2.imshow("Captured Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply thresholding to remove noise
thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Use pytesseract to convert the image to text
text = pytesseract.image_to_string(thresh)

# Print the text
print(text)