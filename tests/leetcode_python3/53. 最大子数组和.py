from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result


# 法二：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*(len(nums))   #dp数组是一个一维数组，dp[i]表示以nums[i]结尾的最大子数组和
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            if dp[i] > result:
                result = dp[i]  #result保存最大的dp[i]
        return result


#leetcode top 1%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_i = nums[0]
        max_sub_sum = max_i
        for num in nums[1:]:
            if max_i <= 0:
                max_i = num
            else:
                max_i = num + max_i
            # max_sub_sum = max(max_i, max_sub_sum)
            if max_i > max_sub_sum:
                max_sub_sum = max_i
        return max_sub_sum


# Python
# 暴力法

class Solution:
    def maxSubArray(self, nums):
        result = float('-inf')  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):  # 设置起始位置
            count = 0
            for j in range(i, len(nums)):  # 从起始位置i开始遍历寻找最大值
                count += nums[j]
                result = max(count, result)  # 更新最大值
        return result

# 贪心法

class Solution:
    def maxSubArray(self, nums):
        result = float('-inf')  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count
            if count <= 0:  # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                count = 0
        return result
# 动态规划

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res
# 动态规划

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        dp = [0] * len(nums)    # dp[i]表示包括i之前的最大连续子序列和
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])   # 状态转移公式
            if dp[i] > result:
                result = dp[i]                      # result 保存dp[i]的最大值
        return result
# 动态规划优化

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf") # 初始化结果为负无穷大，方便比较取最大值
        current_sum = 0         # 初始化当前连续和

        for num in nums:

            # 更新当前连续和
            # 如果原本的连续和加上当前数字之后没有当前数字大，说明原本的连续和是负数，那么就直接从当前数字开始重新计算连续和
            current_sum = max(current_sum+num, num)
            max_sum = max(max_sum, current_sum) # 更新结果

        return max_sum
