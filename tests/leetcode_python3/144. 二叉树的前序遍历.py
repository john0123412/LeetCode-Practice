# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List, TreeNode #TreeNode 通常由平台提供。如果在本地测试，可能需要自己定义 TreeNode 类。
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    

#法二：迭代
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    
#空指针标记法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None) #空指针标记
            else:
                node = stack.pop()
                res.append(node.val)
        return res