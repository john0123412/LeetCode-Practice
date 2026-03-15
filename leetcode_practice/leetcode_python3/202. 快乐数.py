class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        l = len(s)
        while n != 1:
            total = 0
            for i in range(l):
                total += int(s[i])**2
            n = total
            s = str(n)
            l = len(s)
            if n == 4:
                return False
        return True
    

# 法2：算重复数
class Solution:
    def isHappy(self, n: int) -> bool:
        num = set()
        s = str(n)
        l = len(s)
        while n != 1:
            total = 0
            for i in range(l):
                total += int(s[i])**2
            n = total
            s = str(n)
            l = len(s)
            if n in num:
                return False
            else:
                num.add(n)   
        return True
    
# 参考答案
#(版本一)使用集合

class Solution:
    def isHappy(self, n: int) -> bool:        
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num
#(版本二)使用集合

class Solution:
   def isHappy(self, n: int) -> bool:
       record = set()
       while n not in record:
           record.add(n)
           new_num = 0
           n_str = str(n)
           for i in n_str:
               new_num+=int(i)**2
           if new_num==1: return True
           else: n = new_num
       return False
#(版本三)使用数组

class Solution:
   def isHappy(self, n: int) -> bool:
       record = []
       while n not in record:
           record.append(n)
           new_num = 0
           n_str = str(n)
           for i in n_str:
               new_num+=int(i)**2
           if new_num==1: return True
           else: n = new_num
       return False
#(版本四)使用快慢指针

class Solution:
   def isHappy(self, n: int) -> bool:        
       slow = n
       fast = n
       while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
           slow = self.get_sum(slow)
           fast = self.get_sum(self.get_sum(fast))
           if slow == fast:
               return False
       return True
   def get_sum(self,n: int) -> int: 
       new_num = 0
       while n:
           n, r = divmod(n, 10)
           new_num += r ** 2
       return new_num
#(版本五)使用集合+精简

class Solution:
   def isHappy(self, n: int) -> bool:
       seen = set()
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.add(n)
       return True
#(版本六)使用数组+精简

class Solution:
   def isHappy(self, n: int) -> bool:
       seen = []
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.append(n)
       return True