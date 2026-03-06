# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from typing import ListNode
class Solution:
    # 方法1：使用虚拟头结点 + 头插法（不需要栈）
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用虚拟头结点，通过头插法实现链表的反转
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        # 创建虚拟头结点
        dummy_head = ListNode(-1)
        dummy_head.next = None
        
        # 遍历所有节点
        cur = head
        while cur is not None:
            temp = cur.next
            # 头插法：将当前节点插入到虚拟头结点之后
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = temp
        
        return dummy_head.next
    
    # 方法2：使用栈解决反转链表
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        使用栈实现链表反转
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        # 如果链表为空，则返回空
        if head is None:
            return None
        
        # 如果链表中只有一个元素，则直接返回
        if head.next is None:
            return head
        
        # 创建栈，每一个结点都入栈
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur)
            cur = cur.next
        
        # 创建一个虚拟头结点
        dummy_head = ListNode(0)
        cur = dummy_head
        while stack:
            node = stack.pop()
            cur.next = node
            cur = cur.next
        
        # 最后一个元素的next要赋值为空
        # 注意：当出栈循环结束后，cur正好指向原来链表的第一个结点
        # 此时该结点的next可能指向其他节点，因此需要断开连接
        cur.next = None
        
        return dummy_head.next

        