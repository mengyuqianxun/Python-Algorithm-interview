class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

#打印带头结点的链表
def printList(head):
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

#给定单链表head中的某个结点，删除该结点
def RemoveNode(p):
    if p == None or p.next == None:
        return False
    p.data = p.next.data
    tmp = p.next
    p.next = tmp.next
    return True


if __name__ == "__main__":
    i = 1
    head = LNode(0)
    cur = head
    p = None
    while i <8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    print(u"删除节点"+str(p.data)+"前的链表:")
    printList(head)

    result = RemoveNode(p)

    if result:
        print(u"\n删除该节点后的链表:")
        printList(head)
    else:
        print(u"\n删除节点失败")



    


