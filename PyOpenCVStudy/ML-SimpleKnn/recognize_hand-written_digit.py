'''
    使用Knn 训练识别手写数据
'''

import numpy as np
import os
from sklearn import neighbors
import matplotlib.pyplot as plt
import re

trainingDigitsFolder = "Data2/trainingDigits"
testDataFolder = "Data2/testDigits"


#将文字图像转换成mat
def img2Mat(filePath):
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

def load_files_then_initmatsandlabels(fileFolder):
    files = os.listdir(fileFolder)

    mats = np.zeros((len(files),1024))
    labels = np.zeros((len(files),1))
    
    for i in range(len(files)):
        fileFullPath = fileFolder + "/" + files[i]
        mat,label = img2Mat(fileFullPath)

        mats[i] = mat
        labels[i] = label

    return mats,labels

def main():
    trainDataMats ,trainDataLabels = load_files_then_initmatsandlabels(trainingDigitsFolder)
    testDataMats,testDataLabels = load_files_then_initmatsandlabels(testDataFolder)

    #使用Knn 训练 默认k=5取周边的5个
    knn = neighbors.KNeighborsClassifier()
    knn.fit(trainDataMats,trainDataLabels)      #两个数据结构必须一致 行数

    result = knn.predict(testDataMats)

    currectNum = 0
    wrongNum = 0
    for i in  range(testDataLabels.size):
        if result[i] == testDataLabels[i][0]:
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
