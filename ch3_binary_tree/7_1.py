import math

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

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

def array2tree(arr,start,end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = math.floor((start + end +1)/2)
        root.data = arr[mid]
        root.lchild = array2tree(arr,start,mid-1)
        root.rchild = array2tree(arr,mid+1,end)
    else:
        root =None
    return root

def getPathFromRoot(root,node,path_stack):
    if root == node:
        path_stack.push(root)
        return True
    if root == None:
        return False
    if getPathFromRoot(root.lchild,node,path_stack) or getPathFromRoot(root.rchild,node,path_stack):
        path_stack.push(root)
        return True
    else:
        return False

def findParentNode(root,node1,node2):
    stack1 = Stack()
    stack2 = Stack()
    getPathFromRoot(root,node1,stack1)
    getPathFromRoot(root,node2,stack2)
    
    parent = None
    while stack1.top() == stack2.top():
        parent = stack1.top()
        stack1.pop()
        stack2.pop()
    return parent
        
if __name__ == "__main__":
    arr =[1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr,0,len(arr)-1)
    node1 = root.lchild.lchild.lchild
    node2 = root.rchild
    parent = findParentNode(root,node1,node2)
    if parent != None:
        print(str(node1.data) + u'和' + str(node2.data) + u'最近的公共父结点为'+ str(parent.data))
    else:
        print(u'没有公共结点')
