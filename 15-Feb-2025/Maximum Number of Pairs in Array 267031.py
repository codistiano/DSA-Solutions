# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)

        answer = [0, 0]

        for num in nums:
            h[num] += 1
        
        for num in nums:
            if h[num] > 1:
                answer[0] += 1
                h[num] -= 2
            elif h[num] == 1:
                answer[1] += 1
                h[num] -= 1
        
        return answer