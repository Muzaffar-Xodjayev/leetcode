# https://leetcode.com/problems/search-insert-position/
# from typing import List
#
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#             else:
#                 nums.append(target)
#                 nums.sort()
#                 a = (target - nums[-1]) - 1
#                 return len(nums) + a
#
# print(Solution().searchInsert(nums=[1,3,5,6], target=5))
# from typing import List
from os.path import split

# from Tools.scripts.pathfix import keep_flags


# https://leetcode.com/problems/length-of-last-word/
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip().rstrip()
#         s = s.split()
#         return len(s[-1])
#
# print(Solution().lengthOfLastWord(s="   Hello   World    "))


# https://leetcode.com/problems/plus-one/
# from typing import List
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) -1, -1, -1):
#             if digits[i] + 1 != 10:
#                 digits[i] = digits[i] + 1
#                 return digits
#
#             digits[i] = 0
#             if i == 0:
#                 return [1] + digits
#         return digits
#
#
# print(Solution().plusOne(digits=[9, 9]))


# https://leetcode.com/problems/missing-number/
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         a = []
#         for i in range(0, len(nums) + 1):
#             a.append(i)
#
#         for j in a:
#             if j not in nums:
#                 return j
#
# print(Solution().missingNumber(nums=[0, 1]))


# https://leetcode.com/problems/climbing-stairs/
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if 1 <= n and n <= 45:
#             a = 0
#             b = 1
#             for i in range(n):
#                 a, b = b, a + b
#             return b
#         else:
#             return 1
#
#
# print(Solution().climbStairs(n=5))


# https://leetcode.com/problems/single-number/
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             b = nums[:]
#             a = b.pop(i)
#             if a not in b:
#                 return a
#
#
# print(Solution().singleNumber([1, 0, 1]))


# https://leetcode.com/problems/power-of-three/
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         for i in range(31):
#             if 3 ** i == n:
#                 return True
#             continue
#         return False


# https://leetcode.com/problems/contains-duplicate/
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return not len(set(nums)) == len(nums)
#
#
# print(Solution().containsDuplicate([1, 2, 3, 4]))


# https://leetcode.com/problems/majority-element/
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         a = list(set(nums))
#         for i in a:
#             c = nums.count(i)
#             if c > (len(nums) / 2):
#                 return i
#
#
# print(Solution().majorityElement([2,2,1,1,1,2,2]))


# https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         return max((x*3 for x,y,z in zip(num, num[1:], num[2:]) if x==y==z), default='')
#
#
# print(Solution().largestGoodInteger("423523338"))


# https://leetcode.com/problems/power-of-four

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         elif n <= 0:
#             return False
#
#         while n > 4:
#             n /= 4
#
#         if n == 4:
#             return True
#
#         return False
#
# print(Solution().isPowerOfFour(16))


# https://leetcode.com/problems/maximum-69-numbe

# class Solution:
#     def maximum69Number(self, num: int) -> int:
#         s = str(num)
#         a = [int(i) for i in s]
#         a = sorted(a, reverse=True)
#         r = int("".join(map(str, a)))
#         return r
#
#
# print(Solution().maximum69Number(9669))


# https://leetcode.com/problems/move-zeroes/
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         left = 0
#         for right in range(len(nums)):
#             if nums[right] != 0:
#                 nums[right], nums[left] = nums[left], nums[right]
#                 left += 1
#
# print(Solution().moveZeroes([1,0,2,0,3]))


# https://leetcode.com/problems/reverse-string/

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#
#
# print(Solution().reverseString(["h","e","l","l","o"]))


# https://leetcode.com/problems/is-subsequence/
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         pass
#
#
# print(Solution().isSubsequence(s="abc", t="ahbgdc"))


# https://leetcode.com/problems/find-the-difference/
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         # Initialize a dictionary to store character counts
#         count = {}
#
#         # Count characters in string t
#         for c in t:
#             count[c] = count.get(c, 0) + 1
#
#         # Subtract counts for characters in string s
#         for c in s:
#             count[c] -= 1
#             if count[c] == 0:
#                 del count[c]
#
#         # The remaining character in the dictionary is the difference
#         return list(count.keys())[0]
#
#
# print(Solution().findTheDifference(s="abcd", t="abcde"))


