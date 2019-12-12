class Stack:
    #模拟栈
    def __init__(self):
        self.items=[]
    #判断栈是否为空
    def isEmpty(self):
        return len(self.items)==0
    #返回栈的大小
    def size(self):
        return len(self.items)
    #返回栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None
    #弹栈
    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            print(u"栈已经为空")
            return None
    #压栈
    def push(self,item):
        self.items.append(item)

#判断是否是出栈序列
def isPopSeries(push,pop):
    s = Stack()
    pushLen = len(push)
    popLen = len(pop)
    if pushLen != popLen:
        return False
    pushIndex = 0
    popIndex = 0
    while pushIndex < pushLen:
        s.push(push[pushIndex])
        pushIndex += 1
        while (not s.isEmpty()) and s.top() == pop[popIndex]:
            s.pop()
            popIndex += 1
    return s.isEmpty() and popIndex == popLen

if __name__ == "__main__":
    push = "12345"
    pop ="32541"
    if isPopSeries(push,pop):
        print(u'pop是push的一个pop序列')
    else:
        print(u'pop不是push的一个pop序列')