class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = list(accumulate(stones))
        
       
        res = prefix[-1]
        
        for i in range(n - 2, 0, -1):
            res = max(res, prefix[i] - res)
            
        return res
