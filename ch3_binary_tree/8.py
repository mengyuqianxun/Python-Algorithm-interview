class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

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

def creatDupTree(root):
    if root == None:
        return None
    dupTree = BiTNode()
    dupTree.data = root.data
    dupTree.lchild = creatDupTree(root.lchild)
    dupTree.rchild = creatDupTree(root.rchild)
    return dupTree

def printMidOrder(root):
    if root == None:
        return
    if root.lchild != None:
        printMidOrder(root.lchild)
    print(root.data,end = ' ')
    if root.rchild != None:
        printMidOrder(root.rchild)

if __name__ == "__main__":
    root1 =constructTree()
    root2 =creatDupTree(root1)
    print(u'原始二叉树中序遍历为：')
    printMidOrder(root1)
    print(u'\n复制后的二叉树中序遍历为：')
    printMidOrder(root2)
