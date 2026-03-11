# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List, TreeNode #TreeNode 通常由平台提供。如果在本地测试，可能需要自己定义 TreeNode 类。
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    
#法二：迭代(中序遍历的迭代实现比较麻烦，主要是需要一个指针来记录当前访问的节点)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res

#空指针标记法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None) #空指针标记
                if node.left:
                    stack.append(node.left)
            else:
                node =stack.pop()
                res.append(node.val)
        return res
    
#升级：bollean标记法（超出内存限制，力扣）
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack = [(root,False)] if root else []  # 多加一个参数，False 为默认值
        while stack:
            node, visited = stack.pop() # 多加一个 visited 参数，使“迭代统一写法”成为一件简单的事
            if visited:             # visited 为 True，表示该节点和两个儿子的位次之前已经安排过了，现在可以收割节点了
                values.append(node.val)
 
            # visited 当前为 False, 表示初次访问本节点，此次访问的目的是“把自己和两个儿子在栈中安排好位次”。
            # 中序遍历是'左中右'，右儿子最先入栈，最后出栈。
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True)) # 将当前节点重新入栈，并将 visited 设置为 True
            if node.left:
                stack.append((node.left, False))
        return values
        

