class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def add(h1,h2):
    if h1 ==None or h1.next == None:
        return h2
    if h2 ==None or h2.next == None:
        return h1
    
    plus = 0    #记录进位
    sum = 0     #用来记录加和

    pointer1 = h1.next  #遍历h1
    pointer2 = h2.next  #遍历h2

    h3 = LNode(0)
    h3.next = None
    p = h3  #用于指向新创建的存储加和的结点

    while pointer1 != None and pointer2 != None:
        sum = pointer1.data + pointer2.data + plus
        if sum >= 10:
            sum = sum%10
            plus = 1
        else:
            plus = 0
        tmp = LNode(0)
        tmp.data = sum

        p.next = tmp
        p = tmp

        pointer1 = pointer1.next
        pointer2 = pointer2.next

    #链表h1比h2短
    if pointer1 == None:
        sum = pointer2.data + plus
        if sum >= 10:
            sum = sum%10
            plus = 1
        else:
            plus = 0
        tmp = LNode(0)
        tmp.data = sum

        p.next = tmp
        p = tmp
        pointer2 = pointer2.next

    #链表h1比h2长
    if pointer2 == None:
        sum = pointer1.data + plus
        if sum >= 10:
            sum = sum%10
            plus = 1
        else:
            plus = 0
        tmp = LNode(0)
        tmp.data = sum

        p.next = tmp
        p = tmp
        pointer1 = pointer1.next

    #如果计算完还有进位，则增加新的结点
    if plus == 1:
        tmp = LNode(0)
        tmp.data = 1
        p.next = tmp
    return h3

if __name__=="__main__":
    i=1
    head1 = LNode(0)
    head1.next = None
    head2 = LNode(0)
    head2.next = None

    tmp = None
    addResult =None
    #构造第一个链表
    cur =head1
    while i<7:
        tmp = LNode(0)
        tmp.data = i+2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i+=1
    #构造第二个链表
    cur = head2
    i = 9
    while i>4:
        tmp = LNode(0)
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i-=1

    print('Head1:',end = "  ")
    cur = head1.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

    print('\nHead2:',end = "  ")
    cur = head2.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

    print(u"\n相加后:",end = "  ")
    addResult = add(head1,head2)
    cur = addResult.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next