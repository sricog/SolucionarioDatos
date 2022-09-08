#Listas Iguales 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def compare(l1: Node, l2: Node) -> bool:
    if count(l1) != count(l2):
        return False
    else:
        while(l1 != None and l2 != None):
            if l1.val != l2.val:
                return False
            else:
                l1 = l1.next 
                l2 = l2.next
        return True 

def count(head):
    if head == None:
        return 0 
    else:
        return 1 + count(head.next)
