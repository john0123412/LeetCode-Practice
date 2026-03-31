
# 设有两个二维向量 A→(XA,YA),B→(XB,YB)*A*(*X**A*,*Y**A*),*B*(*X**B*,*Y**B*)。给定 L*L*，求 (XA,YA),(XB,YB)(*X**A*,*Y**A*),(*X**B*,*Y**B*) 有多少种不同的取值，使得：

# 1. XA,YA,XB,YB*X**A*,*Y**A*,*X**B*,*Y**B* 均为正整数；
# 2. A→⋅B→≤L*A*⋅*B*≤*L*，其中 A→⋅B→*A*⋅*B* 表示 A→,B→*A*,*B* 的内积，即 XA⋅XB+YA⋅YB*X**A*⋅*X**B*+*Y**A*⋅*Y**B*。

# ### 输入格式

# 输入的第一行包含一个正整数 L*L*，表示题目描述中的限制条件。

# ### 输出格式

# 输出一行包含一个整数表示答案。

import sys
import os

def solve():
    
    L = int(sys.stdin.readline().strip())

# 原问题化简为求满足：对于每一个确定的 $u$，满足 $X_A \cdot X_B = u$ 的正整数对 $(X_A, X_B)$ 的数量恰好等于 $u$ 的约数个数，记作 $d(u)$。
# 同理，满足 $Y_A \cdot Y_B = v$ 的正整数对数量为 $d(v)$。
# 因此，总的取值方案数为：$$\sum_{u=1}^{L-1} \left( d(u) \cdot \sum_{v=1}^{L-u} d(v) \right)$$为了提高效率，我们令 $S(k) = \sum_{i=1}^{k} d(i)$，即约数个数的前缀和。那么公式可以简化为：$$\text{Ans} = \sum_{u=1}^{L-1} d(u) \cdot S(L-u)$$

    if L < 2:
        print(0)
        return
    
    # 计算 1 到 L-1 的约数个数 d(i)
    # 使用筛法，时间复杂度 O(L log L)
    d = [0] * (L +  1)
    for i in range(1,L+1):
        for j in range(1,L+1,i):
            d[j] += 1

    # 计算约数个数的前缀和 S(k)
    s = [0] * (L + 1)
    for i in range(1,L+1):
        s[i] = s[i-1] + s[i]

    # 3. 根据公式计算最终答案
    # Ans = sum( d(u) * S(L-u) ) for u from 1 to L-1
    total = 0
    for u in range(1,L):
        total += d(u) * s[L-u]
    print(total)

if __name__ == "__main__":
    solve()