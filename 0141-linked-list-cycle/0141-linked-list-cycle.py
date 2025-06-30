# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        my_map = set()
        if head:
            curr = head
        else:
            return False

        while curr:
            if curr in my_map:
                return True
                break
            
            my_map.add(curr)
            curr = curr.next
        
        return False

        