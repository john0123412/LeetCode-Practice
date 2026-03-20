from typing import List

# 回溯
# 剪枝以防止超时
# k是切割的个数
def canPartitionKSubsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0: return False
    # 必须要能整除
    target = total_sum // k

    # 1. 降序排序：先放大的数字，更容易触发超限剪枝，大幅提升效率
    nums.sort(reverse=True)
    if nums[0] > target: return False  #剪枝

    # k 个桶，初始每个桶的内含价值为 0
    buckets = [0] * k
    # 定义函数backtrack：为当前数字找到合适的桶
    def backtrack(index):
        # 所有数字都放完了，说明方案可行
        if index == len(nums):
            return True

        # 尝试把当前数字 nums[index] 放入第 i 个桶
        for i in range(k):
            # 剪枝：如果当前桶放入后超过了 target，跳过
            if buckets[i] + nums[index] > target:
                continue

            # 剪枝：如果当前桶和前一个桶的值一样，跳过（去重）
            # 因为把数字放进第一个空桶和放进第二个空桶效果是一样的
            if i > 0 and buckets[i] == buckets[i - 1]:
                continue

            # 做选择
            buckets[i] += nums[index]
            # 递归处理下一个数字
            if backtrack(index + 1):
                return True
            # 撤销选择（回溯）
            buckets[i] -= nums[index]

        return False

    return backtrack(0)


# 背包
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False
        target = total_sum // 2
        dp = [0] * (target + 1)

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                # 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])

        if dp[target] == target:
            return True
        else:
            return False


# 卡哥版


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0

        # dp[i]中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        # 总和不会大于20000，背包最大只需要其中一半，所以10001大小就可以了
        dp = [0] * 10001
        for num in nums:
            _sum += num
        # 也可以使用内置函数一步求和
        # _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum // 2

        # 开始 0-1背包
        for num in nums:
            for j in range(target, num - 1, -1):  # 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j] = max(dp[j], dp[j - num] + num)

        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True
        return False


# 卡哥版(简化版)
#

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[-1] == target


# 二维DP版


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化第一行（空子集可以得到和为0）
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # 当前数字大于目标和时，无法使用该数字
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 当前数字小于等于目标和时，可以选择使用或不使用该数字
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target_sum]


# 一维DP版


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:
            # 从target_sum逆序迭代到num，步长为-1
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target_sum]

