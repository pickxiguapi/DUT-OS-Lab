# coding=utf-8
"""
   @author: Yuan Yi fu
   create Process class
"""


class Process(object):
    def __init__(self, name, arriveTime, serveTime):
        self.name = name
        self.arriveTime = arriveTime  # 到达时间
        self.serveTime = serveTime  # 服务时间
        self.startTime = 0  # 开始时间
        self.finishTime = 0  # 结束时间
        self.cyclingTime = 0  # 周转时间
        self.valCyclingTime = 0  # 带权周转时间

        self.isImplement = False  # 是否被执行，在RR算法中用到
        self.Rp = -1  # 响应比，在HRN算法中用到
