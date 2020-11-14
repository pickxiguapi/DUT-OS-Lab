"""
    @author: Yuan Yi fu
    create GUI using tkinter
"""

from tkinter import *
from tkinter import ttk
from PCB import Process
from schedulingAlgorithm import Scheduling


class GUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("处理器调度算法模拟")

        # init StringVar
        self.key1 = StringVar()
        self.key2 = StringVar()
        self.key3 = StringVar()
        self.treeIndex = 0
        self.tree2Index = 0
        self.aveC = 0  # 本次调度平均周转时间
        self.aveVC = 0  # 本次调度平均带权周转时间

        self.createInputContent(self.root)
        self.showOutputContent(self.root)
        self.root.update()

        # get process list
        self.processList = list()

        # 使窗体在屏幕正中
        curWidth = self.root.winfo_width()  # get current width
        curHeight = self.root.winfo_height()  # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        tmp = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmp)

        self.root.mainloop()

    def createInputContent(self, root):
        lf = ttk.LabelFrame(root, text="添加进程")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)

        ttk.Label(top_frame, text='进程名: ').pack(side=LEFT, fill=X, expand=YES)
        self.en1 = ttk.Entry(top_frame, width=16, textvariable=self.key1)
        self.en1.pack(side=LEFT)
        ttk.Label(top_frame, text='到达时间: ').pack(side=LEFT, fill=X, expand=YES)
        self.en2 = ttk.Entry(top_frame, width=16, textvariable=self.key2)
        self.en2.pack(side=LEFT)
        ttk.Label(top_frame, text='服务时间: ').pack(side=LEFT, fill=X, expand=YES)
        self.en3 = ttk.Entry(top_frame, width=16, textvariable=self.key3)
        self.en3.pack(side=LEFT)
        ttk.Button(top_frame, text="添加", command=self.getEntry).pack(padx=15, fill=X, expand=YES)

        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=BOTH, expand=YES, side=TOP, padx=15, pady=8)

        self.tree = ttk.Treeview(bottom_frame, columns=['序号', '进程名', '到达时间', '服务时间'], show='headings')
        self.tree.column('序号', width=100, anchor='center')
        self.tree.column('进程名', width=100, anchor='center')
        self.tree.column('到达时间', width=100, anchor='center')
        self.tree.column('服务时间', width=100, anchor='center')
        self.tree.heading('序号', text='序号')
        self.tree.heading('进程名', text='进程名')
        self.tree.heading('到达时间', text='到达时间')
        self.tree.heading('服务时间', text='服务时间')
        self.tree.pack(side=TOP, fill=X, padx=15)

    def showOutputContent(self, root):
        lf2 = ttk.LabelFrame(root, text="算法执行")
        lf2.pack(fill=X, padx=15, pady=8)
        top_frame = Frame(lf2)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)
        ttk.Button(top_frame, text="先来先服务FCFS", command=self.FCFS).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(top_frame, text="最短进程优先SJF", command=self.SJF).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(top_frame, text="轮转RR", command=self.RR).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(top_frame, text="最高响应比优先HRN", command=self.HRN).pack(side=LEFT, padx=15, fill=X, expand=YES)

        bottom_frame = Frame(lf2)
        bottom_frame.pack(fill=BOTH, expand=YES, side=TOP, padx=15, pady=8)

        self.tree2 = ttk.Treeview(bottom_frame, columns=['进程名', '到达时间', '服务时间', '完成时间', '周转时间', '带权周转时间'], show='headings')
        self.tree2.column('进程名', width=100, anchor='center')
        self.tree2.column('到达时间', width=100, anchor='center')
        self.tree2.column('服务时间', width=100, anchor='center')
        self.tree2.column('完成时间', width=100, anchor='center')
        self.tree2.column('周转时间', width=100, anchor='center')
        self.tree2.column('带权周转时间', width=100, anchor='center')
        self.tree2.heading('进程名', text='进程名')
        self.tree2.heading('到达时间', text='到达时间')
        self.tree2.heading('服务时间', text='服务时间')
        self.tree2.heading('完成时间', text='完成时间')
        self.tree2.heading('周转时间', text='周转时间')
        self.tree2.heading('带权周转时间', text='带权周转时间')
        self.tree2.pack(side=TOP, fill=X, padx=15)

        self.text1 = StringVar()
        self.text2 = StringVar()
        ttk.Label(bottom_frame, text="本次调度平均周转时间为: ", width=15).pack(side=LEFT, fill=X, expand=YES)
        self.l1 = ttk.Label(bottom_frame, text=self.text1)
        self.l1.pack(side=LEFT, fill=X, expand=YES)
        ttk.Label(bottom_frame, text="本次调度平均带权周转时间为: ", width=15).pack(side=LEFT, fill=X, expand=YES)
        self.l2 = ttk.Label(bottom_frame, text=self.text2)
        self.l2.pack(side=LEFT, fill=X, expand=YES)
        self.l1['text'] = str(self.aveC)
        self.l2['text'] = str(self.aveVC)

    def getEntry(self):
        data = [self.treeIndex, self.key1.get(), self.key2.get(), self.key3.get()]
        self.addProcessList(data[1:])
        self.tree.insert("", self.treeIndex, values=tuple(data))
        self.treeIndex += 1

        # 删除文本框内容
        self.en1.delete(0, 'end')
        self.en2.delete(0, 'end')
        self.en3.delete(0, 'end')

    def delTree(self, tree):
        item = tree.get_children()
        for i in item:
            tree.delete(i)

    def addProcessList(self, data):
        self.processList.append(Process(data[0], int(data[1]), int(data[2])))

    def getProcessList(self):
        return self.processList

    def FCFS(self):
        FCFSScheduling = Scheduling('FCFS', self.processList)
        self.processList, self.aveC, self.aveVC = FCFSScheduling.implement()
        self.outputAlgorithmResult()
        self.updateText()

    def SJF(self):
        SJFScheduling = Scheduling('SJF', self.processList)
        self.processList, self.aveC, self.aveVC = SJFScheduling.implement()
        self.outputAlgorithmResult()
        self.updateText()

    def RR(self):
        RRScheduling = Scheduling('RR', self.processList)
        self.processList, self.aveC, self.aveVC = RRScheduling.implement()
        self.outputAlgorithmResult()
        self.updateText()

    def HRN(self):
        HRNScheduling = Scheduling('HRN', self.processList)
        self.processList, self.aveC, self.aveVC = HRNScheduling.implement()
        self.outputAlgorithmResult()
        self.updateText()

    def updateText(self):
        self.l1['text'] = str(round(self.aveC, 3))
        self.l2['text'] = str(round(self.aveVC, 3))
        self.root.update()

    def outputAlgorithmResult(self):
        self.delTree(self.tree2)
        self.tree2Index = 0
        for i in range(len(self.processList)):
            data = (self.processList[i].name,
                    self.processList[i].arriveTime,
                    self.processList[i].serveTime,
                    self.processList[i].finishTime,
                    self.processList[i].cyclingTime,
                    self.processList[i].varCyclingTime)
            self.tree2.insert("", self.tree2Index, values=data)
            self.tree2Index += 1


if __name__ == "__main__":
    GUI()
