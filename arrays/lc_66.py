# Leetcode: 66 - Plus One
# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_index = len(digits) - 1
        while last_index >= 0:
            if digits[last_index] < 9:
                digits[last_index] += 1
                return digits
            digits[last_index] = 0
            last_index -= 1
        return [1] + digits

s1 = Solution()
print(s1.plusOne([9, 9]))