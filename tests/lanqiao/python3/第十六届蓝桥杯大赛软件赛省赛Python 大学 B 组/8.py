
# ### 问题描述

# 小蓝有 n*n* 个数 ai*a**i*，他想知道这 n*n* 个数中的所有数对下标的差值乘上它们的异或之后，得到的结果的和是多少。 也就是说，小蓝想要得到∑i=1n∑j=i+1n(ai⊕aj)×(j−i)*i*=1∑*n**j*=*i*+1∑*n*(*a**i*⊕*a**j*)×(*j*−*i*)的值，其中 ⊕⊕ 表示按位异或。

# ### 输入格式

# 输入的第一行包含一个正整数 n*n*。

# 第二行包含 n*n* 个正整数 a1,a2,⋯,an*a*1,*a*2,⋯,*a**n*，相邻整数之间使用一个空格分隔。

# ### 输出格式

# 输出一行包含一个整数表示答案。

import os
import sys

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int,sys.stdin.readline().strip().split()))
    ans = 0
    max_bit = max(a).bit_length() if a else 0
    for k in range(max_bit):
        cnt0 = 0
        cnt1 = 0
        sum0 = 0
        sum1 = 0
        contrib= 0
        for j in range(n):
            b = (a[j] >> k) & 1
            if b == 1:
                contrib += j * cnt0 - sum0
                cnt1 += 1
                sum1 += j
            else:
                contrib += j * cnt1 - sum1
                cnt0 += 1
                sum0 += j
        ans += contrib * (1 << k)
    print(ans)

solve()





import sys
input = sys.stdin.readline

def solve():
    # ─────────────────────────────────────────
    # 读入数据
    # ─────────────────────────────────────────
    n = int(input())
    a = list(map(int, input().split()))

    # ─────────────────────────────────────────
    # 目标：计算 ∑(i<j) (a[i] ^ a[j]) × (j - i)
    #
    # 核心思路：异或每一位独立，拆开按位计算
    #
    #   原式 = ∑(k=0~B) 2^k × ∑(i<j，第k位不同) (j - i)
    #                    ↑权重      ↑contrib：下标差之和
    #
    # 对每一位 k，"第k位不同" 等价于 "一个是0一个是1"
    # ─────────────────────────────────────────
    ans = 0

    # max(a).bit_length()：最大值的二进制位数，决定枚举到哪一位
    # 例如 max=7=111₂，bit_length=3，枚举 k=0,1,2
    max_bit = max(a).bit_length() if a else 0

    # ─────────────────────────────────────────
    # 第一层：枚举每个二进制位 k
    # ─────────────────────────────────────────
    for k in range(max_bit):

        cnt0 = 0   # j 左边，第k位为 0 的元素个数
        cnt1 = 0   # j 左边，第k位为 1 的元素个数
        sum0 = 0   # j 左边，第k位为 0 的所有下标之和 ∑i
        sum1 = 0   # j 左边，第k位为 1 的所有下标之和 ∑i
        contrib = 0  # 本位所有配对的 (j-i) 之和

        # ─────────────────────────────────────────
        # 第二层：从左到右遍历每个位置 j
        # 遍历到 j 时，cnt/sum 里只有 j 左边的元素
        # 天然保证 i < j，不重不漏
        # ─────────────────────────────────────────
        for j in range(n):

            # 取 a[j] 的第 k 位
            # 原理：先右移 k 位，再 & 1 取最低位
            # 例如 a[j]=6=110₂，k=1：110>>1=11₂，11&1=1
            b = (a[j] >> k) & 1

            if b == 1:
                # 当前位为1，与左边所有"位为0"的下标 i 配对
                # 因为 1 ⊕ 0 = 1，这些对在第k位有贡献
                #
                # ∑(i∈左边位为0) (j - i)
                # = j×cnt0 - sum0
                # 展开：(j-i₁)+(j-i₂)+... = j×cnt0 - (i₁+i₂+...)
                contrib += j * cnt0 - sum0

                # 把 j 自己的信息加入前缀，供后面更大的 j' 使用
                cnt1 += 1
                sum1 += j

            else:
                # 当前位为0，与左边所有"位为1"的下标 i 配对
                # 因为 0 ⊕ 1 = 1，这些对在第k位有贡献
                #
                # ∑(i∈左边位为1) (j - i)
                # = j×cnt1 - sum1
                contrib += j * cnt1 - sum1

                # 把 j 自己的信息加入前缀
                cnt0 += 1
                sum0 += j

            # 注意：先计算 contrib，再更新 cnt/sum
            # 保证计算时 cnt/sum 只包含 j 左边的元素
            # 如果先更新再计算，j 会和自己配对，结果错误

        # contrib 是第k位所有配对的 (j-i) 之和
        # 乘以 2^k（该位权重）才是对答案的真实贡献
        # 1 << k 等价于 2^k，位运算更快
        ans += contrib * (1 << k)

    print(ans)

solve()
