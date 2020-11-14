import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

fig = plt.figure(figsize=(15, 8), dpi=80)

ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('先来先服务FCFS算法')
ax1.set_ylim(0.5, 10)
ax1.set_xticks([i for i in range(21)])
ax1.set_yticks([])
ax1.set_yticks([1, 2, 3, 4, 5])
ax1.set_yticklabels(labels=['A', 'B', 'C', 'D', 'E'])
plt.plot([0, 3], [1, 1], color='b', linewidth=3)
plt.plot([3, 9], [2, 2], color='r', linewidth=3)
plt.plot([9, 13], [3, 3], color='g', linewidth=3)
plt.plot([13, 18], [4, 4], color='k', linewidth=3)
plt.plot([18, 20], [5, 5], color='y', linewidth=3)
plt.legend(['A', 'B', 'C', 'D', 'E'])

ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('最短进程优先SJF算法')
ax2.set_ylim(0.5, 10)
ax2.set_xticks([i for i in range(21)])
ax2.set_yticks([])
ax2.set_yticks([1, 2, 3, 4, 5])
ax2.set_yticklabels(labels=['A', 'B', 'C', 'D', 'E'])
plt.plot([0, 3], [1, 1], color='b', linewidth=3)
plt.plot([3, 9], [2, 2], color='r', linewidth=3)
plt.plot([9, 11], [5, 5], color='y', linewidth=3)
plt.plot([11, 15], [3, 3], color='g', linewidth=3)
plt.plot([15, 20], [4, 4], color='k', linewidth=3)
plt.legend(['A', 'B', 'E', 'C', 'D'])

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('轮转RR算法')
ax3.set_ylim(0.5, 10)
ax3.set_xticks([i for i in range(21)])
ax3.set_yticks([])
ax3.set_yticks([1, 2, 3, 4, 5])
ax3.set_yticklabels(labels=['A', 'B', 'C', 'D', 'E'])
plt.plot([0, 2], [1, 1], color='b', linewidth=1)
plt.plot([3, 4], [1, 1], color='b', linewidth=1)
plt.plot([2, 3], [2, 2], color='r', linewidth=1)
plt.plot([4, 5], [2, 2], color='r', linewidth=1)
plt.plot([6, 7], [2, 2], color='r', linewidth=1)
plt.plot([9, 10], [2, 2], color='r', linewidth=1)
plt.plot([13, 14], [2, 2], color='r', linewidth=1)
plt.plot([17, 18], [2, 2], color='r', linewidth=1)
plt.plot([5, 6], [3, 3], color='g', linewidth=1)
plt.plot([8, 9], [3, 3], color='g', linewidth=1)
plt.plot([12, 13], [3, 3], color='g', linewidth=1)
plt.plot([16, 17], [3, 3], color='g', linewidth=1)
plt.plot([7, 8], [4, 4], color='y', linewidth=1)
plt.plot([11, 12], [4, 4], color='y', linewidth=1)
plt.plot([15, 16], [4, 4], color='y', linewidth=1)
plt.plot([18, 20], [4, 4], color='y', linewidth=1)
plt.plot([10, 11], [5, 5], color='k', linewidth=1)
plt.plot([14, 15], [5, 5], color='k', linewidth=1)

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('最高响应比优先HRN算法')
ax4.set_ylim(0.5, 10)
ax4.set_xticks([i for i in range(21)])
ax4.set_yticks([])
ax4.set_yticks([1, 2, 3, 4, 5])
ax4.set_yticklabels(labels=['A', 'B', 'C', 'D', 'E'])
plt.plot([0, 3], [1, 1], color='b', linewidth=3)
plt.plot([3, 9], [2, 2], color='r', linewidth=3)
plt.plot([9, 13], [3, 3], color='g', linewidth=3)
plt.plot([13, 15], [5, 5], color='y', linewidth=3)
plt.plot([15, 20], [4, 4], color='k', linewidth=3)
plt.legend(['A', 'B', 'C', 'D', 'E'])

plt.show()
