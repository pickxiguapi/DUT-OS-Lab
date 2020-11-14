"""
    @author: Yuan Yi fu
    create GUI using tkinter
"""

from tkinter import *
from tkinter import ttk
from Algorithm import PageAlgorithm
import copy


class GUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("置换算法模拟")

        # init StringVar
        self.key1 = StringVar()
        self.key2 = StringVar()
        self.key3 = StringVar()
        self.frameNum = 0
        self.pageNum = 0
        self.pageList = list()
        self.pageContent = list()  # 每一个物理页框中存放的信息

        self.createContent()
        self.root.update()

        # 使窗体在屏幕正中
        curWidth = self.root.winfo_width()  # get current width
        curHeight = self.root.winfo_height()  # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        tmp = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmp)

        self.root.mainloop()

    def createContent(self):
        lf = ttk.LabelFrame(self.root, text="输入页面请求")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)

        f1 = Frame(top_frame)
        f1.pack(fill=X, expand=YES, side=LEFT, padx=15, pady=8)
        ttk.Label(f1, text='物理页框数:', width=15).pack(side=LEFT)
        self.en1 = ttk.Entry(f1, textvariable=self.key1)
        self.en1.pack(side=LEFT)

        f2 = Frame(top_frame)
        f2.pack(fill=X, expand=YES, side=LEFT, padx=0, pady=8)
        ttk.Label(f2, text='页面请求数:', width=15).pack(side=LEFT)
        self.en2 = ttk.Entry(f2, textvariable=self.key2)
        self.en2.pack(side=LEFT)


        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=BOTH, expand=YES, side=TOP, padx=15, pady=8)

        f3 = Frame(bottom_frame)
        f3.pack(fill=X, expand=YES, side=TOP, padx=15)
        ttk.Label(f3, text='页面请求序列: ').pack(side=LEFT, fill=X, expand=YES)
        self.en3 = ttk.Entry(f3, width=50, textvariable=self.key3)
        self.en3.pack(side=LEFT, padx=10, fill=X, expand=YES)
        ttk.Button(f3, text="输入", command=self.getEntry).pack(padx=15, fill=X, expand=YES)

        f4 = Frame(bottom_frame)
        f4.pack(fill=X, expand=YES, side=TOP, padx=15)
        self.text1 = ttk.Label(f4, text='输入的页面请求序列为：')
        self.text1.pack()

    def createOutput(self):
        lf = ttk.LabelFrame(self.root, text="页面替换算法输出")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)
        ttk.Button(top_frame, text="先进先出置换算法FIFO", command=self.FIFO).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(top_frame, text="最久未使用置换算法LRU", command=self.LRU).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(top_frame, text="最佳置换算法OPT", command=self.OPT).pack(side=LEFT, padx=15, fill=X, expand=YES)

        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)
        pl = copy.deepcopy(self.getPageList())
        for i in range(len(pl)):
            pl[i] += '(' + str(i+1) + ')'
        pl = ['页面请求序列'] + pl
        self.tree2 = ttk.Treeview(bottom_frame, columns=pl, show='headings')
        self.tree2.column('页面请求序列', width=100, anchor='center')
        self.tree2.heading('页面请求序列', text='页面请求序列')
        for p in pl:
            self.tree2.column(p, width=100, anchor='center')
            self.tree2.heading(p, text=p)
        self.tree2.pack(side=TOP, fill=X, padx=15)

        ttk.Label(bottom_frame, text="依次淘汰的页号: ", width=15).pack(side=LEFT, fill=X, expand=YES)
        self.l1 = ttk.Label(bottom_frame)
        self.l1.pack(side=LEFT, fill=X, expand=YES)
        ttk.Label(bottom_frame, text="缺页次数: ", width=15).pack(side=LEFT, fill=X, expand=YES)
        self.l2 = ttk.Label(bottom_frame)
        self.l2.pack(side=LEFT, fill=X, expand=YES)
        ttk.Label(bottom_frame, text="缺页率: ", width=15).pack(side=LEFT, fill=X, expand=YES)
        self.l3 = ttk.Label(bottom_frame)
        self.l3.pack(side=LEFT, fill=X, expand=YES)

    def getPageList(self):
        return self.pageList

    def getColumns(self):
        return ['页面请求序列'] + self.getPageList()

    def FIFO(self):
        FIFO = PageAlgorithm('FIFO', self.frameNum, self.pageList)
        FIFO.implement()
        data, missNum, deleteList, showDelete = FIFO.getData()

        # insert data to table
        self.delTree(self.tree2)
        for i in range(self.frameNum):
            data[i] = ['页面{}'.format(i+1)] + data[i]
            data[i] = ['' if j is None else j for j in data[i]]
            self.tree2.insert("", i, values=tuple(data[i]))
        showDelete = ['淘汰的页面'] + showDelete
        self.tree2.insert("", self.frameNum, values=tuple(showDelete))

        self.l1['text'] = str(deleteList)
        self.l2['text'] = missNum
        self.l3['text'] = int(missNum) / self.pageNum
        self.root.update()

    def LRU(self):
        LRU = PageAlgorithm('LRU', self.frameNum, self.pageList)
        LRU.implement()
        data, missNum, deleteList, showDelete = LRU.getData()

        # insert data to table
        self.delTree(self.tree2)
        for i in range(self.frameNum):
            data[i] = ['页面{}'.format(i + 1)] + data[i]
            data[i] = ['' if j is None else j for j in data[i]]
            self.tree2.insert("", i, values=tuple(data[i]))
        showDelete = ['淘汰的页面'] + showDelete
        self.tree2.insert("", self.frameNum, values=tuple(showDelete))

        self.l1['text'] = str(deleteList)
        self.l2['text'] = missNum
        self.l3['text'] = int(missNum) / self.pageNum
        self.root.update()

    def OPT(self):
        OPT = PageAlgorithm('OPT', self.frameNum, self.pageList)
        OPT.implement()
        data, missNum, deleteList, showDelete = OPT.getData()

        # insert data to table
        self.delTree(self.tree2)
        for i in range(self.frameNum):
            data[i] = ['页面{}'.format(i + 1)] + data[i]
            data[i] = ['' if j is None else j for j in data[i]]
            self.tree2.insert("", i, values=tuple(data[i]))
        showDelete = ['淘汰的页面'] + showDelete
        self.tree2.insert("", self.frameNum, values=tuple(showDelete))

        self.l1['text'] = str(deleteList)
        self.l2['text'] = missNum
        self.l3['text'] = int(missNum) / self.pageNum
        self.root.update()

    def delTree(self, tree):
        item = tree.get_children()
        for i in item:
            tree.delete(i)

    def getEntry(self):
        # key1 物理页框数
        # key2 页面请求数
        # key3 页面请求序列
        self.frameNum = int(self.key1.get())
        self.pageNum = int(self.key2.get())
        tmpStr = self.key3.get()
        self.pageList = tmpStr.split(" ")  # 页面走向
        self.text1['text'] = '输入的页面请求序列为：' + str(self.pageList)

        # 删除文本框内容
        self.en1.delete(0, 'end')
        self.en2.delete(0, 'end')
        self.en3.delete(0, 'end')

        self.createOutput()
        self.root.update()


if __name__ == "__main__":
    GUI()



