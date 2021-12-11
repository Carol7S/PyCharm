import sys
from module.Task import Task
from module.Process import ProcessStatus,Process
import random


tasks = []
ReadyNum = 0
CoresNum = int(sys.argv[1])  # 核心数
ProcessesNum = int(sys.argv[2]) # 进程数  作业数
schedulePolicy = int(sys.argv[3]) # 时间策略


# cpu
class cpu():
    def __init__(self):
        self.currentTime=0
    def addTime(self):
        self.currentTime+=1

# 策略
class Policy():
    NonPreemptive = 1  # 非抢占式
    DPPAA = 2  # dynamic priority priority algorithm  # 动态优先权优先算法



if CoresNum < 1:
    raise ("ERROR numOfCores")
if ProcessesNum < 1:
    raise ("ERROR numOfProcesses")
if not schedulePolicy in [1,2]:
    raise ("ERROR schedulePolicy")


formatStr = "{:<20}"*8

def checkAll():
    # 检查进程是否全部完成
    for task in tasks:
        if task.process.status != ProcessStatus.COMPLETED:
            return True
    return False

def printStatus():
    flag = True
    Print = tasks.copy()
    Print.sort(key=lambda x: x.process.ID)
    for task in Print:
        if(task.process.status != ProcessStatus.NOTEXIST):
            if(flag):
                print("Time: %d"%cpu.currentTime)
                print(formatStr.format(
                    "Process ID",
                    "Arrival Time",
                    "Costed Time",
                    "Required Time",
                    "Status",
                    "Time Wait For Block",
                    "Time Wait For Ready",
                    "Priority"
                ))
                flag=False
            print(formatStr.format(
                task.process.ID,
                task.process.arrivalTime,
                task.process.costedTime,
                task.process.requiredTime,
                ["BLOCKING","READY","RUNNING","COMPLETED"][task.process.status],
                task.process.timeWaitForBlock,
                task.process.timeWaitForReady,
                task.priority
            ))
    if(flag):
        print("Waiting......")



if __name__ == '__main__':
    cpu = cpu()
    # 初始化进程
    for i in range(ProcessesNum):
        tasks.append(Task(Process(cpu, i,random.randint(10, 30), random.randint(10, 30), random.randint(10, 30)),
                          random.randint(0, 30))) # Priority
    while (checkAll()):
        # 如果进程没有全部完成，就一直循环
        for task in tasks:
            if task.process.status == ProcessStatus.READY:
                # 如果进程是准备状态，优先度+5
                    task.priority += 5  # p1
            elif task.process.status == ProcessStatus.RUNNING:
                # 如果进程是运行状态，优先度-2
                task.priority -= 2  # p2
                if(task.priority<0):
                    task.priority=0
        tasks.sort(key=lambda x: x.priority,reverse = True)  # 根据优先度排序
        # run
        if schedulePolicy == Policy.NonPreemptive: # 如果算法策略是非抢占式
            RunningNum = 0
            for task in tasks:
                if task.process.status == ProcessStatus.RUNNING:  # 如果这个进程正在运行
                    RunningNum+=1
                    task.process.costedTime+=1  # 花费的时间++
            addNumber = min(CoresNum - RunningNum,ReadyNum) # 核心数-运行数，准备数，查看是否有空闲的核心可以用来运行进程
            for i in range(addNumber):
                for task in tasks:
                    if(task.process.status == ProcessStatus.READY):
                        task.process.status = ProcessStatus.RUNNING
                        task.process.costedTime+=1
                        break
            ReadyNum -= addNumber
            RunningNum += addNumber


        elif schedulePolicy == Policy.DPPA: # 如果是DPPA式
            for task in tasks:
                if task.process.status == ProcessStatus.RUNNING:
                    task.process.status = ProcessStatus.READY
                    ReadyNum+=1
            for i in range(min(CoresNum,ReadyNum)):
                for task in tasks:
                    if task.process.status == ProcessStatus.READY:
                        task.process.status = ProcessStatus.RUNNING
                        task.process.costedTime+=1
                        break

        # 一个时间片完成
        for task in tasks:
            if task.process.requiredTime == task.process.costedTime:
                # 如果花费时间等于所需时间，完成进程
                task.process.status = ProcessStatus.COMPLETED
            elif task.process.status == ProcessStatus.NOTEXIST and cpu.currentTime >= task.process.timeWaitForBlock :
                # 如果不存在，就进入堵塞状态
                task.process.arrivalTime = cpu.currentTime  # 进入cpu时间
                task.process.status = ProcessStatus.BLOCKING
            elif task.process.status == ProcessStatus.BLOCKING and cpu.currentTime >= task.process.arrivalTime + task.process.timeWaitForReady:
                # 等待时间结束，可以进入准备状态
                task.process.status = ProcessStatus.READY
                ReadyNum+=1

        printStatus()
        # time++
        cpu.addTime()

