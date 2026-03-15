from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        return sorted(map, key=map.get, reverse=True)[:k]
    

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [num for num, _ in counts.most_common(k)]
    

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
        # 定义小顶堆
        heap = []
        for key, value in map.items():
            if len(heap) < k:
                heapq.heappush(heap, (value,key))
            else:
                heapq.heappushpop(heap, (value,key))
        res = [0]*k
        for i in range(k-1,-1,-1):
            res[i] = heapq.heappop(heap)[1]
        return res
    
#解法一：(和我的第三种一样)

#时间复杂度：O(nlogk)
#空间复杂度：O(n)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #要统计元素出现频率
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
#解法二：
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 使用字典统计数字出现次数
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        # 更改字典，key为出现次数，value为相应的数字的集合
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)
        # 排序
        key = list(index_dict.keys())
        key.sort()
        result = []
        cnt = 0
        # 获取前k项
        while key and cnt != k:
            result += index_dict[key[-1]]
            cnt += len(index_dict[key[-1]])
            key.pop()

        return result[0: k]