from collections import deque

class LRU:
    def __init__(self,storgeSize):
        self.storgeSize = storgeSize
        self.queue = deque()
        self.hashSet = set()
    
    def isQueueFull(self):
        return len(self.queue) == self.storgeSize
    #把页号为pageNum的页缓存到队列中，同时也添加到Hash表中
    def enqueue(self,pageNum):
        #如果队列满，删除队尾的网页
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)
    #当访问一个page时候调用这个函数
    def accessPage(self,pageName):
        if pageName not in self.hashSet:
            self.enqueue(pageName)
        elif pageName != self.queue[0]:
            self.queue.remove(pageName)
            self.queue.appendleft(pageName)
    
    def printQueue(self):
        while len(self.queue)>0:
            print(self.queue.popleft(),end = ' ')


if __name__ == "__main__":
    lru = LRU(3)
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    lru.printQueue()
