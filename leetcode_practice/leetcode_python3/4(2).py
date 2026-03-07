from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        half_len = (m + n + 1) // 2
        
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return float(max_of_left)
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])
                
                return (max_of_left + min_of_right) / 2.0

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    print(f"Example 1: nums1={nums1}, nums2={nums2}")
    print(f"Output: {sol.findMedianSortedArrays(nums1, nums2)}")
    
    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"Example 2: nums1={nums1}, nums2={nums2}")
    print(f"Output: {sol.findMedianSortedArrays(nums1, nums2)}")
