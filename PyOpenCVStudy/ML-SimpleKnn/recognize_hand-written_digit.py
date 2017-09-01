'''
    使用Knn 训练识别手写数据
'''

import numpy as np
import os
from sklearn import neighbors
import matplotlib.pyplot as plt
import re
import cv2

trainingDigitsFolder = "Data2/trainingDigits"
testDataFolder = "Data2/testDigits"


#将文字图像转换成mat
def txtImg2Mat(filePath):
    imgMat = np.zeros((1,1024),np.uint)

    #图像是固定的 32 * 32 = 1024
    with open(filePath) as fs:
        for lineIndex in range(32):
            linecontent = fs.readline()
            lineCharArr = [linecontent[x] for x in range(len(linecontent) - 1)]
            imgMat[0][lineIndex * 32:(lineIndex + 1) * 32] = lineCharArr        #mat是矩阵，不管几行几列

    filesSplitArr = filePath.split('_')
    path = filesSplitArr[0].split('/')
    label = path[len(path) - 1]

    return imgMat,label

def img2GrayMat(filePath):
    mat = cv2.imread(filePath)
    mat = cv2.cvtColor(mat,cv2.COLOR_BGR2GRAY)  #直接能把三个通道BGR变成一个

    #使用LUT把颜色映射
    lookupTable = np.ones((1,256))
    lookupTable[0][255] = 0
    mat = cv2.LUT(mat,lookupTable)

    return mat



def load_files_then_initmatsandlabels(fileFolder):
    files = os.listdir(fileFolder)

    mats = np.zeros((len(files),1024))
    labels = np.zeros((len(files),1))
    
    for i in range(len(files)):
        fileFullPath = fileFolder + "/" + files[i]
        mat,label = txtImg2Mat(fileFullPath)

        mats[i] = mat
        labels[i] = label

    return mats,labels

def main():
    trainDataMats ,trainDataLabels = load_files_then_initmatsandlabels(trainingDigitsFolder)
    testDataMats,testDataLabels = load_files_then_initmatsandlabels(testDataFolder)

    knn = knntrain(trainDataMats,trainDataLabels)
    result = knnpredict(knn,testDataMats)

    #show_result_with_char(result,testDataLabels)

    imgMat3 = img2GrayMat("Imgs/handwrite_3.png") 
    imgMat6 = img2GrayMat("Imgs/handwrite_6.png") 
    imgMat1 = img2GrayMat("Imgs/handwrite_1.png") 

    oneDimMat = np.empty((1,1024))
    #writeContent = []
    #fs = open("Imgs/handwrite_3.txt",'w')
    for i in range(32):
        oneDimMat[0,i * 32:(i + 1) * 32] = imgMat6[i]

    #for i in range(32):
    #    oneDimMat[1,i * 32:(i + 1) * 32] = imgMat6[i]

    #for i in range(32):
    #    oneDimMat[2,i * 32:(i + 1) * 32] = imgMat1[i]

    #    for j in range(32):
    #       writeContent.append(str(int(imgMat[i,j])))
        
    #    writeContent.append('\n')

    #fs.writelines(writeContent)


    #mat,label = txtImg2Mat("Imgs/handwrite3_3.txt")
    #mat2,label2 = txtImg2Mat("Data2/testDigits/3_3.txt")
    ##真傻逼，每一行都得有值，所果全是0就傻逼，样本太少也傻逼
    ''' 第一个就占满了 可以正确的识别，第二个没占满，所以训练的样本应该足够多
00000011111110000000000000000000
00000001111111100000000000000000
00000000111111110000000000000000
00000000111111111110000000000000
00000000111111111111100000000000
00000000111111111111100000000000
00000000000000001111110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000111110000000000
00000000000010111111110000000000
00000000000111111111100000000000
00000000001111111111000000000000
00000000001111111110000000000000
00000000000111111111000000000000
00000000000000111111100000000000
00000000000000001111100000000000
00000000000000000111110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000111110000000000
00000011110000000111100000000000
00000111111110011111100000000000
00000011111111111111000000000000
00000001111111111111000000000000
00000000001111111100000000000000


00000000000000000000000000000000
00000000000000000000000000000000
00000000000000000000000000000000
00000000111111111110000000000000
00000000111111111111100000000000
00000000111111111111100000000000
00000000000000001111110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000111110000000000
00000000000010111111110000000000
00000000000111111111100000000000
00000000001111111111000000000000
00000000001111111110000000000000
00000000000111111111000000000000
00000000000000111111100000000000
00000000000000001111100000000000
00000000000000000111110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000011110000000000
00000000000000000111110000000000
00000011110000000111100000000000
00000111111110011111100000000000
00000011111111111111000000000000
00000001111111111111000000000000
00000000000000000000000000000000



    '''

    custom_result = knnpredict(knn,oneDimMat)
    print(custom_result)


  

def knntrain(trainDatas,trainLabels):
    #使用Knn 训练 默认k=5取周边的5个
    knn = neighbors.KNeighborsClassifier()
    knn.fit(trainDatas,trainLabels)      #两个数据结构必须一致 行数

    return knn

def knnpredict(knn,perdictData):
    result = knn.predict(perdictData)

    return result



def show_result_with_char(result,answer):
    currectNum = 0
    wrongNum = 0
    for i in  range(answer.size):
        if result[i] == answer[i][0]:
            currectNum = currectNum + 1
        else:
            wrongNum = wrongNum + 1

    #计算出正确率，用饼状图画出来
    labels = ["Currect","Wrong"]
    data = [currectNum,wrongNum]
    explode = (0.0,0.1)     #哪个突出显示，突出的范围

    plt.pie(data,labels=labels,shadow=True,explode=explode,startangle=90,autopct='%1.1f%%')     #autopct 在图上显示具体的值
    plt.axis('equal')       #图是个圆
    plt.show()



if __name__ == '__main__':
    main()
