import numpy as np
import matplotlib.pyplot as plt

# N:区域总人数
N = 10000
# beta:传染率
beta = 0.01
# I:感染者初始人数
I = 1
# S:易感者初始人数
S = N - I
# contact:感染者每天接触人数
contact = 10
# T:传播时间
T = 200

Num = np.zeros((3,T))
Num[0][0] = I
Num[1][0] = S

def SI_Model():
    for i in range(T-1):
        # 感染者人数变化
        Num[0][i + 1] = Num[0][i] + (contact * beta * Num[0][i] * Num[1][i]) / N
        # 易感者人数变化
        Num[1][i + 1] = Num[1][i] - (contact * beta * Num[0][i] * Num[1][i]) / N

SI_Model()
# 中文正常显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plot1 = plt.plot(range(T),Num[0], 'r', label='感染者人数', color="red")
plot2 = plt.plot(range(T),Num[1], 'r', label='易感者人数', color="blue")
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend(loc="best")
plt.show()