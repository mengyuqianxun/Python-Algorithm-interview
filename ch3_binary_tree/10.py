from collections import deque
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
        mid = int((start + end +1)/2)
        root.data = arr[mid]
        root.lchild = array2tree(arr,start,mid-1)
        root.rchild = array2tree(arr,mid+1,end)
    else:
        root =None
    return root

def printTreeLayer(root):
    if root == None:
        return None
    
    queue = deque()
    queue.append(root)
    while len(queue) > 0 :
        p = queue.popleft()
        print(p.data,end=' ')
        if p.lchild != None:
            queue.append(p.lchild)
        if p.rchild != None:
            queue.append(p.rchild)

def reverseTree(root):
    if root == None:
        return
    reverseTree(root.lchild)
    reverseTree(root.rchild)
    tmp = root.lchild
    root.lchild = root.rchild
    root.rchild = tmp

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9,10]
    root = array2tree(arr,0,len(arr)-1)
    print(u'树的层序遍历为：')
    printTreeLayer(root)
    reverseTree(root)
    print(u'\n反转后的二叉树层序遍历结果为：')
    printTreeLayer(root)
