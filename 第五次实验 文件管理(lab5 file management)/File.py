"""
    @author: Yuan Yifu
    用于创建文件类 包含文件的长度、编号等属性
"""


class File(object):
    def __init__(self, name, size):
        self.name = name  # 文件名
        self.diskList = list()  # 该文件占据的磁盘块编号
        self.isStore = False  # 是否已经在磁盘中存储
        self.size = size  # 文件的大小

    def setDiskPosition(self, disk):
        """
        设置该文件占据的磁盘块系列
        e.g. 1.txt 4k 占据磁盘块0 1
        """
        self.diskList = disk



