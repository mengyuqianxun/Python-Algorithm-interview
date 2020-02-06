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
        root = None
    return root

class MaxPath:
    def __init__(self):
        self.dis = None

def findMaxPath(root,max):
    if root == None:
        return 0
    sumLeft = findMaxPath(root.lchild,max)
    sumRight = findMaxPath(root.rchild,max)
    if sumLeft >= 0 and sumRight >= 0: 
        tmpMax = root.data + sumLeft + sumRight
    elif sumLeft < 0 and sumRight < 0:
        tmpMax = root.data
    elif sumRight < 0:
        tmpMax = root.data + sumLeft
    else:
        tmpMax = root.data + sumRight
    if tmpMax > max.dis:
        max.dis = tmpMax
    if sumLeft > sumRight:
        subMax = sumLeft
    else:
        subMax = sumRight
    return root.data + subMax

def disMaxPath(root):
    max = MaxPath()
    max.dis = -2**10
    findMaxPath(root,max)
    return max.dis

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    root = array2tree(arr,0,len(arr)-1)
    print(disMaxPath(root))


        