#两次for循环，第一次for循环是为了控制每一层的节点数量，第二次for循环是为了遍历每一层的节点并将它们的值添加到当前层的结果列表中。
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
# result // 存放符合条件结果的集合
# path // 用来存放符合条件单一结果
        result = []
        path = []
        def backtracking(n,k,startIndex):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(startIndex,n+1):
                path.append(i)
                backtracking(n,k,i+1)
                path.pop()
        backtracking(n,k,1)
        return result



from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # result // 存放符合条件结果的集合
        # path // 用来存放符合条件单一结果
        result = []
        path = []

        def backtracking(n, k, startIndex):
            if len(path) == k:
                # 创建 path 的副本以避免引用相同对象
                result.append(path[:])
                return
            # 剪枝：如果剩余可选的元素数量加上当前路径中的元素数量已经不足以构成一个长度为 k 的组合
            if (n - startIndex + 1) + len(path) < k:
                return
            for i in range(startIndex, n + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()

        backtracking(n, k, 1)
        return result



# 未剪枝优化

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

#剪枝优化：

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点
