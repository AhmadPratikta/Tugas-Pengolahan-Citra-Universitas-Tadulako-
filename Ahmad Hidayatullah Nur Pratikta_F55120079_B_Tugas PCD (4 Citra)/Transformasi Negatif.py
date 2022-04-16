import cv2

img = cv2.imread('mammogram.tif', 0)
img_resize = cv2.resize(img, (700,500))

img_1 = 255 - img_resize

cv2.imshow("Original Image", img_resize)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()