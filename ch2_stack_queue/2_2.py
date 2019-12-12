class LNode():
    def __init__(self,x):
        self.data = x
        self.next = None

class Queue():
    def __init__(self):
        self.pHead = None
        self.pEnd = None
    #判断队列是否为空
    def isEmpty(self):
        return self.pHead == self.pEnd
    #获取栈中元素个数
    def size(self):
        size = 0
        p = self.pHead
        while p != None:
            p = p.next
            size += 1
        return size
    #入队列
    def enQueue(self,e):
        tmp = LNode(e)
        if self.pHead == None:
            self.pHead = self.pEnd = tmp
        else:
            self.pEnd.next = tmp
            self.pEnd = tmp
    #出队列，删除列首元素
    def deQueue(self):
        if self.pHead == None:
            print(u"出队列失败，队列已为空")
            return 
        else:
            self.pHead = self.pHead.next
    #查看队列首元素
    def getFront(self):
        if self.pHead == 0:
            print(u"队列为空")
        else:
            return self.pHead.data
    #查看队列尾元素
    def getBack(self):
        if self.pEnd == 0:
            print(u"队列为空")
        else:
            return self.pEnd.data

if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(1)
    queue.enQueue(2)
    print(u'队列头元素为：'+str(queue.getFront()))
    print(u'队列尾元素为:'+str(queue.getBack()))
    print(u'队列大小为:'+str(queue.size()))