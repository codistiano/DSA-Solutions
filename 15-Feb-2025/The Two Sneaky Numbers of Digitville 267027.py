# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        uniqueNums = set(nums)
        result = []

        for num in uniqueNums:
            if nums.count(num) > 1:
                result.append(num)

        return result