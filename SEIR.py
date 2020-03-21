import numpy as np
import matplotlib.pyplot as plt

# N:区域总人数
N = 215000
# beta:传染率
beta = 0.25
# alpha:潜伏期
alpha = 0.143
# gamma:康复率
gamma = 0.143
# I:感染者初始人数
I = 1
# R:康复者初始人数
R = 0
# E:潜伏者初始人数
E = 0
# S:易感者初始人数
S = N - I
# contact:感染者每天接触人数
contact = 3.8
# T:传播时间
T = 150

Num = np.zeros((4,T))
Num[0][0] = I
Num[1][0] = S
Num[2][0] = R
Num[3][0] = E

def SI_Model():
    for i in range(T-1):
        # 感染者人数变化
        Num[0][i + 1] = Num[0][i] + alpha * Num[3][i] - gamma * Num[0][i]
        # 易感者人数变化
        Num[1][i + 1] = Num[1][i] - (contact * beta * Num[0][i] * Num[1][i]) / N
        # 康复者人数变化
        Num[2][i + 1] = Num[2][i] + gamma * Num[0][i]
        # 潜伏者人数变化
        Num[3][i + 1] = Num[3][i] + (contact * beta * Num[0][i] * Num[1][i]) / N - alpha * Num[3][i]


SI_Model()
# 中文正常显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plot1 = plt.plot(range(T),Num[0], 'r', label='感染者人数', color="red")
plot2 = plt.plot(range(T),Num[1], 'r', label='易感者人数', color="blue")
plot3 = plt.plot(range(T),Num[2], 'r', label='康复者人数', color="green")
plot4 = plt.plot(range(T),Num[3], 'r', label='潜伏者人数', color="orange")
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend(loc="best")
plt.show()