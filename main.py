import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Unable to open camera")

# Capture a frame
ret, frame = cap.read()

# Display the captured frame
cv2.imshow('frame', frame)

# Save the captured frame as an image
cv2.imwrite('captured_image.jpg', frame)

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()