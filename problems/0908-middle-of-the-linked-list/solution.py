# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val #1
#         self.next = next #2 # val
#              self.next = next #3 next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        middle = cnt // 2

        cur = head
        for _ in range(middle):
            cur = cur.next
        return cur

