import numpy as np
import cv2

cap = cv2.VideoCapture(0)
return_value, image = cap.read()
cv2.imwrite('images/opencv.png', image)
del(cap)
