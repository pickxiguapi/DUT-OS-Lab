from tkinter import *
from tkinter import ttk
from DiskAlgorithm import DiskAlgorithm
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串


class GUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('磁盘移臂调度算法模拟')

        # init variable
        self.diskList = list()
        self.key1 = StringVar()
        self.i = 0

        self.createWindow()

        # 使窗体在屏幕正中
        curWidth = self.root.winfo_width()  # get current width
        curHeight = self.root.winfo_height()  # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        tmp = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmp)

        self.root.mainloop()

    def createWindow(self):
        lf = ttk.LabelFrame(self.root, text="展示磁盘移臂过程")
        lf.pack(fill=X, padx=15, pady=8)

        self.f1 = Frame(lf)
        self.f1.grid(row=1, column=0)

        self.fig1 = Figure(figsize=(8, 5), dpi=80)
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.set_title('最短寻找时间优先算法（SSTF）')
        # self.ax1.set_xlabel('磁道号')
        self.ax1.set_xlim(0, 300)
        self.ax1.set_ylim(0, 15)
        self.ax1.set_yticks([])
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)

        self.fig2 = Figure(figsize=(8, 5), dpi=80)
        self.ax2 = self.fig2.add_subplot(111)
        self.ax2.set_title('扫描算法(SCAN)')
        # self.ax2.set_xlabel('磁道号')
        self.ax2.set_xlim(0, 300)
        self.ax2.set_ylim(0, 15)
        self.ax2.set_yticks([])
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)

        f2 = Frame(lf)
        f2.grid(row=2, column=0, pady=10)
        self.text1 = ttk.Label(f2, text='磁头起始位置:', width=20)
        self.text1.pack(side=LEFT, fill=X, padx=15)
        self.text2 = ttk.Label(f2, text='磁盘请求序列为: ', width=50)
        self.text2.pack(side=LEFT, fill=X, padx=15)
        self.text3 = ttk.Label(f2, text='响应磁盘请求的顺序为: ', width=50)
        self.text3.pack(side=LEFT, fill=X, padx=15)
        self.text4 = ttk.Label(f2, text='移臂的距离总量为:', width=50)
        self.text4.pack(side=LEFT, fill=X, padx=15)

        f3 = Frame(lf)
        f3.grid(row=3, column=0, pady=10)

        e1 = ttk.Entry(f3, width=70, textvariable=self.key1)
        e1.grid(row=1, column=1, padx=5)

        b1 = ttk.Button(f3, text="输入数据", command=self.inputData)
        b1.grid(row=1, column=2, padx=5)

        b2 = ttk.Button(f3, text="随机生成数据", command=self.randomData)
        b2.grid(row=1, column=3, padx=5)

        f4 = Frame(lf)
        f4.grid(row=4, column=0, pady=10)

        b3 = ttk.Button(f4, text="单步执行", command=self.drawPicSingleStep)
        b3.grid(row=1, column=1, padx=5)

        b4 = ttk.Button(f4, text="全部执行", command=self.drawPic)
        b4.grid(row=1, column=2, padx=5)

    def inputData(self):
        # key1 输入的请求序列
        self.diskList = list(map(int, self.key1.get().split(" ")))

        # update text
        self.text1['text'] = '磁头起始位置:' + str(self.diskList[0])
        self.text2['text'] = '磁盘请求序列为: ' + str(self.diskList)

        # update plot
        self.ax1.set_xticks(list(self.diskList))
        self.ax1.set_yticks([])
        self.ax2.set_xticks(list(self.diskList))
        self.ax2.set_yticks([])
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)

    def randomData(self):
        data = list()
        data.append(np.random.randint(low=0, high=280))
        while len(data) < 10:
            tmp = np.random.randint(low=0, high=280)
            flag = 0
            for i in range(len(data)):
                if abs(tmp - data[i]) >= 10:
                    flag += 1
            if flag == len(data):
                data.append(tmp)

        self.key1.set(data)

        self.diskList = data
        # update text
        self.text1['text'] = '磁头起始位置:' + str(self.diskList[0])
        self.text2['text'] = '磁盘请求序列为: ' + str(self.diskList)

        # update plot
        self.ax1.set_xticks(list(self.diskList))
        self.ax2.set_xticks(list(self.diskList))
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)

    def drawPicSingleStep(self):
        self.i += 1
        self.ax1.clear()
        self.ax2.clear()

        al = DiskAlgorithm(self.diskList[0], self.diskList)
        sstfHistory, sstfDistance = al.SSTF()
        al2 = DiskAlgorithm(self.diskList[0], self.diskList)
        scanHistory, scanDistance = al2.SCAN()

        # update plot
        self.ax1.set_xticks(list(self.diskList))
        self.ax1.set_yticks([])
        self.ax1.set_title('最短寻找时间优先算法（SSTF）')
        self.ax2.set_xticks(list(self.diskList))
        self.ax2.set_yticks([])
        self.ax2.set_title('扫描算法(SCAN)')
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)
        self.ax1.plot(sstfHistory[:self.i], range(len(sstfHistory[:self.i])), linestyle='--', marker='o')
        self.canvas1.draw()
        self.ax2.plot(scanHistory[:self.i], range(len(scanHistory[:self.i])), linestyle=':', marker='*')
        self.canvas2.draw()
        self.text4['text'] = '移臂的距离总量为:' + '\n' + ' SSTF: ' + \
                             str(sstfDistance) + '\n' + ' SCAN: ' + str(scanDistance)
        self.text3['text'] = '响应磁盘请求的顺序为:' + '\n' + ' SSTF: ' + \
                             str(sstfHistory) + '\n' + ' SCAN: ' + str(scanHistory)

        if self.i == len(scanHistory):
            self.i = 0
    def drawPic(self):
        self.ax1.clear()
        self.ax2.clear()

        al = DiskAlgorithm(self.diskList[0], self.diskList)
        sstfHistory, sstfDistance = al.SSTF()
        al2 = DiskAlgorithm(self.diskList[0], self.diskList)
        scanHistory, scanDistance = al2.SCAN()

        # update plot
        self.ax1.set_xticks(list(self.diskList))
        self.ax1.set_yticks([])
        self.ax1.set_title('最短寻找时间优先算法（SSTF）')
        self.ax2.set_xticks(list(self.diskList))
        self.ax2.set_yticks([])
        self.ax2.set_title('扫描算法(SCAN)')
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.f1)
        self.canvas1.get_tk_widget().grid(row=1, column=1)
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.f1)
        self.canvas2.get_tk_widget().grid(row=1, column=2)
        self.ax1.plot(sstfHistory, range(len(sstfHistory)), linestyle='--', marker='o')
        self.canvas1.draw()
        self.ax2.plot(scanHistory, range(len(scanHistory)), linestyle=':', marker='*')
        self.canvas2.draw()
        self.text4['text'] ='移臂的距离总量为:' + '\n' + ' SSTF: ' +\
                            str(sstfDistance) + '\n' + ' SCAN: ' + str(scanDistance)
        self.text3['text'] = '响应磁盘请求的顺序为:' + '\n' + ' SSTF: ' +\
                            str(sstfHistory) + '\n' + ' SCAN: ' + str(scanHistory)












GUI()

