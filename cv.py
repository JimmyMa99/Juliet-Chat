import cv2

img=cv2.imread('asserts/zly.png')
img=cv2.resize(img,(15,15))
cv2.imwrite('asserts/zly.png',img)