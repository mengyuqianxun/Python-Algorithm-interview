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

#把栈底元素移动到栈顶
def moveBottomToTop(s):
    if s.isEmpty():
        return
    top1 = s.top()
    s.pop()
    if not s.isEmpty():
        #递归处理不包含栈顶元素的子栈
        moveBottomToTop(s)
        top2 = s.top()
        s.pop()
        #交换栈顶元素与子栈栈顶元素
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)

def reverse_stack(s):
    if s.isEmpty():
        return
    moveBottomToTop(s)
    top1 = s.top()
    s.pop()
    reverse_stack(s)
    s.push(top1)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    reverse_stack(s)
    print(u"翻转后出栈顺序为")
    while not s.isEmpty():
        print(s.top())
        s.pop()