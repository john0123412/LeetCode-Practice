from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        num_set = set(nums1)
        res = set()
        for num in nums2:
            if num in num_set:
                res.add(num)
        return list(res)
    

# 暴力方法
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = set()
#         for num1 in nums1:
#             for num2 in nums2:
#                 if num1 == num2:
#                     res.add(num1)
#         return list(res)


#参考
#（版本一） 使用字典和集合

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)
#（版本二） 使用数组

	
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0]*1001
        count2 = [0]*1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]]+=1
        for j in range(len(nums2)):
            count2[nums2[j]]+=1
        for k in range(1001):
            if count1[k]*count2[k]>0:
                result.append(k)
        return result
	
#（版本三） 使用集合

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))