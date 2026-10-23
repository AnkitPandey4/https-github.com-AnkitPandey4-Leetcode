from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Initialize ans to -1 (all binary bits set to 1)
        ans = -1
        
        for i, x in enumerate(nums):
            # Check if the element is out of its sorted position
            if i != x:
                ans &= x
                
        
        return max(ans, 0)
