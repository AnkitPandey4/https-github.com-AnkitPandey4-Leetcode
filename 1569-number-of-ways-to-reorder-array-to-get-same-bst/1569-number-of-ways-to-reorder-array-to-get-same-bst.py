import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(elements: List[int]) -> int:
            if len(elements) <= 2:
                return 1
            
            root = elements[0]
            left = [x for x in elements[1:] if x < root]
            right = [x for x in elements[1:] if x > root]
            
            
            total_slots = len(elements) - 1
            combinations = math.comb(total_slots, len(left)) % MOD
            
            return (combinations * dfs(left) * dfs(right)) % MOD

        return (dfs(nums) - 1) % MOD
