class AVLtree:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        self.height  = self.count = 1
    
class Sort:
    #中序遍历AVL树，把遍历结果放入到数组中
    def inOrder(self,arr,root,index):
        if root != None:
            index = self.inOrder(arr,root.left,index)
            i = 0
            while i < root.count:
                arr[index] = root.data
                index += 1
                i += 1
            index = self.inOrder(arr,root.right,index)
        return index
    
    #得到树的高度
    def getHight(self,node):
        if node == None:
            return 0
        else:
            return node.height

    #把以y为根的子树向右旋转
    def rightRotate(self,y):
        x = y.left
        T2 = x.right
        y.left = T2
        y.height = max(self.getHight(y.left),self.getHight(y.right)) + 1
        x.height = max(self.getHight(x.left),self.getHight(x.right)) + 1
        return x
    
    #把以x为根的子树向右旋转
    def leftRotate(self,x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.getHight(x.left),self.getHight(x.right)) + 1
        y.height = max(self.getHight(y.left),self.getHight(y.right)) + 1
        return y
    
    def getBalance(self,N):
        if N == None:
            return 0
        return self.getHight(N.left) - self.getHight(N.right)

    def insert(self,root,data):
        if root == None:
            return AVLtree(data)
        if data == root.data:
            root.count += 1
            return root
        if data < root.data:
            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)
        #插入新的结点后更新root结点的高度
        root.height = max(self.getHight(root.left),self.getHight(root.right)) + 1
        #获取树的平衡因子
        balance = self.getBalance(root)
        #如果树不平衡，进行调整
        #LL型
        if balance > 1 and data < root.left.data:
            return self.rightRotate(root)
        #RR型
        elif balance < -1 and data > root.right.data:
            return self.leftRotate(root)
        #LR型
        elif balance > 1 and data > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        #RL型
        elif balance < -1 and data < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def sort(self,arr):
        root = None
        n = len(arr)
        i = 0
        while i < n:
            root = self.insert(root,arr[i])
            i += 1
        index = 0
        self.inOrder(arr,root,index)

if __name__ == "__main__":
    arr = [15,12,15,2,2,12,2,3,12,100,3,3]
    s = Sort()
    s.sort(arr)
    i = 0
    while i < len(arr):
        print(arr[i],end = ' ')
        i += 1