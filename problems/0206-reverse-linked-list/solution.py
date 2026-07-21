# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        prev = None
        while tail:
            nxt = tail.next
            tail.next = prev
            prev = tail
            tail = nxt
        return prev
