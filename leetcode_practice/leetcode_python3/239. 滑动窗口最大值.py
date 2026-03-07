#暴力算法（超时）
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result


#双端队列（deque）算法
from collections import deque
class Solution:
    class my_deque:
        def __init__(self):
            self.que = deque()
        def pop(self,value: int):
            if self.que and self.que[0] == value:
                self.que.popleft()
        def push(self,value: int):
            while self.que and self.que[-1] < value:
                self.que.pop()
            self.que.append(value)
        def front(self) -> int:
            return self.que[0]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        que = self.my_deque()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k,len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result

#解法一：使用自定义的单调队列类
from collections import deque


class MyQueue: #单调队列（从大到小
    def __init__(self):
        self.queue = deque() #这里需要使用deque实现单调队列，直接使用list会超时
    
    #每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    #同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()#list.pop()时间复杂度为O(n),这里需要使用collections.deque()
            
    #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
    #这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
        
    #查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k): #先将前k的元素放进队列
            que.push(nums[i])
        result.append(que.front()) #result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k]) #滑动窗口移除最前面元素
            que.push(nums[i]) #滑动窗口前加入最后面的元素
            result.append(que.front()) #记录对应的最大值
        return result
#解法二：直接用单调队列
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = [] # 结果集合
        kept_nums = deque() # 单调队列

        for i in range(len(nums)):
            update_kept_nums(kept_nums, nums[i]) # 右侧新元素加入

            if i >= k and nums[i - k] == kept_nums[0]: # 左侧旧元素如果等于单调队列头元素，需要移除头元素
                kept_nums.popleft()

            if i >= k - 1:
                max_list.append(kept_nums[0])

        return max_list

def update_kept_nums(kept_nums, num): # num 是新加入的元素
    # 所有小于新元素的队列尾部元素，在新元素出现后，都是没有价值的，都需要被移除
    while kept_nums and num > kept_nums[-1]:
        kept_nums.pop()

    kept_nums.append(num)