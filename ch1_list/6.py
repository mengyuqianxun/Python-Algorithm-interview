class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def constructList():
    i = 1
    head =LNode(0)
    cur = head
    #构造链表
    while i<8:
        tmp = LNode(0)
        tmp.data = i
        tmp.next =None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = head.next.next.next  #构造环
    return head

#None：无环，否则有环并且返回slow与fast的相遇点
def isLoop(head):
    if head ==None or head.next == None:
        print
        return None
    
    slow = head.next
    fast = head.next
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None

#找出环的入口点:一个指针从链表头开始，一个指针从相遇点开始
def findLoopNode(head,meetNode):
    pointer1 = head.next
    pointer2 = meetNode
    while pointer1 != pointer2:  #一定会相遇
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

#因为列表有环，所以不能打印列表，会出现无限循环
if __name__ == "__main__":
    head = constructList()
    result = isLoop(head)
    if result != None:
        print(u"链表有环")
        loopNode = findLoopNode(head,result)
        print(u"环的入口点为" + str(loopNode.data))
    else:
        print(u"链表无环")