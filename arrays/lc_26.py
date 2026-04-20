# Leetcode: 26. Remove duplicates from array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k


s1 = Solution()
print(s1.removeDuplicates([1,1,1,1]))