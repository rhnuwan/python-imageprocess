import cv2
import numpy as np 
img = cv2.imread('data.jpg')
np.set_printoptions(threshold=np.nan)

lower_blue = np.array([36, 27, 237])
upper_blue = np.array([36, 27, 237])

mask = cv2.inRange(img, lower_blue, upper_blue)

size = img.shape
x= size[1]
y=size[0]

mask_val=[]

xx,yy = np.where(mask>0,)

print(xx)

res = cv2.bitwise_and(img, img, mask=mask)

ret_top = (yy[0]-5,xx[0]-5)

ret_down = (yy[len(yy)-1]+5,xx[len(xx)-1]+5)

print(ret_top)

img = cv2.rectangle(img, ret_top, (431,259), (255, 0, 0), 3)


cv2.imshow('image',img)
# cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
