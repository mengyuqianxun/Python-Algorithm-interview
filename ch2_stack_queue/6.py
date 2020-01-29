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


class MyStack:
    def __init__(self):
        self.A = Stack()#用来储存栈中元素
        self.B = Stack()
    def push(self,data):
        self.A.push(data)
    def pop(self):
        if self.B.isEmpty():
            while not self.A.isEmpty():
                self.B.push(self.A.pop())
        first = self.B.pop()
        return first

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    #队列中没有直接给出top()函数，而是通过pop()来获得队首元素
    print(u'队列首元素为：' + str(stack.pop()))
    print(u'队列首元素为：' + str(stack.pop()))


