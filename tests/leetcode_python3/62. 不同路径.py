# 定义了m×n的一个网格
#方法一：深搜（时间复杂度大，超时）
class Solution:
    def dfs(self, m, n, i, j, dp):
        if i>= m or j >= n:
            return 0
        if i == m - 1 or j == n - 1:
            return 1
        return self.dfs(m,n,i + 1, j) + self.dfs(m, n, i, j + 1)

    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m,n,1,1,)

# 方法二：dp二维数组
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]


#dp一维数组
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个一维列表用于存储每列的唯一路径数
        dp = [1] * n

        # 计算每个单元格的唯一路径数
        for j in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        # 返回右下角单元格的唯一路径数
        return dp[n - 1]


# 递归
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


#数论方法（算组合数）
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numerator = 1  # 分子
        denominator = m - 1  # 分母
        count = m - 1  # 计数器，表示剩余需要计算的乘积项个数
        t = m + n - 2  # 初始乘积项
        while count > 0:
            numerator *= t  # 计算乘积项的分子部分
            t -= 1  # 递减乘积项
            while denominator != 0 and numerator % denominator == 0:
                numerator //= denominator  # 约简分子
                denominator -= 1  # 递减分母
            count -= 1  # 计数器减1，继续下一项的计算
        return numerator  # 返回最终的唯一路径数
