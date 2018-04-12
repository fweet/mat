import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
name = open('E:/各类文档/毕业设计/quant/ChinaBank.csv')
ChinaBank = pd.read_csv(name,index_col = 'Date')
ChinaBank = ChinaBank.iloc[:,1:]#位置索引与切片，提取所有行，从第一列开始的所有列
ChinaBank.head()#查看对象前五个数据
ChinaBank.index = pd.to_datetime(ChinaBank.index)#将索引转化成时间格式
Close = ChinaBank.Close#获取收盘价格的列
Open = ChinaBank.Open
plt.figure(figsize=(10,10))
plt.plot(Close['2014'],label = '收盘价')
plt.plot(Open['2014'],label = '开盘价')
plt.legend(loc = 2)#设置图例
plt.title('中国银行2014年收盘价曲线',loc = 'right')
plt.xlabel('日期')
plt.ylim(2.0,4.5)#调整y轴范围
plt.ylabel('收盘价')
plt.grid(True,axis = 'y')
plt.show()
