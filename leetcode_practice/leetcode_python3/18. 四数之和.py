#双指针
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for k in range(n):
            if nums[k] > target and target >= 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            for i in range(k+1,n):
                if nums[k] + nums[i] > target and target > 0:
                    break
                if i > k+1 and nums[i] == nums[i-1]:
                    continue
                left,right = i+1,n-1
                while left < right:
                    total = nums[k] + nums[i] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[k],nums[i],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
    
#(版本二) 使用字典,慢

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 创建一个字典来存储输入列表中每个数字的频率
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # 创建一个集合来存储最终答案，并遍历4个数字的所有唯一组合
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in freq:
                        # 确保没有重复
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if freq[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
        
        return [list(x) for x in ans]
    

#力扣高效方法
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n-3):
            x = nums[a]
            if a > 0 and x == nums[a-1]:
                continue # 跳过重复数字
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] >target :
                break
            if x + nums[-1] + nums[-2] + nums[-3] < target:
                continue  ##跳过不可能的情况,多层剪枝
            for b in range(a+1,n-2):#因为b的最大值就是n- 3 + 1 -1
                y = nums[b]
                if b > a + 1 and y == nums[b - 1]:
                    continue
                if x + y + nums[b + 1] + nums[b + 2] > target:
                    break
                if x + y + nums[-1] + nums[-2] < target:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]
                    if s > target:
                        d -=  1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([x,y,nums[c],nums[d]] )
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return ans
