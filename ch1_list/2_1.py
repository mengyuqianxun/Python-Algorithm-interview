class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def Delete(head):
    if head == None or head.next ==None:
        return
    innerCur = None
    innerPre = None

    outerCur = head.next
    while outerCur != None:
        innerCur = outerCur.next
        innerPre = outerCur

        while innerCur != None:
            if outerCur.data == innerCur.data:
                innerPre.next =innerCur.next
                innerCur =innerCur.next
            else:
                innerPre = innerCur
                innerCur = innerCur.next
        outerCur = outerCur.next

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