# class Solution:
#     def makingTree(self, n: int, k: int):
#         a = round(n / 2)
#         while a > 0:
#             for i in range(1, n + 1, 2):
#                 print(" " * a + "*" * i)
#                 a -= 1
#
#             for j in range(1, k + 1):
#                 print(" " * ((n // 2) - 2) + "*" * k)
#
#
#
# print(Solution().makingTree(n=50, k=5))


# https://leetcode.com/problems/add-binary/

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         dec_b = int(b, 2)
#         dec_a = int(a, 2)
#         sum_dec = dec_a + dec_b
#         sum_bin = bin(sum_dec)
#         return sum_bin[2:]
#
#
# print(Solution().addBinary(a="11", b="1"))


# https://leetcode.com/problems/merge-sorted-array/
# from typing import List
#
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n > 0:
#             nums1[m:] = nums2
#             nums1.sort()
#
#
# print(Solution().merge(nums1=[1,2,3,0,0,0], nums2=[2,5,6], m=3, n=3))


# https://leetcode.com/problems/valid-palindrome/description/
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(char for char in s if char.isalnum()).lower()
#         if s == s[::-1]:
#             return True
#         return False
#
#
# print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))


# https://leetcode.com/problems/add-digits/description/
# class Solution:
#     def addDigits(self, num: int) -> int:
#         while len(str(num)) > 1:
#             a = 0
#             for i in str(num):
#                 a += int(i)
#             num = a
#         return num
#
#
# print(Solution().addDigits(38))


# https://leetcode.com/problems/reverse-vowels-of-a-string/
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = ['a', 'A', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
#         ind = []
#         for i, j in enumerate(s):
#             if j in vowels:
#                 ind.append(i)
#
#         r = ind[:]
#         r.reverse()
#         a = s
#         for i in range(len(ind)):
#             s = list(s)
#             s[ind[i]] = a[r[i]]
#         s = "".join(s)
#         return s
#
#
#
# print(Solution().reverseVowels(s="IceCreAm"))


# https://leetcode.com/problems/intersection-of-two-arrays/
# from typing import List
#
#
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         a = []
#         for i in nums1:
#             if i in nums2:
#                 a.append(i)
#
#         return list(set(a))
#
#
# print(Solution().intersection(nums1=[1,2,2,1], nums2=[2,2]))


# BINARY SEARCH
# import time
#
# class Solution:
#     start_time = time.perf_counter()
#     def binarySearch(self, nums: list, k: int) -> int:
#         nums = sorted(nums)
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == k:
#                 return mid
#             elif nums[mid] < k:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"{elapsed_time:.6f}")
#
#
# print(Solution().binarySearch(nums=list(range(1,10000)), k=71299))


# https://leetcode.com/problems/ransom-note/
# from collections import Counter
#
#
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         c = Counter(ransomNote)
#         c2 = Counter(magazine)
#         return c == c2
#
#
#
# print(Solution().canConstruct(ransomNote="aab", magazine="baa"))


# https://leetcode.com/problems/third-maximum-number/
# from typing import List
#
#
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         n = 1
#         nums.sort(reverse=True)
#         prev_elem = nums[0]
#
#         for i in range(len(nums)):
#             if nums[i] != prev_elem:
#                 n += 1
#                 prev_elem = nums[i]
#
#             if n == 3:
#                 return nums[i]
#
#         return nums[0]
#
#
#
# print(Solution().thirdMax([2,2,3,1]))


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# from typing import List
#
#
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         arr = set(nums)
#         res = []
#         for i in range(1, len(nums)+1):
#             if i not in arr:
#                 res.append(i)
#         return res
#
#
# print(Solution().findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1]))


# https://leetcode.com/problems/fibonacci-number/
# class Solution:
#     def fib(self, n: int) -> int:
#         f0 = 0
#         f1 = 1
#         for i in range(n):
#             f2 = f1 + f0
#             f0 = f1
#             f1 = f2
#         print(f1)
#
#
# print(Solution().fib(n=4))


# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=daily-question&envId=2025-09-13
# from collections import Counter
#
#
# class Solution:
#     def maxFreqSum(self, s: str) -> int:
#         c = Counter(s)
#         print(c)
#
#
# print(Solution().maxFreqSum("successes"))


# https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=daily-question&envId=2025-09-15
# class Solution:
#     def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
#         text = text.split()
#         a = 0
#         for i in text:
#             for j in brokenLetters:
#                 if j in i:
#                     break
#             else:
#                 a += 1
#
#         return a
#
#
# print(Solution().canBeTypedWords(text="leet code", brokenLetters="lt"))
