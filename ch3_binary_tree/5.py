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

class Test:
    def __init__(self):
        self.pHead = None
        self.pEnd = None
    
    def BiT2List(self,root):
        if root == None:
            return
        #转换root的左子树
        self.BiT2List(root.lchild)
        root.lchild = self.pEnd
        if self.pEnd == None:
            self.pHead = root
        else:
            self.pEnd.rchild = root
        self.pEnd = root
        self.BiT2List(root.rchild)


if __name__ == "__main__":
    arr =[1,2,3,4,5,6,7]
    root = array2tree(arr,0,len(arr)-1)

    test = Test()
    print(u'双向链表正向遍历：')
    test.BiT2List(root)
    cur = test.pHead
    while cur != None:
        print(cur.data,end = ' ')
        cur = cur.rchild
    print('\n'+u'转换后双向链表逆向遍历：')
    cur = test.pEnd
    while cur != None:
        print(cur.data,end = ' ')
        cur = cur.lchild
    
    

