# l1 = [2,4,3]
# l2 = [5,6,4]

# fi = int(''.join(map(str, l1[::-1]))) + int(''.join(map(str, l2[::-1])))
# result = ([int(i) for i in str(fi)][::-1])


# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        li1 = []
        li2 = []
        while l1:
            li1.append(l1.val)
            l1 = l1.next
        while l2:
            li2.append(l2.val)
            l2 = l2.next
        fi = int(''.join(map(str, li1[::-1]))) + int(''.join(map(str, li2[::-1])))
        result = [int(i) for i in str(fi)][::-1]
        head = ListNode(result[0])
        current = head
        for i in result[1:]:
            current.next = ListNode(i)
            current = current.next
        return head



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


print(Solution().addTwoNumbers(l1, l2))