class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

#对不带头结点的单链表进行翻转
def reverse(head):
    if head == None or head.next == None:
        return head
    pre = head
    cur = head.next
    pre.next = None
    while cur != None:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

def reverseK(head,k):
    if head == None or head.next == None or k<2:
        return
    i = 1
    pre = head
    begin = head.next
    while begin != None:
        end = begin
        while i<k:
            if end.next != None:
                end = end.next
            else:
                return
            i += 1
        p = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = p

        pre = begin
        begin = p
        i = 1

if __name__ == "__main__":
    i = 1
    head = LNode(0)
    cur = head
    while i<8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 1
    print(u"顺序输出：",end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next
    
    reverseK(head,3)
    print(u"逆序输出：",end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next 

