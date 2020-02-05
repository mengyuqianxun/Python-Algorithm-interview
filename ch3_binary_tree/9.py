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

def findRoad(root,num,sums,path):
    sums += root.data
    path.append(root.data)
    if root.lchild == None and root.rchild == None and sums == num:
        i = 0
        while i<len(path):
            print(path[i],end = ' ')
            i += 1
    if root.lchild != None:
        findRoad(root.lchild,num,sums,path)
    if root.rchild != None:
        findRoad(root.rchild,num,sums,path)
    sums -= path[-1]
    path.remove(path[-1])

if __name__ == "__main__":
    root = constructTree()
    s = []
    print(u'满足路径结点和等于8的路径为：')
    findRoad(root,8,0,s)

