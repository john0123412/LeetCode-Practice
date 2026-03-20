class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1
        dp = [0] * (n+1)
        # dp表示整数i拆分成至少两个正整数的最大乘积
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i],dp[i-j]*j,j*(i-j))
        return dp[n]

    # 贪心（数学证明法）
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        if n == 5:
            return 6
        res = 1
        while n>4:
            res *= 3
            n -= 3
        res *= n
        return res
