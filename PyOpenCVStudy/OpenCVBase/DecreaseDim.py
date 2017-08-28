import numpy as np
import cv2
import copy

imgOrigin = cv2.imread("Res/lena.jpg")

#lookuptable 必须是个256长度的颜色表,np.arrange跟one eye zeros用法一致，赋初值
identity = np.arange(256,dtype = np.dtype('uint8'))
zeros = np.zeros(256,dtype=np.dtype('uint8'))

lookUpTable = np.dstack((identity,identity,zeros))      #dstack 抽取每一维组成新的，与zip差不多，格式不同
#afterZip = np.asarray(zip(identity,identity,zeros))



#lookUpTable = np.array([np.floor_divide(i,10) * 10 for i in range(256)])

#imgDescreseDim = np.array(imgOrigin,copy=True)

#arrTestLut = np.array([np.random.randint(0,155) for i in range(256)])
afterLut = np.zeros(imgOrigin.shape)

'''
    lut 的使用方法，其中lookuptable 256个是因为一共一通道就是256阶，而在lut(src,lookuptable) 是按颜色到表中查找到具体的值并替换
    比如lookuptable = ([0,] .... 前128个，后128[1，x])  如果原像素是 (125,s,s) 125在lookuptable对应的是0,则输出的像素就是(0,s,s) 
   上方就是把R通道全变成0 
   彩色图像，每个像素是三个维度，所以需要构建出BGR分别的lookup才能映射上
'''

#图像反转，BGR = 256 - BGR ，range [start,end)
reversePixelTable = np.array([255 - i for i in range(0,256)],dtype=np.dtype('uint8'))
lookUpTable = np.dstack((reversePixelTable,reversePixelTable,reversePixelTable))

afterLut = cv2.LUT(imgOrigin,lookUpTable)

#降维
rangePerDim = 50   #10阶为1维度
reduceDimArr = np.array([ np.floor_divide(i,rangePerDim) * rangePerDim for i in range(256)],dtype=np.dtype('uint8'))
lookUpTable = np.dstack((reduceDimArr,reduceDimArr,reduceDimArr))
afterLut = cv2.LUT(imgOrigin,lookUpTable)


cv2.imshow("orgin",imgOrigin)
cv2.imshow("reduceDim",afterLut)
cv2.waitKey()