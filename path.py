import cv2
import numpy as np
img = cv2.imread('path.jpg')
np.set_printoptions(threshold=np.nan)

lower_blue = np.array([0, 0, 250])
upper_blue = np.array([0, 0, 255])

mask = cv2.inRange(img, lower_blue, upper_blue)

res = cv2.bitwise_and(img, img, mask=mask)

# generate x y

mask_val = []

yy, xx = np.where(mask > 0,)

sort_xx = np.sort(xx)

print(sort_xx)

# Fiter through the x axis
# for filter in xx:
#     print(filter,"=>",np.where(xx==filter))

# res = cv2.bitwise_and(img, img, mask=mask)

for i in range(len(xx)):
    img = cv2.line(img, (xx[i], yy[i]), (xx[i], yy[i]), (0, 255, 255), 2)



# cv2.imshow('image', img)
# cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
