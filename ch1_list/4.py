class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

#找出链表中间结点，把链表从中间断成两个子链表:快慢指针法,偶数偏右
def FindMiddleNode(head):
    if head == None or head.next == None:
        return head
    fast = head
    slow = head
    slowPre = head
    #当fast到链表尾时，slow恰好指向链表的中间结点
    while fast != None and fast.next != None:
        slowPre = slow
        slow = slow.next
        fast = fast.next.next
    slowPre.next = None  #如果是偶数  slowPre指向的是中间偏左的中点
    return slow #返回右半部分

#对不带头结点的单链表逆序
def Reverse(head):
    if head == None or head.next == None:
        return head
    cur = head.next
    pre = head
    pre.next = None
    while cur != None:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

def Reorder(head):
    if head == None or head.next == None or head.next.next == None:
        return
    #左半部分链表第一个结点
    cur1 = head.next
    #右半部分第一个结点
    mid = FindMiddleNode(head.next)
    cur2 = Reverse(mid)
    #合并
    tmp = None
    while cur1.next != None:
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp
        tmp = cur2.next
        cur2.next = cur1
        cur2 =tmp
    cur1.next =cur2

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
    print(u'排序前:',end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next

    Reorder(head)
    print(u"\n排序后:",end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next