#单链表数据结构
class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def Reverse(head):
    #判断链表是否为空
    if head.next == None or head.next.next == None:
        return
    pre = None
    cur = None
    nex = None
    #链表首结点变为尾结点
    cur = head.next
    nex = cur.next
    cur.next = None
    pre = cur
    cur = nex
    #使当前遍历到的结点cur指向其前驱节点
    while cur.next != None:
        nex = cur.next
        cur.next = pre    #!!!
        pre = cur
        cur = nex

    #链表最后一个结点指向倒数第二个结点
    cur.next = pre
    #头结点指向原来链表的尾结点
    head.next = cur

if __name__=="__main__":
    i = 1
    head = LNode(0)
    
    cur = head
    #构造单链表
    while i<8:
        tmp = LNode(i)

        cur.next = tmp
        cur = tmp
        i += 1
    print(u'逆序前:',end = "  ")
    cur = head.next
    while cur !=None:
        print(cur.data,end = "  ")
        cur = cur.next

    print(u"\n逆序后:",end = "  ")
    Reverse(head)
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next