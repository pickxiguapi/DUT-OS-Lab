"""
    @author: Yuan Yi fu
    create GUI using tkinter
"""

from tkinter import *
from tkinter import ttk
from Simulation import Simulation


class GUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("文件管理模拟")

        # init StringVar
        self.key1 = StringVar()
        self.key2 = StringVar()
        self.key3 = StringVar()

        self.createContent()
        self.createCanvas()
        self.root.update()

        # 使窗体在屏幕正中
        curWidth = self.root.winfo_width()  # get current width
        curHeight = self.root.winfo_height()  # get current height
        scnWidth, scnHeight = self.root.maxsize()  # get screen width and height
        tmp = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        self.root.geometry(tmp)

        self.root.mainloop()

    def createContent(self):
        lf = ttk.LabelFrame(self.root, text="磁盘文件信息")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)

        self.tree = ttk.Treeview(top_frame, columns=['文件名', '文件大小（K）', '占据磁盘块'], show='headings')
        self.tree.column('文件名', anchor='center')
        self.tree.heading('文件名', text='文件名')
        self.tree.column('文件大小（K）', anchor='center')
        self.tree.heading('文件大小（K）', text='文件大小（K）')
        self.tree.column('占据磁盘块', anchor='center')
        self.tree.heading('占据磁盘块', text='占据磁盘块')

        self.tree.pack(side=LEFT)

        bottom_frame = Frame(lf)
        bottom_frame.pack(fill=X, expand=YES, side=TOP, padx=15, pady=8)
        ttk.Button(bottom_frame, text="随机生成50个文件", command=self.createFile).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(bottom_frame, text="删除奇数文件", command=self.deleteFile).pack(side=LEFT, padx=15, fill=X, expand=YES)
        ttk.Button(bottom_frame, text="创建5个文件", command=self.create5File).pack(side=LEFT, padx=15, fill=X, expand=YES)

    def createFile(self):
        self.s = Simulation()
        self.s.createRandomFile()

        self.delTree(self.tree)
        for i in range(len(self.s.fileList)):
            if self.s.fileList[i].isStore:
                tmp = [self.s.fileList[i].name, self.s.fileList[i].size, self.s.fileList[i].diskList]
                self.tree.insert("", i, values=tuple(tmp))

                self.setStore(self.s.fileList[i].diskList, 'red')



    def deleteFile(self):
        self.s.deleteOdd()

        self.delTree(self.tree)

        self.cv.delete('all')
        for i in range(21):
            self.cv.create_line(25, 20*(i+1)+5, 525, 20*(i+1)+5)
        for j in range(26):
            self.cv.create_line(20 * (j + 1) + 5, 25, 20 * (j + 1) + 5, 425)

        for i in range(len(self.s.fileList)):
            if self.s.fileList[i].isStore:
                tmp = [self.s.fileList[i].name, self.s.fileList[i].size, self.s.fileList[i].diskList]
                self.tree.insert("", i, values=tuple(tmp))

                self.setStore(self.s.fileList[i].diskList, 'red')

    def create5File(self):
        self.s.createFiveFile()

        self.delTree(self.tree)
        for i in range(len(self.s.fileList)):
            if self.s.fileList[i].isStore:
                tmp = [self.s.fileList[i].name, self.s.fileList[i].size, self.s.fileList[i].diskList]
                self.tree.insert("", i, values=tuple(tmp))

                self.setStore(self.s.fileList[i].diskList, 'red')

    def createCanvas(self):
        lf = ttk.LabelFrame(self.root, text="磁盘文件存储")
        lf.pack(fill=X, padx=15, pady=8)

        self.cv = Canvas(lf, bg='white', width=530, height=430)
        self.cv.pack()
        for i in range(21):
            self.cv.create_line(25, 20*(i+1)+5, 525, 20*(i+1)+5)
        for j in range(26):
            self.cv.create_line(20 * (j + 1) + 5, 25, 20 * (j + 1) + 5, 425)

    def setStore(self, diskList, color):
        # 20*20大小 的矩形，每行25个，共20行， 最左上角是（25， 25） 最右下角是（505， 405）
        for d in diskList:
            row = d // 25
            col = d % 25

            x1 = 25+20*col
            y1 = 25+20*row
            pos = [x1, y1, x1+20, y1+20]
            self.cv.create_rectangle(pos, fill=color)

    def delTree(self, tree):
        item = tree.get_children()
        for i in item:
            tree.delete(i)


if __name__ == "__main__":
    GUI()



