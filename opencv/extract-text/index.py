import cv2

img = cv2.imread("tilted_book.jpg")
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# pure black and white
adaptive_threshold = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

cv2.imshow("Image", adaptive_threshold)
cv2.imwrite("improved.jpg", adaptive_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
