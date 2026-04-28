# Leetcode: 217 - Contains Duplicate
from typing import List



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l  = list(set(nums))
        if len(l) != len(nums):
            return True
        return False

s1 = Solution()
print(s1.containsDuplicate([3,1]))
