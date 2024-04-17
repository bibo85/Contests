# time complexity - O(n + m)
# space complexity - O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        l = ListNode()
        head = l

        i = 0
        while list1 and list2:

            if i > 0:
                l.next = ListNode()
                l = l.next

            if list1.val > list2.val:
                l.val = list2.val
                list2 = list2.next
            elif list1.val <= list2.val:
                l.val = list1.val
                list1 = list1.next

            i += 1

        if list1:
            l.next = list1
        elif list2:
            l.next = list2

        return head
