import cv2
import numpy as np

original = cv2.imread("bridge/nm1.jpg")
duplicate = cv2.imread("bridge/nm2.jpg")

if original.shape == duplicate.shape:
    print("The images have same size and channels")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("They are not completely Equal")
		
cv2.imwrite("bridge/difference.jpg", duplicate-original)
img = cv2.imread('bridge/difference.jpg')
cv2.imshow("bridge/difference.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows()





