# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = self.get_value(l1)
        s2 = self.get_value(l2)
        s1 = s1[::-1]
        s2 = s2[::-1]
        add_int = int(s1) + int(s2)
        result = None
        for ch in str(add_int):
            node = ListNode(int(ch))
            if result:
                node.next = result
            result = node
        return result

    def get_value(self, l1):
        s1 = ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        return s1

        