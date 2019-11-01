class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def FindLastK(head,k):
    if head == None or head.next ==None:
        return head
    fast = head
    slow = head

    i =0
    while i<k and fast != None:
        fast = fast.next
        i+=1
    if i<k:
        return None
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow


if __name__=="__main__":
    i=1
    head = LNode(0)
    head.next = None
    tmp = None
    cur = head
    while i<8:
        tmp = LNode(0)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i+=1
    print(u'链表:',end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

    result = FindLastK(head,3)
    if result != None:
        print(u'\n链表倒数第3个元素为：'+ str(result.data))