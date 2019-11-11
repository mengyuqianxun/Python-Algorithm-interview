class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def ConstructList(start):
    i = start
    head = LNode(0)
    cur = head
    while i<8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 2
    return head

#打印带头结点的链表
def printList(head):
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

#两个顺序链表的合并    
def Merge(head1,head2):
    if head1 == None or head1.next == None:
        return head2
    if head2 == None or head2.next == None:
        return head1
    #构造两个遍历指针
    p1 = head1.next
    p2 = head2.next

    head = LNode(0)
    cur = head
    #寻找合并链表的起始点
    if p1.data <= p2.data:
        cur.next = p1
        cur = p1
        p1 = p1.next
    else:
        cur.next = p2
        cur = p2
        p2 = p2.next

    #找链表剩余结点的最小值并连接
    while p1 != None and p2 != None:
        if p1.data <= p2.data:
            cur.next = p1
            cur = p1
            p1 = p1.next
        else:
            cur.next = p2
            cur = p2
            p2 = p2.next
    #当遍历完一个链表后，把另外一个链表剩余的结点链接合并到后面的链表后面
    if p1 != None:
        cur.next = p1
    else:
        cur.next = p2
    return head

if __name__ == "__main__":
    #构造链表
    head1 = ConstructList(1)
    head2 = ConstructList(2)
    print(u"head1为:  ")
    printList(head1)
    print(u"\nhead2为:  ")
    printList(head2)

    head = Merge(head1,head2)
    print(u"\n合并后为：  ")
    printList(head)



