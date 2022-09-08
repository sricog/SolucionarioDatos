#-----Solucion 1---------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(head1: Node, head2: Node) -> Node:
        if head1 is None:
            return head2   
        if head2 is None:
            return head1
        
        newHead= Node(-1)
        cur = newHead
        while head1 and head2:
            if head1.val >= head2.val:
                cur.next = head2
                head2 = head2.next
            else:
                cur.next = head1
                head1 = head1.next
            cur = cur.next
            
        if head1:
            cur.next = head1
            return newHead.next
        if head2:
            cur.next = head2
            return newHead.next
#-----Solucion 2------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(head1: Node, head2: Node) -> Node:
    if head1 is None: 
        return head2
        
    if head1.val <= head2.val:
        nuevo = Node(head1.val)
        return aux(head1.next,head2,nuevo,nuevo)
    else:
        nuevo = Node(head2.val)
        return aux(head1,head2.next,nuevo,nuevo)

def aux(head1,head2,newHead,linkedList):
    if head1 is None and head2 is None: return linkedList
    elif head1 is None:
        new = Node(head2.val)
        newHead.next = new
        aux(head1,head2.next,new,linkedList)
        return linkedList
    elif head2 is None:
        new = Node(head1.val)
        newHead.next = new
        aux(head1.next,head2,new,linkedList)
        return linkedList
    elif head1.val <= head2.val:
        new = Node(head1.val)
        newHead.next = new
        aux(head1.next,head2,new,linkedList)
        return linkedList
    else:
        new = Node(head2.val)
        newHead.next = new
        aux(head1,head2.next,new,linkedList)
        return linkedList
