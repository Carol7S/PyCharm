class ProcessStatus():
    NOTEXIST = -1 # 未创建
    BLOCKING = 0 # 堵塞
    READY = 1 # 准备
    RUNNING = 2 # 运行
    COMPLETED = 3 # 完成

class Process:
    def __init__(self, cpu , ID , requiredTime , timeWaitForReady, timeWaitForBlock):
        self.status = ProcessStatus.NOTEXIST #状态
        self.cpu = cpu  # cpu
        self.ID = ID #进程id
        self.arrivalTime = self.cpu.currentTime  # 进入时间
        self.costedTime = 0  # 已花费时间
        self.requiredTime = requiredTime  # 完成所需要的时间
        self.timeWaitForReady = timeWaitForReady  # 进入准备所需的时间
        self.timeWaitForBlock = timeWaitForBlock  # 进入堵塞状态所需的时间
