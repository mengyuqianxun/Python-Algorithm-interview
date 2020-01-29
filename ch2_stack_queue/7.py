from collections import deque

class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.position = 0
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    def setPosition(self,position):
        self.position = position
    
    def toString(self):
        return("id:" + str(self.id) + "    name:" + self.name + "    position:" + str(self.position))
    
class MyQueue:
    def __init__(self):
        self.q = deque()
    #入队列
    def enQueue(self,e):
        e.setPosition(len(self.q)+1)
        self.q.append(e)
    #出队列
    def deQueue(self):
        self.q.popleft()
        self.updateSeq()
    #队内有人出队列
    def deQueueMove(self,e):
        self.q.remove(e)
        self.updateSeq()

    #更新队列中每个人的序列
    def updateSeq(self):
        i = 1
        for e in self.q:
            e.setPosition(i)
            i += 1
    
    def printList(self):
        for e in self.q:
            print(e.toString())
    
if __name__ =="__main__":
    u1 = User(1,"user1")
    u2 = User(2,"user2")
    u3 = User(3,"user3")    
    u4 = User(4,"user4")
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.deQueue()
    queue.deQueueMove(u3)
    queue.printList()    