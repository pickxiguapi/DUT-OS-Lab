"""
    @author: Yuan Yifu
    仿真实现题目要求
    给出一个磁盘块序列：1、2、3、……、500，初始状态所有块为空的，每块的大小为2k。选择使用空闲表、空闲盘区链、位示图三种算法之一来管理空闲块。对于基于块的索引分配执行以下步骤：
(1) 随机生成2k-10k的文件50个，文件名为1.txt、2.txt、……、50.txt，按照上述算法存储到模拟磁盘中。
(2) 删除奇数.txt（1.txt、3.txt、……、49.txt）文件
(3) 新创建5个文件（A.txt、B.txt、C.txt、D.txt、E.txt），大小为：7k、5k、2k、9k、3.5k，按照与（1）相同的算法存储到模拟磁盘中。
(4) 给出文件A.txt、B.txt、C.txt、D.txt、E.txt的盘块存储状态和所有空闲区块的状态。

"""
import numpy as np
from File import File


class Simulation(object):
    def __init__(self):
        # 创建磁盘块序列：1、2、3、...、500，每个块的大小为2K
        # 初始化状态： 0 未存放 1 已存放数据
        self.blockList = [0 for _ in range(500)]

        # 文件列表
        self.fileList = list()

    def createRandomFile(self):
        # 随机生成50个文件的大小(均在2-10K之间)
        sizeList = np.random.uniform(low=2, high=10, size=50).round(1)

        # 生成50个文件,文件名为'1.txt' '2.txt'...
        for i in range(50):
            fileName = str(i+1) + '.txt'
            self.fileList.append(File(fileName, sizeList[i]))

        for i in range(50):
            # 通过整除的方法判断该文件实际应该占几个磁盘块
            blockNum = self.getBlockNum(self.fileList[i].size)
            # 使用distribution函数分配磁盘块
            tmp = self.distribution(blockNum)
            self.fileList[i].setDiskPosition(tmp)
            self.fileList[i].isStore = True

        self.showFileInfo()

    def getBlockNum(self, size):
        """
        :param size: 文件size
        :return: 文件应该占几个磁盘块
        """
        blockNum = 0
        if size == 2:
            blockNum = 1
        elif 2 < size <= 4:
            blockNum = 2
        elif 4 < size <= 6:
            blockNum = 3
        elif 6 < size <= 8:
            blockNum = 4
        elif 8 < size <= 10:
            blockNum = 5

        return blockNum

    def deleteOdd(self):
        for i in range(50):
            if i % 2 == 0:
                # 从文件列表中移除奇数号的文件,注意这里是从0开始存放的
                # 例如1.txt是fileList[0]
                self.fileList[i].isStore = False
                for t in self.fileList[i].diskList:
                    self.blockList[t] = 0
            else:
                pass
        # self.showFileInfo()

    def showFileInfo(self):
        # show file info
        for i in range(len(self.fileList)):
            if self.fileList[i].isStore:
                print(self.fileList[i].name, self.fileList[i].size, self.fileList[i].diskList)

        for i in range(20):
            for j in range(25):
                print(self.blockList[25*i+j], end=' ')
            print()

    def createFiveFile(self):
        # 新创建5个文件（A.txt、B.txt、C.txt、D.txt、E.txt），大小为：7k、5k、2k、9k、3.5k，按照与（1）相同的算法存储到模拟磁盘中。
        f1 = File('A.txt', 7)
        self.fileList.append(f1)
        tmp = self.distribution(self.getBlockNum(f1.size))
        f1.setDiskPosition(tmp)
        f1.isStore = True

        f2 = File('B.txt', 5)
        self.fileList.append(f2)
        tmp = self.distribution(self.getBlockNum(f2.size))
        f2.setDiskPosition(tmp)
        f2.isStore = True

        f3 = File('C.txt', 2)
        self.fileList.append(f3)
        tmp = self.distribution(self.getBlockNum(f3.size))
        f3.setDiskPosition(tmp)
        f3.isStore = True

        f4 = File('D.txt', 9)
        self.fileList.append(f4)
        tmp = self.distribution(self.getBlockNum(f4.size))
        f4.setDiskPosition(tmp)
        f4.isStore = True

        f5 = File('E.txt', 3.5)
        self.fileList.append(f5)
        tmp = self.distribution(self.getBlockNum(f5.size))
        f5.setDiskPosition(tmp)
        f5.isStore = True

        self.showFileInfo()

    def distribution(self, need):
        need = int(need)
        cnt = 0
        start = -1
        for i in range(len(self.blockList)):
            if self.blockList[i] == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == need:
                start = i - need + 1
                break
        tmp = [start + b for b in range(need)]
        for j in tmp:
            self.blockList[j] = 1

        return tmp

    def discreteDistribution(self, need):
        need = int(need)
        tmp = list()
        for i in range(len(self.blockList)):
            if self.blockList[i] == 0:
                tmp.append(i)
            if len(tmp) == need:
                break
        return tmp


