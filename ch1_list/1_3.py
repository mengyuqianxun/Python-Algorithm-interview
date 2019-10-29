class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def Reverse(head):
    if head == None or head.next == None:
        return 
    cur = None  #当前结点
    nex = None  #后继结点

    cur = head.next.next
    #尾结点指向None
    head.next.next = None
    
    while cur != None:
        nex = cur.next
        cur.next = head.next
        head.next = cur
        cur = nex
    

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