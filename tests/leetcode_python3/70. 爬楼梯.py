class Solution:
    def climbStairs(self, n: int) -> int:
        # 初始化
        if n <= 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 版本二：优化空间复杂度
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1, prev2 = 1, 2
        for _ in range(3,n+1):
            sum = prev1+prev2
            prev1 = prev2
            prev2 = sum
        return prev2