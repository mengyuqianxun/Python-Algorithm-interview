class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.data = None
        self.next = None
    #判断stack是否为空，如果为空返回true，否则返回false
    def empty(self):
        if self.next == None:
            return True
        else:
            return False
    #获取栈内元素个数
    def size(self):
        size = 0
        p = self.next
        while p != None:
            p = p.next
            size += 1
        return size
    #入栈
    def push(self,e):
        p = LNode(e)
        p.next = self.next
        self.next = p
    #出栈，同时返回栈顶元素
    def pop(self):
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
            return tmp.data
        else:
            print(u'栈已经为空')
            return None
    #取得栈顶元素
    def top(self):
        if self.next != None:
            return self.next.data
        else:
            print(u'栈已经为空')
            return None

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(u'栈顶元素为：'+str(stack.top()))
    print(u'栈大小为：'+str(stack.size()))
    stack.pop()
    print(u'弹栈成功')
    stack.pop()