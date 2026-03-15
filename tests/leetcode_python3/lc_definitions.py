from typing import List, Optional, Dict, Set, Tuple, Deque, Any
from collections import deque

# --- 1. 链表 (Linked List) ---
class ListNode:
    """单链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- 2. 二叉树 (Binary Tree) ---
class TreeNode:
    """二叉树节点定义"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- 3. 多叉树 / 图 / 其他复杂结构 (Generic Node) ---
# 注意：力扣中不同题目对 'Node' 的定义可能不同，以下是几种最常见的：

class Node:
    def __init__(self, val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None,
                 random: 'Node' = None,
                 children: List['Node'] = None,
                 neighbors: List['Node'] = None):
        self.val = val
        self.left = left       # 二叉树/搜索树
        self.right = right     # 二叉树/搜索树
        self.next = next       # 填充每个节点的下一个右侧节点指针 / 带随机指针的链表
        self.random = random   # 复制带随机指针的链表
        self.children = children if children is not None else [] # N叉树
        self.neighbors = neighbors if neighbors is not None else [] # 图