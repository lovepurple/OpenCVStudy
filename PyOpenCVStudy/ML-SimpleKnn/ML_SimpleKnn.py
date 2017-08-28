#knn k-nearest neightbor 最临近算法，

import matplotlib.pyplot as plt     #绘图库，包括大量matlab函数，高质量图形输出，各种统计图
import numpy as np
from sklearn import datasets,metrics    #聚类算法库

digits = datasets.load_digits()

print(digits.data.shape)


#k-means 算法