class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def DeleteRecursion(head):
    if head.next == None:
        return head
    pointer = None #定义head.next中的指针
    head.next = DeleteRecursion(head.next)

    pointer = head.next
    pre = head  #pre为pointer的前驱，用于删除操作
    #找出head.next为首的子链表中与head结点相同的结点并删除
    while pointer != None:
        if head.data == pointer.data:
            pre.next = pointer.next
            pointer = pointer.next
        else:
            pointer = pointer.next
            pre = pre.next
    return head

def Delete(head):
    if head == None:
        return
    head.next = DeleteRecursion(head.next)

if __name__=="__main__":
    i=1
    head = LNode(0)
    head.next = None

    tmp = None
    cur = head
    while i<7:
        tmp = LNode(0)
        if i%2 ==0:
            tmp.data = i+1
        elif i%3 == 0:
            tmp.data = i-2
        else:
            tmp.data =i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i+=1

    print(u'删除重复结点前:',end = "  ")
    cur = head.next
    while cur !=None:
        print(cur.data,end = "  ")
        cur = cur.next

    print(u"\n删除重复结点后:",end = "  ")

    Delete(head)
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next