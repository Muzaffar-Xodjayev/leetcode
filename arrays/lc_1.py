# Leetcode: 1 - Two Sum
# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [h[complement], i]
            h[num] = i
        return []


s1 = Solution()
print(s1.twoSum([3, 2, 4], 6))
