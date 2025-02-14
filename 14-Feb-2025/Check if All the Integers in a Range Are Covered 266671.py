# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        numbers = set()
        for r in ranges:
            numbers.update(range(r[0], r[1] + 1))

        if all(num in numbers for num in range(left, right+1)):
            return True
        else:
            return False