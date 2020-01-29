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
        self.elemStack = Stack()
        self.minStack = Stack()
    def push(self,data):
        self.elemStack.push(data)
        #更新保存最小元素的栈
        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if data <= self.minStack.top():
                self.minStack.push(data)
    def pop(self):
        topData = self.elemStack.top()
        self.elemStack.pop()
        if topData == self.mins():
            self.minStack.pop()
        return topData
    def mins(self):
        if self.minStack.isEmpty():
            return 0
        else:
            return self.minStack.top()
    
if __name__ == "__main__":
    stack = MyStack()
    stack.push(5)
    print(u"栈中最小值为:"+str(stack.mins()))
    stack.push(6)
    print(u"栈中最小值为:"+str(stack.mins()))
    stack.push(2)
    print(u"栈中最小值为:"+str(stack.mins()))
    stack.pop()
    print(u"栈中最小值为:"+str(stack.mins()))


