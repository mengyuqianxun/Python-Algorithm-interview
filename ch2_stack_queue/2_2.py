class LNode():
    def __init__(self,x):
        self.data = x
        self.next = None

class MyQueue():
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
            self.pHead = self.pEnd =tmp
        else:
            self.pEnd.next = tmp
            self.pEnd = tmp
    