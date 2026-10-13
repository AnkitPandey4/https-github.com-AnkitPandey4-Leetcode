class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Sort in-place by absolute values to avoid generating new large lists
        nums.sort(key=lambda x: abs(x))
        
        n = len(nums)
        m = n // 2  # The index threshold splitting the subtraction slots from addition slots
        
        ans = 0
        for i, x in enumerate(nums):
            # The first m smallest squared elements are subtracted
            if i < m:
                ans -= x * x
            # The remaining largest squared elements are added
            else:
                ans += x * x
                
        return ans
