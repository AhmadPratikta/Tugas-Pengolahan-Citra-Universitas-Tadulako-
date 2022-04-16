import cv2

img = cv2.imread('epic.jpg', 1)
resize = cv2.resize(img, (700,500))
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Original", resize)
cv2.imshow("Gambar Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()