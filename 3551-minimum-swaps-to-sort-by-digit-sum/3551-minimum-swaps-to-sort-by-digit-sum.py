class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # Sort by (digit_sum, value)
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        
        # Map each value to its target index
        target_indices = {val: i for i, val in enumerate(sorted_nums)}
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or target_indices[nums[i]] == i:
                continue
            
            # Traverse the cycle
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = target_indices[nums[j]]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps
