from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        def backtracking(k,n,startIndex,path,result):
            if len(path) == k and sum(path) == n:
                result.append(path[:])
                return
            for i in range(startIndex,10):
                if sum(path) + 1 > n:
                    return
                path.append(i)
                backtracking(k,n,i+1,path,result)
                path.pop()
        backtracking(k,n,1,path,result)
        return result


#优化，剪枝
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 0, 1, [], result)
        return result

    def backtracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:  # 剪枝操作
            return  # 如果currentSum已经超过targetSum，则直接返回
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):  # 剪枝，限制当前层起点之后的可选上界，避免无效搜索
            currentSum += i  # 处理
            path.append(i)  # 处理
            self.backtracking(targetSum, k, currentSum, i + 1, path, result)  # 注意i+1调整startIndex
            currentSum -= i  # 回溯
            path.pop()  # 回溯