# coding=utf-8
"""
    @author:Yuan Yi fu

"""


class PageAlgorithm(object):
    def __init__(self, name, frameNum, pages):
        self.alName = name  # 应用的算法名称
        self.frameNum = frameNum
        self.pages = pages
        self.missNUm = 0  # 缺页次数
        self.pageDelete = list()  # 淘汰页面
        self.dataContent = [[0 for _ in range(len(pages))] for _ in range(frameNum)]  # 为了在GUI界面显示
        self.showDelete = list()  # 便于展示缺页

    def implement(self):
        if self.alName == 'FIFO':
            self.FIFO(self.frameNum, self.pages)
        elif self.alName == 'LRU':
            self.LRU(self.frameNum, self.pages)
        elif self.alName == 'OPT':
            self.OPT(self.frameNum, self.pages)

    def FIFO(self, frameNum, pages):
        pageNum = len(pages)  # 页面请求数
        count = 0  # 当前计数
        isRoom = True  # 是否有空位
        pageFrame = [None for i in range(frameNum)]  # 初始化物理页框
        deleteIndex = 0  # FIFO替换页的索引

        self.missNum = 0
        self.pageDelete = list()
        self.showDelete = list()

        while count < pageNum:  # 对每个页面请求依次判断
            print("第" + str(count + 1) + "次：" + pages[count])

            # 判断物理页框中是否存在本次页面请求
            isExist = False
            for p in pageFrame:
                if pages[count] == p:
                    isExist = True
            if isExist:
                print("本次页面请求在物理页框中存在")
                print("目前物理页框中页面请求为：", end="")
                for p in pageFrame:
                    print(p, end=" ")
                print()
                print()
                self.showDelete.append('x')
            else:
                # 如果页面请求在物理页框中不存在
                # 判断物理页框中有无空位
                for p in pageFrame:
                    if not p:
                        isRoom = True
                        break
                    else:
                        isRoom = False

                if isRoom:  # 如果物理页框有空位
                    for n in range(frameNum):
                        if pageFrame[n] is None:
                            pageFrame[n] = pages[count]
                            break
                    self.showDelete.append('x')
                else:  # 如果物理框没有空位
                    # FIFO
                    self.pageDelete.append(pageFrame[deleteIndex % frameNum])
                    print("本次淘汰页面：" + str(pageFrame[deleteIndex % frameNum]))
                    self.showDelete.append(pageFrame[deleteIndex % frameNum])
                    pageFrame[deleteIndex % frameNum] = pages[count]
                    deleteIndex += 1

                self.missNum += 1
                print("目前物理页框中页面走向为：", end="")
                t = 0
                for i in pageFrame:
                    print(i, end=" ")
                print()
                print()
            t = 0
            for p in pageFrame:
                self.dataContent[t][count] = p
                t += 1
            count = count + 1

        print("缺页次数：" + str(self.missNum) + "次")
        print("淘汰页面：", end="")
        print(self.pageDelete)

    def LRU(self, frameNum, pages):
        pageNum = len(pages)  # 页面请求数
        count = 0  # 当前计数
        isRoom = True  # 是否有空位
        pageFrame = [None for i in range(frameNum)]  # 初始化物理页框
        deleteIndex = 0  # FIFO替换页的索引

        self.missNum = 0
        self.pageDelete = list()
        self.showDelete = list()

        while count < pageNum:
            print("第" + str(count + 1) + "次：" + pages[count])

            # 判断物理页框中是否存在本次页面请求
            isExist = False
            for p in pageFrame:
                if pages[count] == p:
                    isExist = True
            if isExist:
                print("本次页面请求在物理页框中存在")
                print("目前物理页框中页面请求为：", end="")
                for p in pageFrame:
                    print(p, end=" ")
                print()
                print()
                self.showDelete.append('x')
            else:
                # 如果页面请求在物理页框中不存在
                # 判断物理页框中有无空位
                for p in pageFrame:
                    if not p:
                        isRoom = True
                        break
                    else:
                        isRoom = False

                if isRoom:  # 如果物理页框有空位
                    for n in range(frameNum):
                        if pageFrame[n] is None:
                            pageFrame[n] = pages[count]
                            break
                    self.showDelete.append('x')
                else:  # 如果物理框没有空位
                    # LRU
                    for n in range(len(pageFrame)):
                        if pages[count - int(frameNum)] == pageFrame[n]:
                            self.pageDelete.append(pageFrame[n])
                            self.showDelete.append(pageFrame[n])
                            pageFrame[n] = pages[count]

                self.missNum += 1
                print("目前物理页框中页面走向为：", end="")
                for i in pageFrame:
                    print(i, end=" ")
                print()
                print()
            t = 0
            for p in pageFrame:
                self.dataContent[t][count] = p
                t += 1
            count = count + 1

        print("缺页次数：" + str(self.missNum) + "次")
        print("淘汰页面：", end="")
        print(self.pageDelete)

    def OPT(self, frameNum, pages):
        pageNum = len(pages)  # 页面请求数
        count = 0  # 当前计数
        isRoom = True  # 是否有空位
        pageFrame = [None for i in range(frameNum)]  # 初始化物理页框
        deleteIndex = 0  # FIFO替换页的索引

        self.missNum = 0
        self.pageDelete = list()
        self.showDelete = list()

        while count < pageNum:
            print("第" + str(count + 1) + "次：" + pages[count])

            # 判断物理页框中是否存在本次页面请求
            isExist = False
            for p in pageFrame:
                if pages[count] == p:
                    isExist = True
            if isExist:
                print("本次页面请求在物理页框中存在")
                print("目前物理页框中页面请求为：", end="")
                for p in pageFrame:
                    print(p, end=" ")
                print()
                print()
                self.showDelete.append('x')
            else:
                # 如果页面请求在物理页框中不存在
                # 判断物理页框中有无空位
                for p in pageFrame:
                    if not p:
                        isRoom = True
                        break
                    else:
                        isRoom = False

                if isRoom:  # 如果物理页框有空位
                    for n in range(frameNum):
                        if pageFrame[n] is None:
                            pageFrame[n] = pages[count]
                            break
                    self.showDelete.append('x')
                else:  # 如果物理框没有空位
                    # OPT算法
                    # 总选择那些以后不再需要的或者将来最长时间之后才会用到的界面进行淘汰
                    isFuture = False  # 是否存在未来不再出现的元素
                    isFound = False  # 是否找到未来下标的元素
                    tmpIndex = 0  # 不在未来出现的下标
                    tmpList = list()
                    # ① 寻找当前物理页框是否有将来不再出现的页
                    for i in range(len(pageFrame)):
                        for j in range(count, pageNum):  # 仅查看未执行的
                            if pageFrame[i] == pages[j]:
                                tmpList.append(j)
                                isFound = True  # pageFrame[i]在未来会出现

                        # isFound = False 的情况，pageFrame[i]在未来不会出现
                        if not isFound:
                            tmpIndex = i  # 记录当前物理页框
                            isFuture = True  # 存在未来不再出现的元素
                            break
                        # 初始化isFound
                        isFound = False
                    # ②有将来不出现的页：直接删除 没有将来不出现的页：选择最长时间使用到的页进行替换
                    if isFuture:
                        # 直接淘汰将来不出现的页
                        self.pageDelete.append(pageFrame[tmpIndex])
                        self.showDelete.append(pageFrame[tmpIndex])
                        pageFrame[tmpIndex] = pages[count]

                    else:
                        # tmpList存储将来会用到的page列表下标，下标越大，说明越久才会被使用
                        # e.g. page = [2, 6, 8, 7, 4]  出现下标最大是4，显然page[4]最久才被使用
                        t = max(tmpList)
                        for i in range(len(pageFrame)):
                            if pageFrame[i] == pages[t]:
                                self.pageDelete.append(pageFrame[tmpIndex])
                                pageFrame[i] = pages[count]
                        self.showDelete.append('x')

                self.missNum += 1
                print("目前物理页框中页面走向为：", end="")
                t = 0
                for i in pageFrame:
                    print(i, end=" ")
                print()
                print()
            t = 0
            for p in pageFrame:
                self.dataContent[t][count] = p
                t += 1
            count = count + 1

        print("缺页次数：" + str(self.missNum) + "次")
        print("淘汰页面：", end="")
        print(self.pageDelete)

    def getData(self):
        return self.dataContent, self.missNum, self.pageDelete, self.showDelete





