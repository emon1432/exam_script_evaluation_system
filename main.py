import cv2

# Initialize webcam
cap = cv2.VideoCapture('http://192.168.1.155:4747/video')

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
cv2.imshow("Captured Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()