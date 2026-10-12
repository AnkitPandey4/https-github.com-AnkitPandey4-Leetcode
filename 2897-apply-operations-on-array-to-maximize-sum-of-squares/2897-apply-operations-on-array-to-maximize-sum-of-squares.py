class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 1_000_000_007
        MAX_BIT = 30
        
        cnt = [0] * MAX_BIT
        for num in nums:
            for i in range(MAX_BIT):
                if (num >> i) & 1:
                    cnt[i] += 1
        
        ans = 0
        for _ in range(k):
            cur = 0
            for i in range(MAX_BIT - 1, -1, -1):
                if cnt[i] > 0:
                    cnt[i] -= 1
                    cur |= (1 << i)
            ans = (ans + cur * cur) % MOD
            
        return ans
