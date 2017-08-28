import cv2
import numpy as np

mat = cv2.imread("Res/lena.jpg")


#在C++的版本中使用的是Mat::zeros 这里使用Numpy提供
mat2 = np.zeros((2,3),dtype=np.uint8)   #2X3 全0矩阵

mat3 = np.eye(2,3,dtype=np.double)  #对角矩阵

mat4 = np.ones(2,3,dtype=float) #都是1

print(mat4)

cv2.imshow("sss",mat2)
cv2.waitKey(0)