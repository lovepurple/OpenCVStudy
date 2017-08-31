'''
    数据可视化成各种图形，各种统计图

    中文的支持，可修改
    mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题  

    也可以使用FontManager
'''


import matplotlib.pyplot as plt
import matplotlib.font_manager as fontMgr
import numpy as np

customFont = fontMgr.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#基本的二维图像
plt.plot([1,2,3,4],[0,10,20,30])
#plt.ylabel("Y 轴")
#plt.xlabel("X 轴")
plt.ylabel("Y 轴",fontproperties=customFont)
plt.xlabel("X 轴",fontproperties=customFont)

plt.clf()
#subplot() 一个画布上画多个图
#axis([xmin,xmax,ymin,ymax])
sinDiagram = plt.subplot(2,1,1)       #创建2行，1列的图，当前为第一个 也可以写成plt.subplot(211)

#sinDiagram.title("Sin(x) function")
x_values = np.arange(-np.pi * 4,np.pi * 4,0.01)          #X轴的范围0~4Pi 每个单位0.01
y_values = np.sin(x_values)     #y轴的值
sinDiagram.plot(x_values,y_values,linewidth = 1.0,c='#000000')
sinDiagram.set_xlabel('x')
sinDiagram.set_ylabel('sin(x)')

#饼状图
pieDiagram = plt.subplot(2,1,2)

label = np.array(['Frogs', 'Hogs', 'Dogs', 'Logs'])
sizes = np.array([15, 30, 45, 10])
pieDiagram.pie(sizes,labels = label,shadow=True)


 
plt.show()