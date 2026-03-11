# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List, TreeNode #TreeNode 通常由平台提供。如果在本地测试，可能需要自己定义 TreeNode 类。
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        res = []
        if not root:
            return []
        if root:
            que.append(root)
        while que:
            size = len(que)   #size 记录当前层的节点数量
            vector = []
            while size > 0:
                node = que.popleft()
                vector.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                size -= 1
            res.append(vector)
        return res

#递归法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = []

        def traverse(node, level):
            if not node:
                return

            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return levels
