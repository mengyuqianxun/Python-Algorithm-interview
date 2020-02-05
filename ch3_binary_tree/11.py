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

def getMinNode(root):
    if root == None:
        return root
    while root.lchild != None:
        root = root.lchild
    return root

def getMaxNode(root):
    if root == None:
        return root
    while root.rchild != None:
        root = root.rchild
    return root

def findNode(root):
    maxNode = getMaxNode(root)
    minNode = getMinNode(root)
    mid = (maxNode.data + minNode.data)/2
    result = None
    while root != None:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root
            root = root.lchild
    return result

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    root = array2tree(arr,0,len(arr)-1)
    print(findNode(root).data)