class LNode():
    def __init__(self,x):
        self.data = x
        self.next = None

def reverse(head):
    if head == None or head.next == None:
        return
    cur = head.next #当前遍历结点
    pre = head  #当前结点的前驱结点
    while cur != None and cur.next !=None:
        nex = cur.next.next
        pre.next = cur.next
        pre.next.next = cur #或者cur.next.next = cur
        cur.next = nex
        pre = cur
        cur = nex


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
    
    reverse(head)
    print(u"逆序输出：",end = "  ")
    cur = head.next
    while cur != None:
        print(cur.data,end = "  ")
        cur = cur.next
    