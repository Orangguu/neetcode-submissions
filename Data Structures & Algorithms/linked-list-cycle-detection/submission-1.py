# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_ptr = head
        slow_ptr = head
        idx = 0

        while slow_ptr:

            print("fast_ptr = ", fast_ptr)
            print("slow_ptr = ", slow_ptr)

            if slow_ptr == fast_ptr and idx != 0:
                return True

            if fast_ptr:
                fast_ptr = fast_ptr.next
                if fast_ptr:
                    fast_ptr = fast_ptr.next


            slow_ptr = slow_ptr.next

            idx += 1
        return False

