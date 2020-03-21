
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def logistic(t, K, P0, r):
    t0 = 0
    r = 0.25
    # t:时间  t0:初始时间  P0:初始人数  K:环境容量  r:增长速率  Pt:极限人数
    exp_value = np.exp(r * (t - t0))
    # exp_value = e^(rt)
    Pt = (K * P0 * exp_value) / (K + P0 * (exp_value - 1))
    return Pt


'''
1.26日2761例
1.27日4535例
1.28日5997例
1.29日7736例
1.30日9720例
1.31日11821例
2.1日14411例
2.2日17238例
2.3日20471例
2.4日24363例
2.5日28060例
2.6日31211例
2.7日34598例
2.8日37251例
2.9日40235例
2.10日42708例
2.11日44730例
2.12日59882例
2.13日63932例
2.14日66576例
2.15日68584例
2.16日70635例
2.17日72582例
2.18日74279例
2.19日75101例
2.20日75993例
2.21日76392例
2.22日77041例
2.23日77262例
2.24日77779例
2.25日78190例
2.26日78630例
'''

# 日期和感染人数
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
t = np.array(t)
P = [2761, 4535, 5997, 7736, 9720, 11821, 14411, 17238, 20471, 24363, 28060, 31211, 34598, 37251,\
     40235, 42708, 44730, 59882, 63932, 66576, 68584, 70635, 72582, 74279, 75101, 75993, 76392,\
     77041, 77262, 77779, 78190, 78630]
P = np.array(P)

# 用最小二乘法进行拟合
popt, pcov = curve_fit(logistic, t, P)
# 获取popt里面是拟合系数
print("K:%d, P0:%d, r:%d" % (popt[0],popt[1],popt[2]))
# 拟合后预测的P值
P_predict = logistic(t, popt[0], popt[1], popt[2])
# 未来情况预测
tomorrow = [32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 57, 58, 60]
tomorrow = np.array(tomorrow)
tomorrow_predict = logistic(tomorrow, popt[0], popt[1], popt[2])
# 中文可以正常显示
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plot1 = plt.plot(t, P, "s", label="累计确诊人数", marker = '.')
plot2 = plt.plot(t, P_predict, 'r', label='拟合确诊人数')
plot3 = plt.plot(tomorrow, tomorrow_predict, 's', label='预测确诊人数', marker = '.')
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend(loc="best")
# 显示某个点的人数
for i in range(60):
    print(logistic(np.array(i), popt[0], popt[1], popt[2]))
plt.show()