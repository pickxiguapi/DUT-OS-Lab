# coding=utf-8
"""
    @author:Yuan Yi fu

    implement 先来先服务FCFS 轮转RR 最短进程优先SJF 最高响应比优先HRN
"""
from queue import Queue


class Scheduling(object):
    def __init__(self, name, processList):
        self.alName = name  # 应用的算法名称
        self.processList = processList

    def implement(self):
        aveC = 0
        aveVC = 0
        if self.alName == 'FCFS':
            aveC, aveVC = self.FCFS()
        elif self.alName == 'SJF':
            aveC, aveVC = self.SJF()
        elif self.alName == 'RR':
            aveC, aveVC = self.RR(1)
        elif self.alName == 'HRN':
            aveC, aveVC = self.HRN()

        return self.processList, aveC, aveVC

    def FCFS(self):
        # 对列表按照到达时间进行升序排序  x:x[1]为依照到达时间进行排序
        self.processList.sort(key=lambda x: x.arriveTime, reverse=False)
        # 计算开始时间和完成时间
        for i in range(len(self.processList)):
            if i == 0:  # 第一个执行的进程，从到达时间开始算起
                startTime = self.processList[i].arriveTime
                self.processList[i].startTime = startTime
                self.processList[i].finishTime = startTime + self.processList[i].serveTime

            elif i > 0 and self.processList[i-1].finishTime < self.processList[i].arriveTime:
                startTime = self.processList[i].arriveTime
                self.processList[i].startTime = startTime
                self.processList[i].finishTime = startTime + self.processList[i].serveTime

            else:
                startTime = self.processList[i-1].finishTime
                self.processList[i].startTime = startTime
                self.processList[i].finishTime = startTime + self.processList[i].serveTime

        # 计算周转时间和带权周转时间
        for i in range(len(self.processList)):
            self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
            self.processList[i].varCyclingTime = self.processList[i].cyclingTime / self.processList[i].serveTime

        # 计算平均周转时间和平均带权周转时间
        aveCyclingTime = 0
        aveVarCyclingTime = 0
        for i in range(len(self.processList)):
            aveCyclingTime += self.processList[i].cyclingTime
            aveVarCyclingTime += self.processList[i].varCyclingTime
        aveCyclingTime /= len(self.processList)
        aveVarCyclingTime /= len(self.processList)

        print("运行结果:")
        for i in range(len(self.processList)):
            print("时刻: %d 开始运行进程: %s    完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
                  % (self.processList[i].startTime, self.processList[i].name, self.processList[i].finishTime,
                     self.processList[i].cyclingTime, self.processList[i].varCyclingTime))
        print("本次调度的平均周转时间为： %.2f" % float(aveCyclingTime))
        print("本次调度的平均带权周转时间为： %.2f" % float(aveVarCyclingTime))
        return round(aveCyclingTime, 3), round(aveVarCyclingTime, 3)

    def SJF(self):
        # 对processList按照到达时间顺序排列
        self.processList.sort(key=lambda x: x.arriveTime, reverse=False)

        lastFinish = 0  # 初始化上个任务完成时间

        for i in range(len(self.processList)):
            if i == 0:
                # 到达时间最早的第一个进程一定最先执行（不考虑到达时间相同的情况）,不管他的服务时间有多长
                startTime = self.processList[0].arriveTime
                self.processList[0].startTime = startTime
                self.processList[0].finishTime = startTime + self.processList[0].serveTime
                self.processList[0].cyclingTime = self.processList[0].finishTime - self.processList[0].arriveTime
                self.processList[0].varCyclingTime = self.processList[0].cyclingTime / self.processList[0].serveTime

            else:
                # 设置一个等待队列WaitList，等待队列中按服务时间升序存放当前时刻已经到达的进程
                # 如果上一个进程执行完的时刻等待队列不为空，则选择服务时间最短的
                # 如果上一个进程执行完的时刻等待队列为空，则选择到达时间最接近的
                # 上个任务完成时间 > 到达时间的且没有被执行过的进程，存进WaitList
                WaitList = list()
                for j in range(i, len(self.processList)):
                    if lastFinish > self.processList[j].arriveTime:
                        WaitList.append(self.processList[j])

                if WaitList:
                    # WaitList不为空，选择WaitList中服务时间最短的
                    # 服务时间升序排列
                    WaitList.sort(key=lambda x: x.serveTime, reverse=False)  # 此时WaitList[0]为服务时间最短且已经到达的
                    for k in range(len(self.processList)):
                        if WaitList[0].name == self.processList[k].name:
                            del(self.processList[k])
                            break
                    self.processList.insert(i, WaitList[0])

                    startTime = lastFinish
                    self.processList[i].startTime = startTime
                    self.processList[i].finishTime = startTime + self.processList[i].serveTime
                    self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
                    self.processList[i].varCyclingTime = self.processList[i].cyclingTime / self.processList[i].serveTime

                else:
                    startTime = self.processList[i].arriveTime
                    self.processList[i].startTime = startTime
                    self.processList[i].finishTime = startTime + self.processList[i].serveTime
                    self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
                    self.processList[i].varCyclingTime = self.processList[i].cyclingTime / self.processList[i].serveTime

            lastFinish = self.processList[i].finishTime

        # 计算平均周转时间和平均带权周转时间
        aveCyclingTime = 0
        aveVarCyclingTime = 0
        for i in range(len(self.processList)):
            aveCyclingTime += self.processList[i].cyclingTime
            aveVarCyclingTime += self.processList[i].varCyclingTime
        aveCyclingTime /= len(self.processList)
        aveVarCyclingTime /= len(self.processList)

        print("运行结果:")
        for i in range(len(self.processList)):
            print("时刻: %d 开始运行进程: %s    完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
                    % (self.processList[i].startTime, self.processList[i].name, self.processList[i].finishTime,
                    self.processList[i].cyclingTime, self.processList[i].varCyclingTime))
        print("本次调度的平均周转时间为： %.2f" % float(aveCyclingTime))
        print("本次调度的平均带权周转时间为： %.2f" % float(aveVarCyclingTime))
        return round(aveCyclingTime, 3), round(aveVarCyclingTime, 3)

    def RR(self, time):
        # 时间片长度为time=1
        time = 1
        # 创建队列Q
        q = Queue()
        # 对列表按照到达时间进行升序排序  x:x[1]为依照到达时间进行排序
        self.processList.sort(key=lambda x: x.arriveTime, reverse=False)
        serveTime = [self.processList[i].serveTime for i in range(len(self.processList))]  # 备份serveTime列表
        tick = self.processList[0].arriveTime  # tick记录时间
        q.put(self.processList[0])
        self.processList[0].isImplement = True
        while not q.empty():
            # 取队首使用时间片
            tmp = q.get()
            tmp.serveTime -= 1

            # 下一个时间点，查看是否有新任务到达，如果有，入队新任务，最后再入队tmp
            tick += 1
            for i in range(len(self.processList)):
                if self.processList[i].isImplement:
                    continue
                if self.processList[i].arriveTime == tick:
                    q.put(self.processList[i])
                    self.processList[i].isImplemnt = True
                    break
            if tmp.serveTime:
                # 进程tmp没运行完
                q.put(tmp)
            else:
                # 进程tmp运行完
                for i in range(len(self.processList)):
                    if tmp == self.processList[i]:
                        self.processList[i].finishTime = tick

        for i in range(len(self.processList)):
            startTime = self.processList[i].finishTime - self.processList[i].serveTime
            self.processList[i].startTime = startTime
            self.processList[i].serveTime = serveTime[i]
            self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
            self.processList[i].varCyclingTime = self.processList[i].cyclingTime / self.processList[i].serveTime

        # 计算平均周转时间和平均带权周转时间
        aveCyclingTime = 0
        aveVarCyclingTime = 0
        for i in range(len(self.processList)):
            aveCyclingTime += self.processList[i].cyclingTime
            aveVarCyclingTime += self.processList[i].varCyclingTime
        aveCyclingTime /= len(self.processList)
        aveVarCyclingTime /= len(self.processList)

        print("运行结果:")
        for i in range(len(self.processList)):
            print("时刻: %d 开始运行进程: %s    完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
                  % (self.processList[i].startTime, self.processList[i].name, self.processList[i].finishTime,
                     self.processList[i].cyclingTime, self.processList[i].varCyclingTime))
        print("本次调度的平均周转时间为： %.2f" % float(aveCyclingTime))
        print("本次调度的平均带权周转时间为： %.2f" % float(aveVarCyclingTime))
        return round(aveCyclingTime, 3), round(aveVarCyclingTime, 3)

    def HRN(self):
        """
        和SJF算法的区别为SJF从WaitList选择服务时间最短的进程而HRN算法从WaitList选择 响应比Rp 最高的进程
        在SJF算法基础上做修改
        """
        # 对processList按照到达时间顺序排列
        self.processList.sort(key=lambda x: x.arriveTime, reverse=False)

        lastFinish = 0  # 初始化上个任务完成时间

        for i in range(len(self.processList)):
            if i == 0:
                # 到达时间最早的第一个进程一定最先执行（不考虑到达时间相同的情况）,不管他的服务时间有多长
                startTime = self.processList[0].arriveTime
                self.processList[0].startTime = startTime
                self.processList[0].finishTime = startTime + self.processList[0].serveTime
                self.processList[0].cyclingTime = self.processList[0].finishTime - self.processList[0].arriveTime
                self.processList[0].varCyclingTime = round(self.processList[0].cyclingTime / self.processList[0].serveTime, 3)

            else:
                # 设置一个等待队列WaitList，等待队列中按 响应比 升序存放当前时刻已经到达的进程
                # 如果上一个进程执行完的时刻等待队列不为空，则选择 响应比 最高的
                # 如果上一个进程执行完的时刻等待队列为空，则选择到达时间最接近的
                # 上个任务完成时间 > 到达时间的且没有被执行过的进程，存进WaitList
                WaitList = list()
                for j in range(i, len(self.processList)):
                    # 计算响应比
                    self.processList[j].Rp = (lastFinish - self.processList[j].arriveTime +
                                              self.processList[j].serveTime)/self.processList[j].serveTime
                    if lastFinish > self.processList[j].arriveTime:
                        WaitList.append(self.processList[j])

                if WaitList:
                    # WaitList不为空，选择WaitList中响应比最高的
                    # 按响应比降序排列
                    WaitList.sort(key=lambda x: x.Rp, reverse=True)  # 此时WaitList[0]为响应比最高且已经到达的
                    for k in range(len(self.processList)):
                        if WaitList[0].name == self.processList[k].name:
                            del (self.processList[k])
                            break
                    self.processList.insert(i, WaitList[0])

                    startTime = lastFinish
                    self.processList[i].startTime = startTime
                    self.processList[i].finishTime = startTime + self.processList[i].serveTime
                    self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
                    self.processList[i].varCyclingTime = round(self.processList[i].cyclingTime / self.processList[i].serveTime, 3)

                else:
                    startTime = self.processList[i].arriveTime
                    self.processList[i].startTime = startTime
                    self.processList[i].finishTime = startTime + self.processList[i].serveTime
                    self.processList[i].cyclingTime = self.processList[i].finishTime - self.processList[i].arriveTime
                    self.processList[i].varCyclingTime = round(self.processList[i].cyclingTime / self.processList[i].serveTime, 3)

            lastFinish = self.processList[i].finishTime

        # 计算平均周转时间和平均带权周转时间
        aveCyclingTime = 0
        aveVarCyclingTime = 0
        for i in range(len(self.processList)):
            aveCyclingTime += self.processList[i].cyclingTime
            aveVarCyclingTime += self.processList[i].varCyclingTime
        aveCyclingTime /= len(self.processList)
        aveVarCyclingTime /= len(self.processList)

        print("运行结果:")
        for i in range(len(self.processList)):
            print("时刻: %d 开始运行进程: %s    完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
                  % (self.processList[i].startTime, self.processList[i].name, self.processList[i].finishTime,
                     self.processList[i].cyclingTime, self.processList[i].varCyclingTime))
        print("本次调度的平均周转时间为： %.2f" % float(aveCyclingTime))
        print("本次调度的平均带权周转时间为： %.2f" % float(aveVarCyclingTime))
        return round(aveCyclingTime, 3), round(aveVarCyclingTime, 3)







