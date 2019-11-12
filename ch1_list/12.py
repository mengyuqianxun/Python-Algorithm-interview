class LNode:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down = None

class MergeList:
    def __init__(self):
        self.head = None
    
    #将data插入链表头
    def insert(self,head_ref,data):
        tmp = LNode(data)
        tmp.down = head_ref
        head_ref = tmp
        return head_ref

    #用来合并两个有序的链表
    def merge(self,a,b):
        if a == None:
            return b
        if b == None:
            return a
        #将两个链表头中的较小的结点赋值给result
        if a.data < b.data:
            result = a
            result.down = self.merge(a.down,b)
        else:
            result = b
            result.down = self.merge(a,b.down)
        return result
    
    #将链表扁平化处理
    def flatten(self,p):
        if p == None or p.right == None:
            return p
        p.right = self.flatten(p.right)
        p = self.merge(p,p.right)
        return p

    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data,end = "  ")
            tmp = tmp.down
        print("\n")

if __name__ == "__main__":
    L = MergeList()
    #构造链表
    L.head = L.insert(L.head,31)
    L.head = L.insert(L.head,8)
    L.head = L.insert(L.head,6)
    L.head = L.insert(L.head,3)
    L.head.right = L.insert(L.head.right,21)
    L.head.right = L.insert(L.head.right,11)
    L.head.right.right  = L.insert(L.head.right.right,50)
    L.head.right.right  = L.insert(L.head.right.right,22)
    L.head.right.right  = L.insert(L.head.right.right,15)
    L.head.right.right.right  = L.insert(L.head.right.right.right,55)
    L.head.right.right.right  = L.insert(L.head.right.right.right,40)
    L.head.right.right.right  = L.insert(L.head.right.right.right,39)
    L.head.right.right.right  = L.insert(L.head.right.right.right,30)
    #扁平化链表
    L.head = L.flatten(L.head)
    L.printList()
