class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def isAfterOrder(arr,start,end):
    if arr == None:
        return False
    root = arr[end]
    i = start
    while i<end:
        if(arr[i]>root):
            break
        i += 1
    j = i
    while j<end:
        if arr[j]<root:
            return False
        j += 1
    leftpart = True
    rightpart = True
    if i>start:
        leftpart = isAfterOrder(arr,start,i-1)
    if j<end:
        rightpart = isAfterOrder(arr,i,end)
    return leftpart and rightpart

if __name__ == "__main__":
    arr = [1,3,2,5,7,6,4]
    result = isAfterOrder(arr,0,len(arr)-1)
    i = 0
    while i<len(arr):
        print(arr[i],end=' ')
        i += 1
    if result:
        print(u'是某一二元查找树的后序遍历序列')
    else:
        print(u'不是某一二元查找树的后序遍历序列')
    

