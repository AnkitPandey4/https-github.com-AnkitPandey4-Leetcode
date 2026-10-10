class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diffs = [0] * 100001
        total_diff = 0
        max_diff = 0
        
        # 1. Count frequencies of absolute differences
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            if d > 0:
                diffs[d] += 1
                total_diff += d
                max_diff = max(max_diff, d)
        
        k_sum = k1 + k2
        
        # If we have enough operations to make all differences 0
        if total_diff <= k_sum:
            return 0
        
        # 2. Greedily reduce the largest differences
        for i in range(max_diff, 0, -1):
            if diffs[i] > 0:
                # How many operations needed to reduce diffs[i] to i - 1
                reduce_count = min(k_sum, diffs[i])
                diffs[i] -= reduce_count
                diffs[i - 1] += reduce_count
                k_sum -= reduce_count
                
                if k_sum == 0:
                    break
        
        # 3. Calculate the sum of squares
        ans = 0
        for i in range(1, 100001):
            if diffs[i] > 0:
                ans += (i * i) * diffs[i]
                
        return ans
