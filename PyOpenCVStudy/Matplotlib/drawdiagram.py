import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#remap 函数
def remap(current,imin,imax,omin,omax):
    return omin + (current - imin) * (omax - omin) / (imax - imin)

def smoothStep(x,min,max):
    if x <= min:
        return min
    elif x >= max:
        return max
    else:  #使用3*x^2 - 2*x^3版本
        smoothStepFun = lambda x: 3 * x ** 2 - 2 * x ** 3       # ** 相当于power
        
        xRemapto01 = remap(x,min,max,0,1)
        
        result = smoothStepFun(xRemapto01)
        
        return remap(result,0,1,min,max)

xValues = np.linspace(-10,10,1000)    #[-10,10] 差值出20个值
yValues = [smoothStep(xValues[x],-10,10) for x in range(len(xValues)) ]
fig,ax = plt.subplots(1,1)

ax.plot(xValues, yValues,'g-', label='smoothclamp')
plt.xticks(np.arange(-10,10,0.5))            #xticks 控制x轴一个单位的精度,太细的话太卡了


plt.legend(loc='upper left')
plt.show()