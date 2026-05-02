import unittest
from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    count = Counter(nums1)
    res = []

    for i in nums2:
        if count[i] > 0:
            res.append(i)
            count[i] -= 1
    return res


class TestIntersect(unittest.TestCase):

    def assert_intersection(self, nums1, nums2, expected):
        """Helper: sort both sides so order doesn't matter"""
        self.assertEqual(sorted(intersect(nums1, nums2)), sorted(expected))

    # ── Normal Cases ─────────────────────────────────────
    def test_basic_with_duplicates(self):
        self.assert_intersection([1,2,2,1], [2,2], [2,2])

    def test_no_duplicates(self):
        self.assert_intersection([4,9,5], [9,4,9,8,4], [4,9])

    def test_partial_overlap(self):
        self.assert_intersection([1,1,2], [1,1,1], [1,1])

    def test_all_match(self):
        self.assert_intersection([3,3,3], [3,3,3], [3,3,3])

    # ── Edge Cases ───────────────────────────────────────
    def test_no_intersection(self):
        self.assert_intersection([1,2,3], [4,5,6], [])

    def test_first_array_empty(self):
        self.assert_intersection([], [1,2,3], [])

    def test_second_array_empty(self):
        self.assert_intersection([1,2,3], [], [])

    def test_both_empty(self):
        self.assert_intersection([], [], [])

    def test_single_match(self):
        self.assert_intersection([5], [5], [5])

    def test_single_no_match(self):
        self.assert_intersection([5], [6], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
