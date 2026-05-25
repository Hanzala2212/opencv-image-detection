import cv2

# Load Haar Cascade
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read image
img = cv2.imread("elon.jpeg")

# Convert to grayscale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = detect.detectMultiScale(grey, 1.3, 5)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

# Show image
cv2.imshow("Elon Image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()