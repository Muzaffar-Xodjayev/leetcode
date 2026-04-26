# LeetCode: 121 - Best time to buy and sell Stock
from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < min_price:
                min_price = i

            profit = max(profit, i - min_price)
        return profit




s1 = Solution()
print(s1.maxProfit([7,6,4,3,1]))