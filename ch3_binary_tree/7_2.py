import math

class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

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

class NodeNum:
    def __init__(self):
        self.num = None

#找出结点在二叉树中的编号
def getNum(root,node,number):
    if root == None:
        return False
    if root == node:
        return True
    tmp = number.num
    number.num = tmp*2
    if getNum(root.lchild,node,number):
        return True
    else:
        number.num = tmp*2 +1
        return getNum(root.rchild,node,number)

#根据编号找出对应的结点
def getNodeFromNum(root,number):
    if root == None or number<0:
        return None
    if number == 1:
        return root
    lens = int((math.log(number)/math.log(2)))
    number -= 1 <<lens
    while lens > 0:
        if (number>>(lens-1))%2 == 1:
            root = root.rchild
        else:
            root = root.lchild
        lens -= 1
    return root

def findParentNode(root,node1,node2):
    nodenum1 = NodeNum()
    nodenum2 = NodeNum()
    nodenum1.num = 1
    nodenum2.num = 1
    getNum(root,node1,nodenum1)
    getNum(root,node2,nodenum2)
    num1 = nodenum1.num
    num2 = nodenum2.num
    #找出编号为num1和num2的共同父结点
    while num1 != num2:
        if num1 > num2:
            num1 = int(num1/2)
        else:
            num2 = int(num2/2)
    return getNodeFromNum(root,num1)


if __name__ == "__main__":
    arr =[1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr,0,len(arr)-1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.rchild
    parent = findParentNode(root,node1,node2)
    if parent != None:
        print(str(node1.data) + u'和' + str(node2.data) + u'最近的公共父结点为'+ str(parent.data))
    else:
        print(u'没有公共结点')
