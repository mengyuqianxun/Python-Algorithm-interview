class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.maxSum = -2**31
    
    def findMaxSubTree(self,root,maxRoot):
        if root == None:
            return 0
        lmax = self.findMaxSubTree(root.lchild,maxRoot)
        rmax = self.findMaxSubTree(root.rchild,maxRoot)
        sums = lmax + rmax + root.data
        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.data = root.data
        return sums

def constructTree():
    root = BiTNode()
    node1 = BiTNode()
    node2 = BiTNode()
    node3 = BiTNode()
    node4 = BiTNode()
    root.data =6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = 9
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    return root

if __name__ == "__main__":
    root = constructTree()
    test = Test()
    maxRoot = BiTNode()
    maxRoot.data = 0
    test.findMaxSubTree(root,maxRoot)
    print(u'最大子树和为：'+str(test.maxSum))
    print(u'对应子树的根结点为：'+str(maxRoot.data))







