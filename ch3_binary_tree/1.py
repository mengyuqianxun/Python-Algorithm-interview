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

#中序遍历打印二叉树的结点内容
def printTreeMidOrder(root):
    if root == None:
        return None
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data,end = ' ')
    if root.rchild != None:
        printTreeMidOrder(root.rchild)

if __name__ =="__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(u'数组为:')
    i = 0
    while i<len(arr):
        print(arr[i],end = ' ')
        i += 1
    print('\n'+u'树的中序遍历为:')

    root = array2tree(arr,0,len(arr)-1)
    printTreeMidOrder(root)


