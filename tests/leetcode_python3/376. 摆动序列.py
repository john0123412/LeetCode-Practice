from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prediff = 0
        curdiff = 0
        res = 1
        for i in range(0,len(nums)-1):
            curdiff = nums[i+1] - nums[i]
            if (curdiff < 0 and prediff >= 0) or (curdiff > 0 and prediff <= 0):
                res += 1
                prediff = curdiff

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength([1,7,4,2,5,9,6,8]))





# 贪心（版本一）

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]  # 计算下一个元素与当前元素的差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度


# 贪心（版本二）

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        preDiff, curDiff, result = 0, 0, 1  # 题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]
            if curDiff * preDiff <= 0 and curDiff != 0:  # 差值为0时，不算摆动
                result += 1
                preDiff = curDiff  # 如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return result


# 动态规划（版本一）

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 0 i 作为波峰的最大长度
        # 1 i 作为波谷的最大长度
        # dp是一个列表，列表中每个元素是长度为 2 的列表
        dp = []
        for i in range(len(nums)):
            # 初始为[1, 1]
            dp.append([1, 1])
            for j in range(i):
                # nums[i] 为波谷
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                # nums[i] 为波峰
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[-1][0], dp[-1][1])


# 动态规划（版本二）

class Solution:
    def wiggleMaxLength(self, nums):
        dp = [[0, 0] for _ in range(len(nums))]  # 创建二维dp数组，用于记录摆动序列的最大长度
        dp[0][0] = dp[0][1] = 1  # 初始条件，序列中的第一个元素默认为峰值，最小长度为1
        for i in range(1, len(nums)):
            dp[i][0] = dp[i][1] = 1  # 初始化当前位置的dp值为1
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)  # 如果前一个数比当前数大，可以形成一个上升峰值，更新dp[i][1]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)  # 如果前一个数比当前数小，可以形成一个下降峰值，更新dp[i][0]
        return max(dp[-1][0], dp[-1][1])  # 返回最大的摆动序列长度


# 动态规划（版本三）优化


class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度

        up = down = 1  # 记录上升和下降摆动序列的最大长度
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1  # 如果当前数比前一个数大，则可以形成一个上升峰值
            elif nums[i] < nums[i - 1]:
                down = up + 1  # 如果当前数比前一个数小，则可以形成一个下降峰值

        return max(up, down)  # 返回上升和下降摆动序列的最大长度