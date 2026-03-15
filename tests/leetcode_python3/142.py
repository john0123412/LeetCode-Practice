# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        index2 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                index1 = fast
                while True:
                    if index1 == index2:
                        return index1
                    index1 = index1.next
                    index2 = index2.next
                break
        else:
            return None
        

#集合法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None