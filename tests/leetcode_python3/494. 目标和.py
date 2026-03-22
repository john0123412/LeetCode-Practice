from typing import List
# 动态规划（二维数组）

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        bagsize = (total + target) // 2
        n = len(nums)
        dp = [[0] * (bagsize + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # dp[i][j]：使用前 i 个数字（nums[0..i-1]）凑出和 j 的方案数
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(bagsize + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]

        return dp[n][bagsize]


# 动态规划（一维数组）

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        bagsize = (total + target) // 2
        n = len(nums)
        dp = [0] * (bagsize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagsize,nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]
        return dp[bagsize]