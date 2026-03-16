class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[n]

# 版本二：优化空间复杂度
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp0 = 0
        dp1 = 0
        for i in range(2,n+1):
            dpi = min(dp1+cost[i-1],dp0+cost[i-2])
            dp0 = dp1
            dp1 = dpi
        return dp1
