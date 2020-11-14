# coding='utf-8'
"""
    @author: Yuan Yi fu
    a class implement SSTF and SCAN algorithm
"""
import copy


class DiskAlgorithm(object):
    def __init__(self, start, diskList):
        self.start = start
        self.diskList = diskList

    def SSTF(self):
        """
        最短寻找时间优先（SSTF）
        不断找出和当前位置寻找时间最短的磁道
        :return:diskHistory 相应请求的顺序 distanceMove 总移动距离
        """
        currentPosition = self.start  # currentPosition
        diskListCopy = copy.deepcopy(list(map(int, self.diskList)))  # copy diskList
        diskHistory = list()  # history
        distanceMove = 0

        for i in range(len(diskListCopy)):
            # 对diskList排序，选出离当前位置最近的磁道
            minDisk = min(diskListCopy, key=lambda x: abs(x - currentPosition))
            # 磁盘移动历史列表加入该磁道
            diskHistory.append(minDisk)
            # 移臂总距离增加
            distanceMove += abs(currentPosition - minDisk)
            # 更新当前磁臂位置
            currentPosition = minDisk
            diskListCopy.remove(minDisk)

        print("SSTF :  " + (" ".join(map(str, diskHistory))))
        print("Distance:  {}".format(distanceMove))

        return diskHistory, distanceMove

    def SCAN(self):
        """
        扫描算法(SCAN)
        当设备无访问请求，磁头不动；
        有访问请求时先按一个方向一直移动，如果有则继续扫描，直到该方向无访问请求；
        否则改变移动方向，重复上述操作
        :return:diskHistory 相应请求的顺序 distanceMove 总移动距离
        """
        currentPosition = self.start  # currentPosition
        diskListCopy = copy.deepcopy(list(map(int, self.diskList)))  # copy diskList
        diskHistory = list()  # history
        distanceMove = 0
        direct = 1  # 初始化方向 1+ 0-

        # 如果DiskList不空，则持续遍历
        while diskListCopy:

            # direct = 1 正向扫描 +
            if direct:
                # 只要磁头扫描到磁道的访问请求，则立即执行访问请求
                if currentPosition in diskListCopy:
                    diskListCopy.remove(currentPosition)
                    diskHistory.append(currentPosition)

                # 扫描过程，如果没达到该方向的最大访问请求，则继续扫描
                if diskListCopy:
                    maxDiskPos = max(diskListCopy)
                    # 大于等于是为了防止一开始磁头的位置就大于最大的磁道
                    if currentPosition >= maxDiskPos:
                        direct = 0
                        currentPosition -= 1
                        distanceMove += 1
                    else:
                        currentPosition += 1
                        distanceMove += 1

            # direct = 0 负向扫描 -
            else:
                if currentPosition in diskListCopy:
                    diskListCopy.remove(currentPosition)
                    diskHistory.append(currentPosition)

                # 扫描过程，如果没达到该方向的最小访问请求，则继续扫描
                if diskListCopy:
                    minDiskPos = min(diskListCopy)
                    # 小于等于是为了防止一开始磁头的位置就大于最大的磁道
                    if currentPosition <= minDiskPos:
                        direct = 1
                    else:
                        currentPosition -= 1
                        distanceMove += 1
        print("SCAN :  " + (" ".join(map(str, diskHistory))))
        print("Distance:  {}".format(distanceMove))

        return diskHistory, distanceMove
