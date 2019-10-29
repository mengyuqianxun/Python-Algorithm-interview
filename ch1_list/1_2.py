class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

#对不带头结点的单链表进行逆序
def RecursiveReverse(head):
    if head.next == None or head == None:
        return head
    else:
        newhead = RecursiveReverse(head.next)
        head.next.next = head   #!!
        head.next = None
    return newhead

#对带头节点的单链表进行逆序
def Reverse(head):
    if head ==None:
        return head
    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return head

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