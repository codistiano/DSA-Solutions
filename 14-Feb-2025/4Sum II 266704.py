# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        h = defaultdict(int)
        count = 0

        for i in nums1:
            for j in nums2:
                key = i + j
                h[key] += 1
        
        for i in nums3:
            for j in nums4:
                key = i + j
                count += h.get(-key, 0)
        
        return count