class Queue:
    def __init__(self):
        self.array=[]
        self.front=0
        self.rear=0
    #判断队列是否为空
    def isEmpty(self):
        return self.front == self.rear
    #返回队列大小
    def size(self):
        return self.rear-self.front
    #返回队列首元素
    def getFront(self):
        if self.isEmpty():
            return None
        return self.array[self.front]
    #返回队列尾元素
    def getBack(self):
        if self.isEmpty():
            return None
        return self.array[self.rear-1]
    #删除队列头元素
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
        else:
            print(u'队列为空')
    #把新元素加入队列尾
    def enQueue(self,item):
        self.array.append(item)
        self.rear += 1
    
if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(1)
    queue.enQueue(2)
    print(u'队列头元素为：'+str(queue.getFront()))
    print(u'队列尾元素为:'+str(queue.getBack()))
    print(u'队列大小为:'+str(queue.size()))