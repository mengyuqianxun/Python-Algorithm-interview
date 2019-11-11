class LNode():
    def __init__(self,x):
        self.data = x
        self.next = None

#判断带头结点链表是否相交，若相交返回相交结点，若不相交返回None
def IsIntersect(h1,h2):
    #n1,n2不包含头结点,所以寻找相交从head.next开始
    cur1 = h1
    p1 = None
    n1 = 0
    while cur1.next != None:
        cur1 = cur1.next
        n1 += 1
    p1 = cur1

    cur2 = h2
    p2 = None
    n2 = 0
    while cur2.next != None:
        cur2 = cur2.next
        n2 += 1
    p2 = cur2

    if p1 == p2:
        p = None
        cur1 = h1.next
        cur2 = h2.next
        i = 0
        if n1 >= n2:
            while i<(n1-n2):
                cur1 = cur1.next
                i += 1
            while i < n1:
                if cur1 == cur2:
                    p = cur1
                    return p
                cur1 = cur1.next
                cur2 = cur2.next
        else:
            while i<(n2-n1):
                cur2 = cur2.next
                i += 1
            while i < n2:
                if cur1 == cur2:
                    p = cur1
                    return p
                cur1 = cur1.next
                cur2 = cur2.next
    else:
        return None

if __name__ == "__main__":
    #构造第一个链表
    head1 = LNode(0)
    p = None
    cur = head1

    i = 1
    while i<8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    #构造第二个链表
    head2 = LNode(0)
    cur = head2

    i = 1
    while i<5:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = p

    result = IsIntersect(head1,head2)
    if result == None:
        print(u"两个链表没有交叉")
    else:
        print(u"两个链表有交叉,交叉点为："+str(result.data))