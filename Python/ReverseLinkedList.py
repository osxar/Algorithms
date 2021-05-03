
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    
    prev = None
    current = head
    succ = None

    while(current):
        succ = current.next

        current.next = prev
        prev=current
        current = succ


    return prev

